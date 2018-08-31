#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element
from .server import Server


class Table(Element):
    def __init__(self, x, y, w, h, spritesheet, sx, sy):
        Element.__init_(self, x, y, w, h, spritesheet, sx, sy)

        self._server = None

    def interact(self, item):
        """ Interaction with the table

        Arguments:
            item : an item

        If the table has a server on it, the item is interacted with it
        """
        if isinstance(item, Server):
            if self._server is not None:
                raise ValueError

            self._server = item

        elif item is not None:
            self._server.interact(item)

        else:
            server = self._server
            self._server = None
            return server
