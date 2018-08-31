#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import os

import pyxel

from map import Map
from misc import SPRITESHEET_IMAGE
from scoreboard import ScoreBoard


class Menu(object):
    _width = 256
    _height = 256

    def __init__(self):
        pyxel.init(self._width, self._height, caption="Gamejam - FullSave")

        assets = os.path.join(os.path.dirname(__file__), 'assets')
        pyxel.image(SPRITESHEET_IMAGE).load(
            0, 0, os.path.join(assets, 'spritesheet.png'))

        self.map = Map()
        self.scoreboard = ScoreBoard(self.map)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            # Restart the game
            pass

        self.map.update()

    def draw(self):
        pyxel.cls(0)

        # Draw UI
        self.scoreboard.draw()

        # Draw Map
        self.map.draw()


if __name__ == '__main__':
    Menu()
