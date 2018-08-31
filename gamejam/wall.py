#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel

from misc import Element


class Wall(Element):
    def __init__(self, x, y, w, h):
        # FIXME: disable sprite
        Element.__init__(self, x, y, w, h, None, None, None)

    def draw(self):
        # FIXME: draw a rectangle instead of an image
        pyxel.rect(self.x, self.y, self.x+self.w, self.y+self.h, 4)
