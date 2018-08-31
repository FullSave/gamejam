#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Item


class RAM(Item):
    # FIXME depends on the spritesheet
    sx = 0
    sy = 0


class CPU(Item):
    # FIXME depends on the spritesheet
    sx = 0
    sy = 0


class Server(Item):
    # FIXME depends on the spritesheet
    sx = 0
    sy = 0

    def __init__(self, spritesheet):
        Item.__init__(self, spritesheet, self.sx, self.sy)

        self._ram = 0
        self._cpu = 0

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
