#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element
from .server import RAM, CPU, Server


class Provider(Element):
    item_class = None

    def __init__(self, x, y, w, h):
        Element.__init_(self, x, y, w, h)

    def interact(self):
        if self.item_class is None:
            raise RuntimeError("Provider class must be inherited")

        else:
            return self.item_class(self.spritesheet)


class RAMProvider(Provider):
    item_class = RAM

    def __init__(self, x, y, w, h):
        Provider.__init_(self, x, y, w, h)

        self.get_sprite("provider_ram")


class CPUProvider(Provider):
    item_class = CPU

    def __init__(self, x, y, w, h):
        Provider.__init_(self, x, y, w, h)

        self.get_sprite("provider_cpu")


class CaseProvider(Provider):
    item_class = Server

    def __init__(self, x, y, w, h):
        Provider.__init_(self, x, y, w, h)

        self.get_sprite("provider_case")
