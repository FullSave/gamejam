#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel


class Hitbox(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def x2(self):
        return self.x + self.w

    @property
    def y2(self):
        return self.y + self.h


class SpriteSheet(object):
    def __init__(self, image, path, w, h, mask=0):
        self._image = image
        self._w = w
        self._h = h
        self._mask = mask

    def render(self, x, y, mask=None):
        if mask is None:
            mask = self._mask

        return self._image, self._w * x, self._h * y, self._h, self._w, mask


class Element(object):
    def __init__(self, x, y, w, h, spritesheet, sx, sy):
        """Basic Game Element

        Arguments:
            * x, y, w, h: x, y, width, height
            * spritesheet: a SpriteSheet object
            * sx, sy: the coords, in multiple of w and h in the spritesheet
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.sx = sx
        self.sy = sy

        # The element hitbox
        self.hitbox = Hitbox(x, y, w, h)

        # Sprite sheet rendering
        self.spritesheet = spritesheet

    def draw(self):
        # Drawn the sprite at the element coords
        pyxel.blt(self.x, self.y, *self.spritesheet.render(self.sx, self.sy))

    def copy(self):
        # Return a copy of this element to predict movements
        return Element(
                self.x, self.y, self.w, self.h,
                self.spritesheet, self.sx, self.sy
        )

    def is_colliding(self, element):
        # Is this element colliding with element
        return self.hitbox.x < element.hitbox.x2 and \
               self.hitbox.x2 > element.hitbox.x and \
               self.hitbox.y < element.hitbox.y2 and \
               self.hitbox.y2 > element.hitbox.y
