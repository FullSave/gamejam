#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import time
import pyxel
from pyxel.constants import FONT_WIDTH

from .misc import BACKGROUND_IMAGE, SpriteSheet, Hitbox, KEYS_TO_CHAR
from .player import Player
from .wall import Wall
from .rack import Rack
from .providers import RAMProvider, CPUProvider, CaseProvider
from .table import Table
from .trash import Trash
from .scoreboard import ScoreBoard
from .gamepad import Controller

START_TIME = 60.0  # Time (in seconds)


class Map(object):
    def __init__(self, game, offset_x, offset_y):
        self._game = game
        self._offset_x = offset_x
        self._offset_y = offset_y
        self._width = pyxel.width - offset_x
        self._height = pyxel.height - offset_y

        # Game controller
        self._controller = Controller()
        self.reset()

    def reset(self):
        """ Static map re-generation.
        """
        self._score = 0
        self._time = START_TIME
        self._prevtime = time.perf_counter()

        self._player_name = ""
        self._cursor_counter = 0
        self._is_completed = False

        # Error bubble
        self._error_bubble_fadeout = 0

        self._walls = [
            # Left wall
            Wall(0, 143, 72, 33, "left", Hitbox(0, 24, 72, 9)),
            # Middle wall
            Wall(108, 143, 8, 57, "middle", Hitbox(0, 24, 8, 57)),
            # Right wall
            Wall(152, 143, 72, 33, "right", Hitbox(0, 24, 72, 9)),
        ]

        self._racks = []
        for i in range(1, 6):
            self._racks.append(Rack(36 + 32 * (i-1), 85, 24, 42, "%s" % i))
            self._racks.append(Rack(36 + 32 * (i-1), 21, 24, 42, "%s" % (i+5)))

        self._providers = [
            CPUProvider(0, 200, number=0),
            RAMProvider(32, 200, number=1),
            CaseProvider(64, 200, number=2),
        ]

        self._tables = [
            Table(160, 200, number=3),
            Table(192, 200, number=4),
        ]

        self._trashs = [
            Trash(128, 192)
        ]

        self._player = Player(self, 32, 120)
        self._scoreboard = ScoreBoard(self)

    @property
    def game_over(self):
        return self._time <= 0.0

    @property
    def time(self):
        return self._time

    def increase_time(self, value):
        self._prevtime += value

    @property
    def score(self):
        return self._score

    def increase_score(self, value):
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
    def trashs(self):
        return self._trashs

    @property
    def player(self):
        return self._player

    @property
    def elements(self):
        return self._walls + self._racks + self._providers + \
            self._tables + self._trashs

    def show_error_bubble(self):
        self._error_bubble_fadeout = 120

    def update(self):
        if not self._is_completed:
            self.gameloop()
        else:
            self.timeoutloop()

    def gameloop(self):
        t = time.perf_counter()
        delta = t - self._prevtime
        self._prevtime = t
        self._time -= delta
        if self._time <= 0.0:
            self._time = 0.0
            self._is_completed = True

        if self._error_bubble_fadeout:
            self._error_bubble_fadeout -= 1

        # Move player
        move_x = move_y = 0
        speed = 2

        axs_x = self._controller.get_axis('x') or self._controller.get_axis('hat0x')
        axs_y = self._controller.get_axis('y') or self._controller.get_axis('hat0y')
        btn_a = self._controller.is_pressed('thumb')

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or axs_y < 0:
            move_y = -speed
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) or axs_y > 0:
            move_y = speed
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or axs_x < 0:
            move_x = -speed
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or axs_x > 0:
            move_x = speed

        if pyxel.btnp(pyxel.KEY_SPACE) or btn_a:
            self._player.interact()

        if move_x != 0 or move_y != 0:
            self._player.move(move_x, move_y)
        else:
            self._player.reset_animation()

    def timeoutloop(self):
        # Cycle through all the key, if one is pressed, change the player name
        for key in pyxel.__dict__.keys():
            if key.startswith('KEY_') and pyxel.btnp(getattr(pyxel, key)):
                if key in KEYS_TO_CHAR:
                    if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                        self._player_name += KEYS_TO_CHAR[key].upper()
                    else:
                        self._player_name += KEYS_TO_CHAR[key]
                elif key == 'KEY_BACKSPACE':
                    self._player_name = self._player_name[:-1]
                elif key == 'KEY_ENTER':
                    self._game.complete_map(self._player_name)

    def _centered_text(self, y, text):
        pyxel.text(
            self._width / 2 - len(text) * FONT_WIDTH / 2,
            y + 3, text, 11)

    def draw(self):
        self._scoreboard.draw()

        pyxel.blt(
            self._offset_x,
            self._offset_y,
            BACKGROUND_IMAGE,
            0, 0,
            self._offset_x + self._width,
            self._offset_y + self._height)

        objects = self.elements + [self._player]
        sorted_objects = sorted(objects, key=lambda e: e.y)

        for obj in sorted_objects:
            obj.draw(self._offset_x, self._offset_y)

        # Show error bubble
        if self._error_bubble_fadeout:
            pyxel.blt(
                self.offset_x + self._player.x - 8,
                self.offset_y + self._player.y - 20,
                *SpriteSheet().get_sprite("error_bubble").render())

        if self._is_completed:
            x1 = (self._width - 152) / 2 + self._offset_x
            y1 = (self._height - 40) / 2 + self._offset_y
            x2 = (self._width + 152) / 2 + self._offset_x
            y2 = (self._height + 40) / 2 + self._offset_y
            pyxel.rect(x1, y1, x2, y2, 0)
            pyxel.rectb(x1, y1, x2, y2, 5)
            self._centered_text(y1 + 3, "Timeout !")
            rank = self._game.leaderboard.get_score_rank(self.score)
            suffix = "th"
            if rank == 2:
                suffix = "nd"
            elif rank == 1:
                suffix = "st"
            self._centered_text(
                y1 + 11,
                "You are ranked at the %s%s position." % (rank, suffix))
            self._centered_text(
                y1 + 19,
                "Please enter your name :")
            cursor = " "
            if self._cursor_counter > 30:
                cursor = "_"

            self._cursor_counter += 1
            if self._cursor_counter >= 60:
                self._cursor_counter = 0

            self._centered_text(
                y1 + 27,
                "%s%s" % (self._player_name, cursor)
            )
