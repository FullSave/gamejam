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
        self.get_sprite("player")

        # Carried item
        self._item = None

        # The global map
        self._map = map_

    def move(self, dx, dy):
        new_self = self.copy()
        new_self.x = new_self.x + dx
        new_self.y = new_self.y + dy

        elements = self._map.providers + self._map.racks + \
            self._map.tables + self._map.walls
        for element in elements:
            if self.is_colliding(element):
                break
        else:
            self.x = new_self.x
            self.y = new_self.y
