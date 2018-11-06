#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
from .misc import Item


class RAM(Item):
    def __init__(self):
        self.get_sprite("item_ram")


class CPU(Item):
    def __init__(self):
        self.get_sprite("item_cpu")


class Server(Item):
    def __init__(self, ram=0, cpu=0):
        self.get_sprite("server_%s_%s" % (cpu, ram))

        self._ram = int(ram)
        self._cpu = int(cpu)

    @property
    def is_racked(self):
        return False  # FIXME

    @property
    def cpu(self):
        return self._cpu

    @property
    def ram(self):
        return self._ram

    @property
    def value(self):
        return 50 + self._ram * 25 + self._cpu * 25

    def compare(self, other):
        errors = 0
        if self._ram != other._ram:
            errors += 1
        if self._cpu != other._cpu:
            errors += 1
        return errors

    def draw(self, x, y, offset_x=0, offset_y=0):
        self.get_sprite("server_%s_%s" % (self._cpu, self._ram))
        Item.draw(self, x, y, offset_x, offset_y)

    def interact(self, Item):
        """ Interaction with the server

        Arguments:
            Item: an Item instance (CPU or RAM)
        """
        if isinstance(Item, RAM) and self._ram < 2:
            self._ram = self._ram + 1
        elif isinstance(Item, CPU) and self._cpu < 2:
            self._cpu = self._cpu + 1
        else:
            raise ValueError
