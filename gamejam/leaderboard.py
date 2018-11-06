#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
import json
import os.path

SAVEFILE = os.path.abspath(os.path.dirname(__file__) + "/..") + "/ranking.json"

TITLE_COLOR = 8
FIRST_COLOR = 9
RANK_COLOR = 7


class LeaderBoard(object):

    def __init__(self, game):
        self._game = game
        self._ranking = []
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
        i = 0
        while i < len(self._ranking):
            if score > self._ranking[i][1]:
                break
            i += 1
        self._ranking.insert(i, (player_name, score))
        self.save()
        return i + 1

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._game.start_map()

    def draw(self):
        pyxel.text(100, 5, "LEADER BOARD", TITLE_COLOR)
        rank = 0
        for (name, score) in self._ranking:
            rank += 1
            if rank > 20:
                break
            row = "{0:2d}.{1:.<43s}{2:05d}".format(rank, name, score)
            if rank==1:
                color = FIRST_COLOR
            else:
                color = RANK_COLOR
            pyxel.text(25, 10 + (rank*10), row, color)
    
        pyxel.text(25, 235, "Press SPACE to continue...", TITLE_COLOR)