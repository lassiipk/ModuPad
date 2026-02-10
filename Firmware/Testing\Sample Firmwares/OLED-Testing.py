print("Launching ModuPad, a custom macro pad built on KMK firmware for the - " \
" Seeed XIAO RP2040 microcontroller. Developed by M. Saim Ghazanfar.")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.display import Display, TextEntry, ImageEntry

keyboard = KMKKeyboard()

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
        TextEntry(text="Is't it Cool? Huh?", x=0, y=16),# inverted=True, layer=0),
        #ImageEntry(image="/1.bmp", x=0, y=0, layer=0),
    ],

    width=128,
    height=32,
    dim_time=30, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen

)

keyboard.extensions.append(display)

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()
