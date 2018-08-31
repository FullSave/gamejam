#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel

from .player import Player
from .wall import Wall
from .rack import Rack


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
        self._racks = [
            Rack(0, 0, 32, 32, "1"),
            Rack(32, 0, 32, 32, "2"),
        ]
        self._providers = []
        self._tables = []

        self._player = Player(self, 0, 0, 16, 32)

    @property
    def walls(self):
        return self._walls

    @property
    def racks(self):
        return self._racks

    @property
    def providers(self):
        return self._providers

    @property
    def tables(self):
        return self._tables

    @property
    def player(self):
        return self._player

    def update(self):
        # Move player
        move_x = move_y = 0
        speed = 2

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            move_y = -speed
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            move_y = speed
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            move_x = -speed
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            move_x = speed

        self._player.move(move_x, move_y)

    def draw(self):
        entities = self._walls + self._racks + self._providers + self._tables
        for entity in entities:
            entity.draw(self._offset_x, self._offset_y)

        self._player.draw(self._offset_x, self._offset_y)
