#!/usr/bin/env python3

import gamepad


class Controller(gamepad.Gamepad):
    # pip install gamepad
    def __init__(self):
        gamepad.Gamepad.__init__(self)

        self._prev_states = {
            'a': False,
            'b': False,
            'x': False,
            'y': False,
            'tl': False,
            'tr': False,
            'select': False,
            'start': False,
            'mode': False,
            'thumbl': False,
            'thumbr': False
        }

    def is_pressed(self, button):
        try:
            ret = not self._prev_states[button] and self._button_states[button]
        except KeyError:
            ret = False

        self._prev_states = self._button_states.copy()
        return ret

    def get_axis(self, axis):
        try:
            return self._axis_states[axis]
        except KeyError:
            return 0
