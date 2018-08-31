#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import math

from .misc import Element, Hitbox


class Player(Element):
    def __init__(self, map_, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(10, 20, 12, 12))

        # Sprite loading
        self.get_sprite("player_left0")

        # Carried item
        self._item = None

        # The global map
        self._map = map_

        # Static diagonal smooth move
        self._diagonal_move = (math.cos(45), math.sin(45))

    def move(self, dx, dy):
        # Default one-way move
        smoothness_x = 1
        smoothness_y = 1

        # Diagonal smooth move
        if dx != 0 and dy != 0:
            smoothness_x, smoothness_y = self._diagonal_move

        # Test collisions with all other elements
        new_self = self.copy()
        new_self.x += smoothness_x * dx
        new_self.y += smoothness_y * dy

        for element in self._map.elements:
            if new_self.is_colliding(element):
                break
        else:
            self.x = new_self.x
            self.y = new_self.y
