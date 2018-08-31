#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element


class Player(Element):
    def __init__(self, map_, x, y, w, h):
        Element.__init__(self, x, y, w, h)

        # Sprite loading
        self.get_sprite("player_left0")

        # Carried item
        self._item = None

        # The global map
        self._map = map_

    def move(self, dx, dy):
        new_self = self.copy()
        new_self.x = new_self.x + dx
        new_self.y = new_self.y + dy

        for element in self._map.elements:
            if self.is_colliding(element):
                break
        else:
            self.x = new_self.x
            self.y = new_self.y
