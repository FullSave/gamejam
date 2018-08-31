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
        Element.__init__(self, x, y, w, h, Hitbox(7, 3, 18, 26))
        self.get_sprite("rack0")
        self.number = number

        self._size = 4
        self._servers = []

    @property
    def is_full(self):
        # FIXME: is full when servers < size + requests
        return len(self._servers) >= self._size

    def draw(self, offset_x=0, offset_y=0):
        Element.draw(self, offset_x, offset_y)
        x = self.x + offset_x
        y = self.y + offset_y + 1
        pyxel.rect(x, y, x + 6, y + 6, 10)
        pyxel.text(x+2, y+1, self.number, 0)

    def interact(self, item):
        if isinstance(item, Server):
            if not self.is_full:
                self._servers.append(item)
                return None
        else:
            raise ValueError()
