#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element, Hitbox
from .server import Server


class Table(Element):
    def __init__(self, x, y):
        Element.__init__(self, x, y, 32, 32, Hitbox(0, 8, 32, 24))

        self.get_sprite("table")

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
