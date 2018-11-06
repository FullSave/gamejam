#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import time
import pyxel

from .misc import BACKGROUND_IMAGE, SpriteSheet
from .player import Player
from .wall import Wall
from .rack import Rack
from .providers import RAMProvider, CPUProvider, CaseProvider
from .table import Table
from .scoreboard import ScoreBoard


START_TIME = 120.0  # Time (in seconds)


class Map(object):
    def __init__(self, game, offset_x, offset_y):
        self._game = game
        self._offset_x = offset_x
        self._offset_y = offset_y
        self._width = pyxel.width - offset_x
        self._height = pyxel.height - offset_y
        self.reset()

    def reset(self):
        """ Static map re-generation.
        """
        self._score = 0
        self._time = START_TIME
        self._prevtime = time.perf_counter()

        self._walls = [
            # Left wall
            Wall(0, 167, 72, 9),
            # Middle wall
            Wall(107, 167, 9, 57),
            # Right wall
            Wall(151, 167, 72, 9),
        ]

        self._racks = []
        for i in range(1, 6):
            self._racks.append(Rack(36 + 32 * (i-1), 85, 24, 42, "%s" % i))
            self._racks.append(Rack(36 + 32 * (i-1), 21, 24, 42, "%s" % (i+5)))

        self._providers = [
            RAMProvider(0, 200),
            CPUProvider(32, 200),
            CaseProvider(64, 200),
        ]

        self._tables = [
            Table(160, 200),
            Table(192, 200),
        ]

        self._player = Player(self, 32, 120)
        self._scoreboard = ScoreBoard(self)

    @property
    def game_over(self):
        return self._time <= 0.0

    @property
    def time(self):
        return self._time

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score += value

    @property
    def scoreboard(self):
        return self._scoreboard

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
        t = time.perf_counter()
        delta = t - self._prevtime
        self._prevtime = t
        self._time -= delta
        if self._time <= 0.0:
            self._time = 0.0
            self._game.complete_map()

        # Move player
        move_x = move_y = 0
        speed = 1.5

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            move_y = -speed
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            move_y = speed
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            move_x = -speed
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            move_x = speed
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self._player.interact()

        if move_x != 0 or move_y != 0:
            self._player.move(move_x, move_y)

    def draw(self):
        self._scoreboard.draw()

        pyxel.blt(self._offset_x,
                   self._offset_y,
                   BACKGROUND_IMAGE,
                   0, 0,
                   self._offset_x + self._width,
                   self._offset_y + self._height)

        for element in self.elements:
            element.draw(self._offset_x, self._offset_y)

        self._player.draw(self._offset_x, self._offset_y)

        # Draw the part in front of the player if needed
        if self._player.y < 37:
            for i in range(0, 5):
                pyxel.blt(
                    self.offset_x + 36 + 32 * i, self.offset_y + 21,
                    *SpriteSheet().get_sprite("racks_%s_top" % (i+6)).render())
        elif self._player.y < 110:
            for i in range(0, 5):
                pyxel.blt(
                    self.offset_x + 36 + 32 * i, self.offset_y + 85,
                    *SpriteSheet().get_sprite("racks_%s_top" % (i+1)).render())
        elif self._player.y < 167:
            pyxel.blt(
                self.offset_x + 0, self.offset_y + 143,
                *SpriteSheet().get_sprite("wall_left").render())
            pyxel.blt(
                self.offset_x + 108, self.offset_y + 143,
                *SpriteSheet().get_sprite("wall_middle").render())
            pyxel.blt(
                self.offset_x + 152, self.offset_y + 143,
                *SpriteSheet().get_sprite("wall_right").render())
        elif self._player.y < 209:
            pyxel.blt(
                self.offset_x + 0, self.offset_y + 200,
                *SpriteSheet().get_sprite("table_left").render())
            pyxel.blt(
                self.offset_x + 160, self.offset_y + 200,
                *SpriteSheet().get_sprite("table_right").render())
