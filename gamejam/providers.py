#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element
from .server import RAM, CPU, Case


class Provider(Element):
    item_class = None

    # FIXME depends on the spritesheet
    sx = 0
    sy = 0

    def __init__(self, x, y, w, h, spritesheet):
        Element.__init_(self, x, y, w, h, spritesheet)

    def interact(self):
        if self.item_class is None:
            raise RuntimeError("Provider class must be inherited")

        else:
            return self.item_class(self.spritesheet)


class RAMProvider(Element):
    item_class = RAM

    # FIXME depends on the spritesheet
    sx = 0
    sy = 0


class CPUProvider(Element):
    item_class = CPU

    # FIXME depends on the spritesheet
    sx = 0
    sy = 0


class CaseProvider(Element):
    item_class = Case

    # FIXME depends on the spritesheet
    sx = 0
    sy = 0
