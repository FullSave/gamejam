#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
from .misc import Element, Hitbox
from .server import Server


class Rack(Element):
    def __init__(self, x, y, w, h, number):
        Element.__init__(self, x, y, w, h, Hitbox(0, 25, w-1, 16))
        # XXX self.get_sprite("rack0")
        self.number = number

        self._size = 4
        self._servers = []

    @property
    def is_full(self):
        return len(self._servers) >= self._size

    def draw(self, offset_x=0, offset_y=0):
        # Draw servers in racks
        x = self.x + offset_x
        y = self.y + offset_y + 1

        # Server draw
        i = 0
        for server in self._servers:
            server.draw(self.x + 2, self.y + 17 + i * 6, offset_x, offset_y)
            i = i + 1

    def interact(self, item):
        if isinstance(item, Server):
            if not self.is_full:
                self._servers.append(item)
                return None
        raise ValueError()
