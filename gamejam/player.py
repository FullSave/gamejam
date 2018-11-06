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
from .trash import Trash
from .rack import Rack


class Player(Element):
    # duration of 1 player animation frame (bases on fps)
    frame_duration = 5
    frames = 4

    def __init__(self, map_, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(7, 20, 17, 10))

        # Carried item
        self._item = None

        # The global map
        self._map = map_

        # Static diagonal smooth move
        self._diagonal_move = math.sqrt(2)

        # Current count of frame for animation calculation
        self._fps_count = 0
        self._current_frame = 0

        # Sprite loading
        self._direction = "bottom"
        self.update_sprite(direction="bottom")

    def update_sprite(self, direction):
        self._fps_count += 1

        # Direction change resets frame count
        if self._direction != direction:
            self._fps_count = 0
            self._current_frame = 0
        self._direction = direction

        # Add one more frame to the count, handling looping
        if self._fps_count > self.frame_duration:
            self._fps_count = 0
            self._current_frame += 1
        if self._current_frame >= self.frames:
            self._current_frame = 0

        # Update sprite
        self.get_sprite('player_%s%d' % (direction, self._current_frame))

    def draw(self, offset_x=0, offset_y=0):
        if self._direction == 'top':
            if self._item is not None:
                self._item.draw(self.x + 6, self.y + 18, offset_x, offset_y)
            Element.draw(self, offset_x, offset_y)
        else:
            Element.draw(self, offset_x, offset_y)
            if self._item is not None:
                self._item.draw(self.x + 6, self.y + 18, offset_x, offset_y)

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
                self.update_sprite(direction="top")
            elif dy > 0:
                self.update_sprite(direction="bottom")
            elif dx < 0:
                self.update_sprite(direction="left")
            elif dx > 0:
                self.update_sprite(direction="right")

    def interact(self):
        near_element = None

        sx = self.x + self.hitbox.w
        sy1 = self.y + self.hitbox.y
        sy2 = self.y + self.hitbox.y2

        # Elements the player must be above
        for element in self._map.providers + self._map.tables + self._map.trashs:
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
                # Already an item in hands, can't pick another one
                if self._item:
                    raise ValueError()

                self._item = near_element.interact()
            except ValueError:
                self._map.show_error_bubble()
        elif isinstance(near_element, (Table, Rack, Trash)):
            try:
                item = self._item
                self._item = near_element.interact(item)

                if isinstance(near_element, Rack):
                    self._map.scoreboard.validate_server(near_element, item)
            except ValueError:
                self._map.show_error_bubble()
