#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Item


class RAM(Item):
    def __init__(self):
        self.get_sprite("ram")


class CPU(Item):
    def __init__(self):
        self.get_sprite("cpu")


class Server(Item):
    def __init__(self, ram=0, cpu=0):
        self._get_sprite("server")

        self._ram = ram
        self._cpu = cpu

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
