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

    def __init__(self, x, y, number):
        Element.__init__(self, x, y, 32, 32, Hitbox(0, 7, 32, 16))

        self.get_sprite("table_%s" % number)

    def interact(self):
        if self.item_class is None:
            raise RuntimeError("Provider class must be inherited")

        else:
            return self.item_class()


class RAMProvider(Provider):
    item_class = RAM


class CPUProvider(Provider):
    item_class = CPU


class CaseProvider(Provider):
    item_class = Server
