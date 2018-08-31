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
    def __init__(self, image, w, h, mask=0):
        """ SpriteSheet object

        Arguments:
            image: a pyxel image number (0, 1 or 2)
            w, h: the sprites size
            mask: the transparent color
        """
        self._image = image
        self.w = w
        self.h = h
        self._mask = mask

    def render(self, x, y, mask=None):
        if mask is None:
            mask = self._mask

        return self._image, self._w * x, self._h * y, self._h, self._w, mask


class Item(object):
    sx = 0
    sy = 0

    def __init__(self, spritesheet, sx=None, sy=None):
        """Basic Game Element

        Arguments:
            * x, y, w, h: x, y, width, height
            * spritesheet: a SpriteSheet object
            * sx, sy: the coords, in multiple of w and h in the spritesheet
        """
        # Sprite sheet rendering
        self.spritesheet = spritesheet
        if sx is not None:
            self.sx = sx
        if sy is not None:
            self.sy = sy

    def copy(self):
        # Return a copy of this element to predict movements
        return Item(self.spritesheet, self.sx, self.sy)

    def draw(self, x, y):
        # Drawn the sprite at the element coords
        pyxel.blt(x, y, *self.spritesheet.render(self.sx, self.sy))


class Element(Item):
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

        # The element hitbox
        self.hitbox = Hitbox(x, y, w, h)

        # Sprite sheet rendering
        Item(spritesheet, sx, sy)

    def draw(self):
        Item.draw(self, self.x, self.y)

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
