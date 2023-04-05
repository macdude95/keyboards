import board
import displayio
import adafruit_displayio_ssd1306
import busio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
from adafruit_bitmap_font import bitmap_font
from displayio import Bitmap
import keyMaps


# TODO: Find space on oled thing to display win/mac toggle and qwerty/colemak toggle
class OLEDContext:
    def __init__(self, keyboard, width=128, height=64):
        self.width = width
        self.height = height

        # Clear OLED and prep a group to add to
        displayio.release_displays()
        i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
        display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
        self.splash = displayio.Group()
        display.show(self.splash)
        self.active_layers = []
        self.font = bitmap_font.load_font("fonts/ib8x8u.bdf", Bitmap)
        glyphs_string = "".join(set(keyMaps.kcToCharDict.values()))
        self.font.load_glyphs(glyphs_string)
        self.updateState(keyboard)

        self.layer_circles = self.createLayerCirclesList()
        layer_circle_group = displayio.Group()
        for c in self.layer_circles:
            layer_circle_group.append(c)
        self.layerTextTitle, self.layerTextBody = self.createLayerTextView()
        self.splash.append(layer_circle_group)
        self.splash.append(self.layerTextTitle)
        self.splash.append(self.layerTextBody)

    def isUpdateAvailable(self, keyboard):
        return keyboard.active_layers != self.active_layers

    def onUpdate(self, keyboard):
        if not self.isUpdateAvailable(keyboard):
            return
        self.updateState(keyboard)
        self.updateDisplay()

    def updateDisplay(self):
        self.layerTextTitle.text = self.createTitleString()
        self.layerTextBody.text = self.createBodyString()
        for c in self.layer_circles:
            c.fill = 0x000000
        self.layer_circles[self.current_active_layer_idx].fill = 0xFFFFFF

    def updateState(self, keyboard):
        self.active_layers = keyboard.active_layers.copy()
        self.total_layers_count = len(keyboard.keymap)
        self.current_active_layer_idx = max(self.active_layers)
        self.current_active_layer = keyboard.keymap[self.current_active_layer_idx]

    # TODO: Only show circles for non-toggle layers (exclude colemak/querty/windows/mac from list)
    def createLayerCirclesList(self):
        layer_circles = []
        circle_count = self.total_layers_count
        padding = 2
        spacing = 2
        diameter = int(self.height / circle_count) - spacing
        radius = int(diameter / 2)
        for i in range(circle_count):
            fill = 0xFFFFFF if i is self.current_active_layer_idx else 0x000000
            yPos = int(i * self.height / circle_count) + radius
            xPos = 128 - radius - padding
            circle = Circle(xPos, yPos, radius, fill=fill, outline=0xFFFFFF, stroke=2)
            layer_circles.append(circle)
        return layer_circles

    def createLayerTextView(self):
        xOffset = -5
        titleLabel = label.Label(
            self.font,
            text=self.createTitleString(),
            color=0xFFFFFF,
            anchored_position=(self.width / 2 + xOffset, 0),
            scale=2,
            anchor_point=(0.5, 0),
        )
        bodyLabel = label.Label(
            self.font,
            text=self.createBodyString(),
            color=0xFFFFFF,
            anchored_position=(self.width / 2 + xOffset, self.height / 2 - 10),
            scale=1,
            anchor_point=(0.5, 0),
        )

        return titleLabel, bodyLabel

    def createBodyString(self):
        helpTextString = ""
        keyCount = 0
        for keyCode in self.current_active_layer:
            if keyCount is 5:
                helpTextString += "   "  # Add gap between hands
            elif keyCount >= 10:
                keyCount = 0
                helpTextString += "\n"
            helpTextString += keyMaps.convertKCtoChar(keyCode)
            keyCount += 1

        return helpTextString

    def createTitleString(self):
        currentLayer = max(self.active_layers)

        layerTextDict = {
            0: "QWERTY",
            1: "COLEMAK",
            2: "SYMBOL",
            3: "→←↓↑ #",
            4: "SYS/FUN",
        }
        return layerTextDict[currentLayer]
