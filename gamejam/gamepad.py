#!/usr/bin/env python3

import threading
import inputs

# Map kernel event names to game keys
# https://www.kernel.org/doc/Documentation/input/gamepad.txt
EVENT_MAPPING = {
    'Absolute-ABS_HAT0X': 'X',
    'Absolute-ABS_HAT0Y': 'Y',
    'Absolute-ABS_X': 'X',
    'Absolute-ABS_Y': 'Y',
    'Key-BTN_NORTH': 'N',
    'Key-BTN_EAST': 'E',
    'Key-BTN_SOUTH': 'S',
    'Key-BTN_WEST': 'W',
    'Key-BTN_START': 'ST',
}

class Controller(threading.Thread):
    def __init__(self, gamepad_id=0):
        # Gamepad initialization
        # FIXME Can break if no gamepad is plugged
        self.gamepad = inputs.devices.gamepads[gamepad_id]

        self._prev_states = {}
        for name, value in EVENT_MAPPING.items():
            self._prev_states[value] = 0

        self._current_states = self._prev_states.copy()

        self._thread = threading.Thread(target=self._worker)
        self._thread.setDaemon(True)
        self._thread.start()

    def _worker(self):
        while True:
            self._prev_states = self._current_states.copy()
            events = inputs.get_gamepad()
            for event in events:
                if event.ev_type == 'Sync':
                    continue
                if event.ev_type == 'Misc':
                    continue

                key = event.ev_type + '-' + event.code
                self._current_states[EVENT_MAPPING[key]] = event.state

    def is_pressed(self, button):
        try:
            return not self._prev_states[button] and self._current_states[button]
        except KeyError:
            return 0

    def get_axis(self, axis):
        try:
            return self._current_states[axis]
        except KeyError:
            return 0
