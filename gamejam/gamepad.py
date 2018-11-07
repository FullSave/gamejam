#!/usr/bin/env python3

import threading
import inputs

# FIXME Should be in a config file
CONFIG = {
    "usb gamepad": {
        "axis": {
            "ABS_X": (0, 255),
            "ABS_Y": (0, 255)
        },
        "mapping": {
            'Absolute-ABS_X': 'X',
            'Absolute-ABS_Y': 'Y',
            'Key-BTN_TRIGGER': 'N',
            'Key-BTN_THUMB': 'E',
            'Key-BTN_THUMB2': 'S',
            'Key-BTN_TOP': 'W',
            'Key-BTN_BASE4': 'ST',
        }
    },
    "Logitech Gamepad F310": {
        "axis": {
            "ABS_X": (-32768, 32768),
            "ABS_Y": (-32768, 32768),
            "ABS_HAT0X": (-1, 1),
            "ABS_HAT0Y": (-1, 1),
        },
        "mapping": {
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
    }
}

# The dead zone for an axis is 10%
AXIS_DEAD_ZONE = 0.1
AXIS_RANGE = 65536


class Controller(threading.Thread):
    def __init__(self, gamepad_id=0):
        # Gamepad initialization
        # If none is plugged, the worker thread is not started
        try:
            self.gamepad = inputs.devices.gamepads[gamepad_id]
            self._thread = threading.Thread(target=self._worker)
            self._thread.setDaemon(True)
            self._thread.start()
            self._name = str(self.gamepad)
        except IndexError:
            pass

        self._prev_states = {}
        self._current_states = {}

    def _format_axis_value(self, axis, value):
        try:
            config = CONFIG[self._name]["axis"][axis]
        except KeyError:
            return value

        # Recenter the value around 0
        decalage = (config[0] + config[1]) / 2
        value = value - decalage

        # Normalize the value
        range = abs(config[0]) + abs(config[1])
        value = value * AXIS_RANGE / range

        # Dead zone
        if abs(value) < abs(AXIS_RANGE / 2) * AXIS_DEAD_ZONE:
            value = 0

        return value

    def _map_key(self, key):
        try:
            return CONFIG[self._name]["mapping"][key]
        except KeyError:
            return False

    def _get_prev_state(self, key):
        try:
            return self._prev_states[key]
        except KeyError:
            return 0

    def _get_current_state(self, key):
        try:
            return self._current_states[key]
        except KeyError:
            return 0

    def _worker(self):
        while True:
            events = inputs.get_gamepad()
            for event in events:
                if event.ev_type == 'Sync':
                    continue
                if event.ev_type == 'Misc':
                    continue

                key = self._map_key(event.ev_type + '-' + event.code)

                # If the pressed key is not in the mapping, ignore it
                if not key:
                    continue

                self._current_states[key] = self._format_axis_value(event.code, event.state)

    def is_pressed(self, button):
        ret = not self._get_prev_state(button) and self._get_current_state(button)
        self._prev_states = self._current_states.copy()
        return ret

    def get_axis(self, axis):
        try:
            return self._current_states[axis]
        except KeyError:
            return 0
