# ==============================
# ModuPad - KMK Firmware (Corrected)
# MCU: Seeed XIAO RP2040
# Matrix: 3 Rows x 4 Columns (9 Keys + Encoder Button)
# Author: M. Saim Ghazanfar
# ==============================

import board
import os
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import OLED, SSD1306

# ==============================
# Keyboard Init
# ==============================
keyboard = KMKKeyboard()

# ==============================
# Matrix Configuration
# Columns: GP26, GP27, GP28, GP29
# Rows:    GP2, GP4, GP3
# Diodes:  Column -> Row
# Encoder button is located at R0C3
# ==============================

keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
)

keyboard.row_pins = (
    board.GP2,
    board.GP4,
    board.GP3,
)

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# ==============================
# Layers
# ==============================
layers = Layers()
keyboard.modules.append(layers)

FN = KC.MO(1)

# ==============================
# Encoder Configuration
# Encoder A -> GP0
# Encoder B -> GP1
# Encoder push button is part of matrix (R0C3)
# ==============================

encoder = EncoderHandler()
encoder.pins = ((board.GP0, board.GP1, None),)
keyboard.modules.append(encoder)

encoder.map = (
    (
        KC.VOLD,
        KC.VOLU,
        KC.NO,
    ),
)

# ==============================
# OLED Setup (I2C GP6 SDA / GP7 SCL)
# ==============================

oled = OLED(
    SSD1306,
    width=128,
    height=32,
    rotation=0,
)
keyboard.extensions.append(oled)

# OLED state
oled_mode = 0              # 0 = animation, 1 = text, 2 = status
oled_enabled = True
animation_index = 0
encoder_press_time = 0
encoder_held = False

ANIMATION_PATH = "/OLED_ANIMATIONS"

# ==============================
# OLED Drawing Functions
# ==============================

def get_animation_files():
    try:
        return sorted([
            f for f in os.listdir(ANIMATION_PATH)
            if f.endswith(".py")
        ])
    except OSError:
        return []


def draw_boot_screen():
    oled.clear()
    oled.text("ModuPad", 0, 0)
    oled.text("M. Saim", 0, 16)
    oled.show()


def draw_text_mode():
    oled.clear()
    oled.text("Creator:", 0, 0)
    oled.text("M. Saim", 0, 16)
    oled.show()


def draw_status_mode():
    oled.clear()
    oled.text("Status:", 0, 0)
    oled.text("Ready", 0, 16)
    oled.show()


def oled_off():
    oled.clear()
    oled.show()


def play_animation():
    global animation_index

    files = get_animation_files()
    if not files:
        oled.clear()
        oled.text("No Anim", 0, 0)
        oled.show()
        return

    animation_index %= len(files)

    try:
        exec(open(f"{ANIMATION_PATH}/{files[animation_index]}").read())
    except Exception:
        oled.clear()
        oled.text("Anim Error", 0, 0)
        oled.show()

# ==============================
# Encoder Button Logic
# Implemented via matrix key (R0C3)
# ==============================

ENCODER_BTN = KC.F19


def encoder_button_handler(key, keyboard, *args):
    global oled_mode, oled_enabled, animation_index
    global encoder_press_time, encoder_held

    now = time.monotonic()

    # Key pressed
    if key.pressed:
        encoder_press_time = now
        encoder_held = False
        return

    # Key released
    hold_time = now - encoder_press_time

    # FN + Hold (>=3s) → OLED toggle
    if keyboard.active_layers[0] == 1 and hold_time >= 3:
        oled_enabled = not oled_enabled
        if not oled_enabled:
            oled_off()
        else:
            draw_boot_screen()
        return

    # FN + Press → cycle text/status
    if keyboard.active_layers[0] == 1:
        oled_mode = (oled_mode + 1) % 3

        if oled_mode == 0:
            play_animation()
        elif oled_mode == 1:
            draw_text_mode()
        else:
            draw_status_mode()
        return

    # Normal press → next animation
    if oled_enabled and oled_mode == 0:
        animation_index += 1
        play_animation()


# ==============================
# Keymap
# Matrix order:
# Row0: C0 C1 C2 C3 (Encoder button here)
# Row1: C0 C1 C2 C3
# Row2: C0 C1 C2 C3
# ==============================

keyboard.keymap = [

    # ===== Layer 0 =====
    [
        FN,                                KC.PSCR,                       KC.LCTL(KC.LSFT(KC.Z)), ENCODER_BTN,
        KC.LCTL(KC.C),                     KC.LCTL(KC.V),                 KC.LCTL(KC.Z),          KC.NO,
        KC.APP1,                           KC.WWW_HOME,                   KC.EXPLORER,            KC.NO,
    ],

    # ===== Layer 1 (FN Held) =====
    [
        KC.NO,                             KC.MUTE,                       KC.LALT(KC.TAB),        ENCODER_BTN,
        KC.LCTL(KC.LSFT(KC.ESC)),          KC.MUTE,                       KC.NO,                  KC.NO,
        KC.SYSTEM_SLEEP,                   KC.SYSTEM_RESTART,             KC.SYSTEM_POWER,        KC.NO,
    ],
]

# Bind encoder button handler
keyboard.add_key_handler(ENCODER_BTN, encoder_button_handler)

# ==============================
# Startup
# ==============================

draw_boot_screen()

if __name__ == '__main__':
    keyboard.go()
