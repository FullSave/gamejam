#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element, Hitbox


class Trash(Element):
    def __init__(self, x, y):
        Element.__init__(self, x, y, 17, 20, Hitbox(0, 10, 17, 10))

    def draw(self, offset_x=0, offset_y=0):
        pass

    def interact(self, item):
        return None
