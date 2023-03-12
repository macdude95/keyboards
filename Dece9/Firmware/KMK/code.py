from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import usb_hid
import usb_cdc
import storage
import digitalio
import supervisor
import board

# Extra imports
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

print("Starting")
keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP6, board.GP7, board.GP8)  # Cols
keyboard.row_pins = (board.GP10, board.GP11, board.GP12)  # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# NOTE: Uncomment this line if you want to go into debug mode, then follow these instructions: https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux
# keyboard.debug_enabled = True

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

# any tap longer than 250ms will be interpreted as a hold
LAYER_TAP = KC.LT(1, KC.KP_7, prefer_hold=True,
                  tap_interrupted=False, tap_time=250)

# Keymap
keyboard.keymap = [
    # Base Layer
    [
        KC.KP_1, KC.KP_2, KC.KP_3,
        KC.KP_4, KC.KP_5, KC.KP_6,
        LAYER_TAP, KC.KP1_8, KC.KP_9
    ],
    # Function Layer
    [
        KC.AUDIO_VOL_DOWN, KC.NO, KC.AUDIO_VOL_UP,
        KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
        KC.NO, KC.NO, KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
