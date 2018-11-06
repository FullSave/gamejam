#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import json
import os.path
import pyxel
import random
from pyxel.constants import FONT_WIDTH

from .misc import SpriteSheet

SAVEFILE = os.path.abspath(os.path.dirname(__file__) + "/..") + "/ranking.json"

TITLE_COLOR = 8
FIRST_COLOR = 9
RANK_COLOR = 7

LOGO_QUOTES = [
    "Don't forget to restart sup'",
    "With love from FullSave",
    "Don't touch the red button !",
    "Ice cream ! Ice cream everywhere !!",
    "So long and thanks for all the fish",
    "E_NOQUOTE",
    "404 Quote not found",
    "It's not bug..well...maybe it is"
]


class LeaderBoard(object):

    def __init__(self, game):
        self._game = game
        self._ranking = []
        self._screen_counter = 0
        self._screen_quote = random.choice(LOGO_QUOTES)
        self.load()

    def load(self):
        try:
            with open(SAVEFILE, "r") as fp:
                data = json.load(fp)
        except OSError:
            print("Unable to read ranking file.")
        else:
            try:
                self._ranking = data["ranking"]
            except KeyError:
                print("Unable to parse ranking file.")

    def save(self):
        try:
            with open(SAVEFILE, "w") as fp:
                json.dump({"ranking": self._ranking}, fp)
        except OSError:
            print("Unable to write ranking file.")

    def add_score(self, player_name, score):
        """ Add player score to ranking, save new ranking, then return the
        player position in leader board.
        """
        i = self.get_score_rank(score)
        self._ranking.insert(i - 1, (player_name, score))
        self.save()
        return i

    def get_score_rank(self, score):
        i = 0
        while i < len(self._ranking):
            if score > self._ranking[i][1]:
                break
            i += 1
        return i + 1

    @classmethod
    def centered_text(cls, pos_y, text, color):
        pyxel.text(pyxel.width/2 - len(text)*FONT_WIDTH/2, pos_y, text, color)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._game.start_map()

    def draw_ranking(self):
        self.centered_text(5, "LEADER BOARD", TITLE_COLOR)
        rank = 0
        for (name, score) in self._ranking:
            rank += 1
            if rank > 20:
                break
            row = "{0:2d}.{1:.<43s}{2:06d}".format(rank, name, score)
            if rank == 1:
                color = FIRST_COLOR
            else:
                color = RANK_COLOR
            self.centered_text(10 + (rank*10), row, color)

    def draw_logo(self):
        pyxel.blt(
            (pyxel.width - 96) / 2,
            100,
            *SpriteSheet().get_sprite("gamejam_logo").render())
        self.centered_text(116, self._screen_quote, 10)

    def draw(self):
        if self._screen_counter >= 300:
            self.draw_ranking()
        else:
            self.draw_logo()

        self.centered_text(228, "Press SPACE to continue...", TITLE_COLOR)

        self._screen_counter += 1
        if self._screen_counter >= 600:
            self._screen_quote = random.choice(LOGO_QUOTES)
            self._screen_counter = 0
