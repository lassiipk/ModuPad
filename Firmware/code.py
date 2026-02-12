print("Launching ModuPad, a custom macro pad built on KMK firmware for the - " \
" Seeed XIAO RP2040 microcontroller. Developed by M. Saim Ghazanfar.")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay
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

#Macro setup, you can define your macros here and then call them in the keymap. You can also define them directly in the keymap, but this way you can reuse them and keep the keymap cleaner.
macros = Macros()
KC.MACRO(
    on_press=None, 
    on_hold=None,
    on_release=None,
    blocking=True,
)
keyboard.extensions.append(macros)
OPEN_Youtube = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI),
    Delay(500), # Delay in milliseconds to allow the Run dialog to open, 500ms is equal to 0.5 seconds
    Tap(KC.W), # You can also use Tap(KC.HOME) or any other keycode to open a specific application or folder, but using the Run dialog is more versatile and works on all Windows versions.
    Tap(KC.ENTER)
)

Alt_Tab = KC.MACRO(
    Press(KC.LALT),
    Delay(30),
    Tap(KC.TAB),
    Delay(30),
    Release(KC.LALT),
)

keyboard.keymap = [
    [OPEN_Youtube, Alt_Tab, KC.N3, KC.N0,
    KC.N4, KC.N5, KC.N6, KC.NO,
    KC.N7, KC.N8, KC.N9, KC.NO],
]

#------------------------------------------------------------------------------------

encoder_handler = EncoderHandler()

# ==============================
# Encoder
# ==============================

# Regular GPIO Encoder Pins assigned as D-Pins, with no button and 2 steps per detent. 

encoder_handler.pins = ( (board.D6, board.D7, None, False, 2), ) 
keyboard.modules.append(encoder_handler)

# You can optionally predefine combo keys as for your layout, but you can also just use the encoder as a regular encoder and it will send the keycodes in the order defined in the map.

keyboard.extensions.append(MediaKeys())

# You can also use the encoder as a rotary switch by changing KC's To other Keycode, for exaample KC.A n B, and it will send the keycode on each step, Just like With Keyswitches.
encoder_handler.map = [ ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),), # Standard
                        #((KC.VOLD, KC.VOLU, KC.NO),), # Extra
                        #((KC.A, KC.Z, KC.N1),), # NumPad not yet properly configured
                        #((KC.A, KC.Z, KC.N1),), # Gaming not yet properly configured

                        ]                      

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

        #TextEntry(text="Bilal ♥"#, x=0, y=0,#inverted=True, layer=0
        #   ),
        #TextEntry(text="Is't it Cool???? Huh?", x=0, y=16,#inverted=True, layer=0
        #          ),
        ImageEntry(image="3.bmp"#, x=0, y=0
                   ),    
        #ImageEntry(image="4.bmp", x=0, y=0),    

        ],

    width=128,
    height=32,
    flip = True, # flips your display content
    #flip_left = False, # flips your display content on left side split
    #flip_right = True, # flips your display content on right side split
    #brightness=0.8, # initial screen brightness level
    #brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=15, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=30, # time in seconds to turn off screen
    #powersave_dim_time=10, # time in seconds to reduce screen brightness
    #powersave_dim_target=0.1, # set level for brightness decrease
    #powersave_off_time=30, # time in seconds to turn off screen

)

keyboard.extensions.append(display)

#------------------------------------------------------------------------------------

if __name__ == '__main__':
    keyboard.go()
