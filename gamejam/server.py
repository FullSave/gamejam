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
        self.get_sprite("ram")


class CPU(Item):
    def __init__(self):
        self.get_sprite("cpu")


class Server(Item):
    def __init__(self, ram=0, cpu=0):
        self.get_sprite("server")

        self._ram = ram
        self._cpu = cpu

    @property
    def is_racked(self):
        return False  # FIXME

    @property
    def cpu(self):
        return self._cpu

    @property
    def ram(self):
        return self._ram

    def compare(self, other):
        erros = 0
        if self._ram != other._ram:
            errors += 1
        if self._cpu == other._cpu:
            errors += 1
        return errors

    def draw(self, x, y, offset_x=0, offset_y=0):
        Item.draw(self, x, y, offset_x, offset_y)
        if self.is_racked:
            pyxel.pix(x + offset_x + 1, y + offset_y + 7, 11)
        if self._cpu >= 1:
            pyxel.line(x + offset_x + 5, y + offset_y + 7,
                       x + offset_x + 5, y + offset_y + 8, 13)
        if self._cpu >= 2:
            pyxel.line(x + offset_x + 7, y + offset_y + 7,
                       x + offset_x + 7, y + offset_y + 8, 13)
        if self._ram >= 1:
            pyxel.line(x + offset_x + 11, y + offset_y + 7,
                       x + offset_x + 11, y + offset_y + 8, 3)
        if self._ram >= 2:
            pyxel.line(x + offset_x + 13, y + offset_y + 7,
                       x + offset_x + 13, y + offset_y + 8, 3)

    def interact(self, Item):
        """ Interaction with the server

        Arguments:
            Item: an Item instance (CPU or RAM)
        """
        if isinstance(Item, RAM):
            self._ram = self._ram + 1
        elif isinstance(Item, CPU):
            self._cpu = self._cpu + 1
        else:
            raise ValueError
