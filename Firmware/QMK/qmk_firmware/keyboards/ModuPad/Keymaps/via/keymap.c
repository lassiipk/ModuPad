#include QMK_KEYBOARD_H

enum layers {
_BASE,
_FN
};

enum custom_keycodes {
OLED_TOGGLE = SAFE_RANGE
};

static uint8_t oled_mode = 0;     // 0 = animation, 1 = status
static bool oled_power = true;
static uint16_t encoder_btn_timer = 0;
static int volume_level = 50;

// 3x4 matrix
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
[_BASE] = LAYOUT(
MO(_FN), KC_NO, KC_NO, KC_NO,
KC_NO, KC_NO, KC_NO, KC_NO,
KC_NO, KC_NO, KC_NO, KC_NO
),
[_FN] = LAYOUT(
_______, KC_NO, KC_NO, KC_NO,
KC_NO, KC_NO, KC_NO, KC_NO,
KC_NO, KC_NO, KC_NO, KC_NO
)
};

// Encoder rotation → Volume
bool encoder_update_user(uint8_t index, bool clockwise) {
if (clockwise) {
tap_code(KC_VOLU);
if (volume_level < 100) volume_level++;
} else {
tap_code(KC_VOLD);
if (volume_level > 0) volume_level--;
}
return false;
}

// Encoder button logic (ROW0 COL3)
bool process_record_user(uint16_t keycode, keyrecord_t *record) {

```
if (record->event.key.row == 0 && record->event.key.col == 3) {

    if (record->event.pressed) {
        encoder_btn_timer = timer_read();
    } else {
        uint16_t held = timer_elapsed(encoder_btn_timer);

        if (layer_state_is(_FN)) {
            if (held > 3000) {
                oled_power = !oled_power;
                if (oled_power) oled_on();
                else oled_off();
            } else {
                oled_mode = !oled_mode;
            }
        } else {
            oled_mode = !oled_mode;
        }
    }
    return false;
}

return true;
```

}

// OLED Rendering
#ifdef OLED_ENABLE

bool oled_task_user(void) {

```
if (!oled_power) return false;

oled_clear();

if (oled_mode == 0) {
    oled_write_ln(PSTR("XIAO MACROPAD"), false);
    oled_write_ln(PSTR("Animation Mode"), false);
} else {
    oled_write_ln(PSTR("Status Mode"), false);

    oled_write_P(PSTR("Layer: "), false);
    oled_write_ln(layer_state_is(_FN) ? PSTR("FN") : PSTR("BASE"), false);

    oled_write_P(PSTR("Vol: "), false);
    oled_write(get_u8_str(volume_level, ' '), false);
    oled_write_ln(PSTR("%"), false);

    if (host_keyboard_led_state().caps_lock) {
        oled_write_ln(PSTR("CAPS: ON"), false);
    } else {
        oled_write_ln(PSTR("CAPS: OFF"), false);
    }

    oled_write_ln(PSTR("Author: You"), false);
}

return false;
```

}

#endif
