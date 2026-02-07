#include QMK_KEYBOARD_H

enum layers {
    _BASE,
    _FN
};

enum custom_keycodes {
    OLED_TOGGLE = SAFE_RANGE
};

static uint8_t oled_mode __attribute__((unused)) = 0;     // 0 = animation, 1 = status
static bool oled_power __attribute__((unused)) = true;
static uint16_t encoder_btn_timer __attribute__((unused)) = 0;
static int volume_level __attribute__((unused)) = 50;


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
