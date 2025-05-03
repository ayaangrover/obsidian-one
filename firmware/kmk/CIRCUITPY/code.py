from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
keyboard.row_pins = (16, 17, 18, 19, 20, 21)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Row 0: Escape + Mac media keys (F1–F12, Mute, Vol Up/Down)
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.MUTE, KC.VOLU, KC.VOLD],

    # Row 1: `~, numbers, Delete, Home
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.DEL, KC.HOME, KC.NO, KC.NO, KC.NO],

    # Row 2: QWERTY top row
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.NO, KC.NO],

    # Row 3: Home row
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.NO, KC.NO],

    # Row 4: Bottom row letters + arrow up
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.NO, KC.NO, KC.NO],

    # Row 5: Modifiers + spacebar + arrows
    [KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
]

if __name__ == '__main__':
    keyboard.go()