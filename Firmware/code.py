print("Launching ModuPad, a custom macro pad built on KMK firmware for the - " \
" Seeed XIAO RP2040 microcontroller. Developed by M. Saim Ghazanfar.")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
import busio

#-----------------------------------------------------------------------------------

keyboard = KMKKeyboard()

# ==============================
#Switch setup
# ==============================s

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.ENTER,
    KC.D, KC.E, KC.F, KC.NO,
    KC.G, KC.H, KC.LGUI, KC.NO],
]

#------------------------------------------------------------------------------------

# ==============================
# Encoder
# ==============================

#------------------------------------------------------------------------------------

# ==============================
#Display setup
# ==============================

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Driver FIRST
driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)

# Then Display

display = Display(
    display=driver,
    entries=[
        TextEntry(text="Saim's ModuPad", x=0, y=0),# inverted=True, layer=0),
        TextEntry(text="Is't it Cool???? Huh?", x=0, y=16),# inverted=True, layer=0),
        #ImageEntry(image="/1.bmp", x=0, y=0, layer=0),
    ],

    width=128,
    height=32,
    dim_time=15, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=30, # time in seconds to turn off screen

)

keyboard.extensions.append(display)

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()
