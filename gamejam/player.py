#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import math

from .misc import Element, Hitbox
from .providers import Provider
from .table import Table
from .rack import Rack


class Player(Element):
    def __init__(self, map_, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(8, 16, 16, 15))

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

        self.move_direction(smoothness_x * dx, 0)
        self.move_direction(0, smoothness_y * dy)

    def move_direction(self, dx, dy):
        # Only move on direction, to allow "slipping" against obstacles
        if dx != 0 and dy != 0:
            self.move_direction(dx, 0)
            self.move_direction(0, dy)

        new_self = self.copy()
        new_self.x += dx
        new_self.y += dy

        # Map limits
        if new_self.x + self.hitbox.x < 0:
            new_self.x = -self.hitbox.x
        elif new_self.x + self.hitbox.x2 > self._map.width:
            new_self.x = self._map.width - self.hitbox.x2

        if new_self.y + self.hitbox.y < 0:
            new_self.y = -self.hitbox.y
        if new_self.y + self.hitbox.y2 > self._map.height:
            new_self.y = self._map.height - self.hitbox.y2

        # Test collisions with all other elements
        for element in self._map.elements:
            if new_self.is_colliding(element):
                break
        else:
            self.x = new_self.x
            self.y = new_self.y

    def interact(self):
        near_element = None

        # Elements the player must be above
        for element in self._map.providers + self._map.tables:
            if self.hitbox.x > element.hitbox.x and \
                    self.hitbox.x2 < element.hitbox.x2 and \
                    self.hitbox.y2 < element.hitbox.y and \
                    self.hitbox.y2 > element.hitbox.y - 8:
                near_element = element
                break

        if near_element is None:
            # Elements the player must be below
            for element in self._map.racks:
                if self.hitbox.x > element.hitbox.x and \
                        self.hitbox.x2 < element.hitbox.x2 and \
                        self.hitbox.y > element.hitbox.y2 and \
                        self.hitbox.y < element.hitbox.y2 + 8:
                    near_element = element
                    break

        near_element = self._map.racks[0]

        if issubclass(near_element.__class__, Provider):
            try:
                near_element.interact()
            except ValueError:
                print("Invalid item in hands")
        elif isinstance(near_element, Table) or isinstance(near_element, Rack):
            try:
                near_element.interact(self._item)
            except ValueError:
                print("Invalid item in hands")
