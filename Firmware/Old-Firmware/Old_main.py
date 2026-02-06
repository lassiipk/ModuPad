# ==============================
# ModuPad - KMK Firmware
# MCU: Seeed XIAO RP2040
# Author: M. Saim Ghazanfar
# ==============================

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.extensions.oled import OLED, SSD1306
import os
import time

keyboard = KMKKeyboard()

# ==============================
# Matrix configuration
# ==============================
keyboard.col_pins = (0, 1, 2)
keyboard.row_pins = (9, 10, 11)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# ==============================
# Layers
# ==============================
layers = Layers()
keyboard.modules.append(layers)

FN = KC.MO(1)

# ==============================
# Encoder
# ==============================
encoder = EncoderHandler()
encoder.pins = ((7, 8, 4),)  # (A, B, Button)
keyboard.modules.append(encoder)

encoder.map = (
    (
        KC.VOLD,   # CCW
        KC.VOLU,   # CW
        KC.NO      # handled manually for OLED
    ),
)

# ==============================
# OLED Setup
# ==============================
oled = OLED(
    SSD1306,
    width=128,
    height=32,
    rotation=0,
)
keyboard.extensions.append(oled)

oled_mode = 0        # 0 = animation, 1 = text, 2 = status
oled_enabled = True
animation_index = 0
last_encoder_press = 0

ANIMATION_PATH = "/OLED_ANIMATIONS"

def get_animation_files():
    try:
        return sorted([
            f for f in os.listdir(ANIMATION_PATH)
            if f.endswith(".py")
        ])
    except:
        return []

def draw_boot_screen():
    oled.clear()
    oled.text("ModuPad", 0, 0)
    oled.text("M. Saim Ghazanfar", 0, 16)
    oled.show()

def draw_text_mode():
    oled.clear()
    oled.text("Creator:", 0, 0)
    oled.text("M. Saim Ghazanfar", 0, 16)
    oled.show()

def draw_status_mode():
    oled.clear()
    oled.text("Status:", 0, 0)
    oled.text("Mic / Volume OK", 0, 16)
    oled.show()

def play_animation():
    files = get_animation_files()
    if not files:
        oled.clear()
        oled.text("No Animations", 0, 0)
        oled.show()
        return

    global animation_index
    animation_index %= len(files)

    try:
        exec(open(f"{ANIMATION_PATH}/{files[animation_index]}").read())
    except:
        oled.clear()
        oled.text("Anim Error", 0, 0)
        oled.show()

# ==============================
# Encoder Button Logic
# ==============================
def encoder_button_handler():
    global oled_mode, oled_enabled, animation_index, last_encoder_press

    now = time.monotonic()

    # FN + Hold (3s) → OLED OFF
    if keyboard.active_layers[0] == 1:
        if now - last_encoder_press > 3:
            oled.clear()
            oled.show()
            oled_enabled = False
            return

    # Normal press → next animation
    if oled_mode == 0 and oled_enabled:
        animation_index += 1
        play_animation()

    # FN + press → cycle text/status
    if keyboard.active_layers[0] == 1 and oled_enabled:
        oled_mode = (oled_mode + 1) % 3
        if oled_mode == 1:
            draw_text_mode()
        elif oled_mode == 2:
            draw_status_mode()

    last_encoder_press = now

encoder.button_callback = encoder_button_handler

# ==============================
# Keymap
# ==============================
keyboard.keymap = [
    # ===== Layer 0 =====
    [
        FN,                KC.PSCR,           KC.LCTL(KC.LSFT(KC.Z)),
        KC.LCTL(KC.C),     KC.LCTL(KC.V),      KC.LCTL(KC.Z),
        KC.APP,            KC.WWW_HOME,        KC.EXPLORER,
    ],

    # ===== Layer 1 (FN) =====
    [
        KC.MUTE,           KC.LALT(KC.TAB),    KC.LCTL(KC.LSFT(KC.ESC)),
        KC.F13,            KC.F14,             KC.F15,
        KC.F16,            KC.F17,             KC.F18,
    ],
]

# ==============================
# Startup
# ==============================
draw_boot_screen()

if __name__ == '__main__':
    keyboard.go()
