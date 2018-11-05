#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
from .misc import Element, Hitbox
from .server import RAM, CPU, Server


class Provider(Element):
    item_class = None

    def __init__(self, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(0, 7, 32, 16))

    def interact(self):
        if self.item_class is None:
            raise RuntimeError("Provider class must be inherited")

        else:
            return self.item_class()

    def draw(self, offset_x, offset_y):
        pass


class RAMProvider(Provider):
    item_class = RAM

    def __init__(self, x, y):
        Provider.__init__(self, x, y)

        self.get_sprite("provider_ram")


class CPUProvider(Provider):
    item_class = CPU

    def __init__(self, x, y):
        Provider.__init__(self, x, y)

        self.get_sprite("provider_cpu")


class CaseProvider(Provider):
    item_class = Server

    def __init__(self, x, y):
        Provider.__init__(self, x, y)

        self.get_sprite("provider_case")
