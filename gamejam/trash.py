#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element, Hitbox


class Trash(Element):
    def __init__(self, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(6, 21, 18, 10))

        self.get_sprite("trash")

    def interact(self, item):
        return None
