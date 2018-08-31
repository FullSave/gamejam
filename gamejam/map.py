#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from wall import Wall


class Map(object):
    def __init__(self):
        self.reset()

    def reset(self):
        """ Static map re-generation.
        """
        self._walls = []
        self._racks = []
        self._providers = []
        self._tables = []

        # self._player = None

    def update(self):
        pass

    def draw(self):
        entities = self._walls + self._racks + self._providers + self._tables
        for entity in entities:
            entity.draw()

        # self._player.draw()
