#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel


class SpriteSheet(object):
    def __init__(self, image, path, w, h, mask=0):
        self._image = image
        self._w = w
        self._h = h
        self._mask = mask

    def render(self, x, y, mask=None):
        if mask is None:
            mask = self._mask

        return [self._image, self._w * x, self._h * y, self._h, self._w, mask]


class Element(object):
    def __init__(self, x, y, w, h, spritesheet, sx, sy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.spritesheet = spritesheet
        self.sprite = spritesheet.render(sx, sy)

    def draw(self):
        pyxel.blt(self.x, self.y, *self.sprite)
