#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
from .misc import Element, Hitbox
from .server import Server


class Table(Element):
    def __init__(self, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(0, 7, 32, 16))

        self.get_sprite("table")

        self._server = None

    def draw(self, offset_x=0, offset_y=0):
        # TODO Draw the server at the right position
        if self._server is not None:
            self._server.draw(self.x + 8, self.y + 3, offset_x, offset_y)

    def interact(self, item):
        """ Interaction with the table

        Arguments:
            item : an item

        If the table has a server on it, the item is interacted with it
        """
        # Put a server  on the table
        if isinstance(item, Server):
            if self._server is not None:
                raise ValueError

            self._server = item
            return None

        # Interact the item with the server
        elif item is not None and self._server:
            self._server.interact(item)
            return None

        # Hands free, get the server from the table
        elif not item:
            server = self._server
            self._server = None
            return server

        # Nothing to do with what your tried to give me
        # FIXME: to decide: lose the item in case of error ?
        return item
