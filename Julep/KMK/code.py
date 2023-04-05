from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
import board
import oled
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap
import keyMaps

print("Starting")


def setupKMKKeyboard():
    k = KMKKeyboard()

    k.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5)  # Rows
    k.col_pins = (
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
    )  # Cols
    k.diode_orientation = DiodeOrientation.COL2ROW

    k.modules.append(Layers())
    k.extensions.append(MediaKeys())
    k.modules.append(ModTap())

    k.keymap = keyMaps.getKeymap()
    return k


# This code will run each time the keyboard update loop runs
def onUpdate():
    oledContext.onUpdate(keyboard)
    pass


keyboard = setupKMKKeyboard()
oledContext = oled.OLEDContext(keyboard)


def main():
    keyboard.go(onUpdate)


if __name__ == "__main__":
    main()
