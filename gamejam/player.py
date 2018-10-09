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
        Element.__init__(self, x, y, 32, 32, Hitbox(8, 16, 16, 13))

        # Sprite loading
        self._directions = {
            "top": "chicken_back",
            "bottom": "chicken_front",
            "left": "chicken_left",
            "right": "chicken_right"
        }
        self.set_direction("bottom")

        # Carried item
        self._item = None

        # The global map
        self._map = map_

        # Static diagonal smooth move
        self._diagonal_move = math.sqrt(2)

    def set_direction(self, direction):
        self._direction = direction
        self.get_sprite(self._directions[direction])

    def draw(self, offset_x=0, offset_y=0):
        if self._direction == 'top':
            if self._item is not None:
                self._item.draw(self.x + 8, self.y + 13, offset_x, offset_y)
            Element.draw(self, offset_x, offset_y)
        else:
            Element.draw(self, offset_x, offset_y)
            if self._item is not None:
                self._item.draw(self.x + 8, self.y + 13, offset_x, offset_y)

    def move(self, dx, dy):
        # Diagonal smooth move
        if dx != 0 and dy != 0:
            # Only move on direction, to allow "slipping" against obstacles
            self.move(dx / self._diagonal_move, 0)
            self.move(0, dy / self._diagonal_move)
            return

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

            if dy < 0:
                self.set_direction("top")
            elif dy > 0:
                self.set_direction("bottom")
            elif dx < 0:
                self.set_direction("left")
            elif dx > 0:
                self.set_direction("right")

    def interact(self):
        near_element = None

        sx = self.x + self.hitbox.w
        sy1 = self.y + self.hitbox.y
        sy2 = self.y + self.hitbox.y2

        # Elements the player must be above
        for element in self._map.providers + self._map.tables:
            ex1 = element.x + element.hitbox.x
            ex2 = element.x + element.hitbox.x2
            ey1 = element.y + element.hitbox.y
            ey2 = element.y + element.hitbox.y2

            if sx >= ex1 and sx <= ex2 and sy2 <= ey1 and sy2 >= ey1 - 8:
                near_element = element
                break

        if near_element is None:
            # Elements the player must be below
            for element in self._map.racks:
                ex1 = element.x + element.hitbox.x
                ex2 = element.x + element.hitbox.x2
                ey1 = element.y + element.hitbox.y
                ey2 = element.y + element.hitbox.y2
                if sx >= ex1 and sx <= ex2 and sy1 >= ey2 and sy1 <= ey2 + 8:
                    near_element = element
                    break

        if issubclass(near_element.__class__, Provider):
            try:
                self._item = near_element.interact()
            except ValueError:
                print("Invalid item in hands")
        elif isinstance(near_element, Table) or isinstance(near_element, Rack):
            try:
                self._item = near_element.interact(self._item)
            except ValueError:
                print("Invalid item in hands")
