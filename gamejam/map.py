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


FLOOR_COLOR = 7


class Map(object):
    def __init__(self, offset_x, offset_y):
        self._offset_x = offset_x
        self._offset_y = offset_y
        self._width = pyxel.width - offset_x
        self._height = pyxel.height - offset_y
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
            Wall(0, 168, 80, 8),
            Wall(112, 168, 8, 64),

            # table room
            Wall(154, 168, 56, 8),
            Wall(210, 168, 8, 64),

            # network room
            Wall(208, 128, 48, 8),
            Wall(200, 32, 8, 104),
        ]
        self._racks = [
            Rack(0, 0, 32, 32, "1"),
            Rack(32, 0, 32, 32, "2"),
            Rack(64, 0, 32, 32, "3"),
            Rack(96, 0, 32, 32, "4"),
            Rack(0, 64, 32, 32, "5"),
            Rack(32, 64, 32, 32, "6"),
            Rack(64, 64, 32, 32, "7"),
            Rack(96, 64, 32, 32, "8"),
        ]
        self._racks[3].get_sprite("rack1")
        self._racks[7].get_sprite("rack1")
        self._providers = []
        self._tables = []

        self._player = Player(self, 32, 120)

    @property
    def offset_x(self):
        return self._offset_x

    @property
    def offset_y(self):
        return self._offset_y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

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

    @property
    def elements(self):
        return self._walls + self._racks + self._providers + self._tables

    def update(self):
        # Move player
        move_x = move_y = 0
        speed = 2

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            move_y = -speed
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            move_y = speed
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            move_x = -speed
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            move_x = speed

        if move_x != 0 or move_y != 0:
            self._player.move(move_x, move_y)

    def draw(self):
        pyxel.rect(self._offset_x,
                   self._offset_y,
                   self._offset_x + self._width - 1,
                   self._offset_y + self._height - 1,
                   FLOOR_COLOR)
        for element in self.elements:
            element.draw(self._offset_x, self._offset_y)

        self._player.draw(self._offset_x, self._offset_y)
