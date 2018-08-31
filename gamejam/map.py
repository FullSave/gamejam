#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .wall import Wall


class Map(object):
    def __init__(self, offset_x, offset_y):
        self._offset_x = offset_x
        self._offset_y = offset_y
        self.reset()

    def reset(self):
        """ Static map re-generation.
        """
        self._walls = [
            # racks room
            Wall(0, 128, 32, 8),
            Wall(64, 128, 96, 8),
            Wall(160, 0, 8, 136),

            # providers room
            Wall(0, 160, 80, 8),
            Wall(112, 160, 8, 72),

            # table room
            Wall(154, 160, 56, 8),
            Wall(210, 160, 8, 72),

            # network room
            Wall(208, 128, 48, 8),
            Wall(200, 32, 8, 104),
        ]
        self._racks = []
        self._providers = []
        self._tables = []

        # self._player = None

    def update(self):
        pass

    def draw(self):
        entities = self._walls + self._racks + self._providers + self._tables
        for entity in entities:
            entity.draw(self._offset_x, self._offset_y)

        # self._player.draw(self._offset_x, self._offset_y)
