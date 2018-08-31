#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import os

import pyxel


class Game(object):
    _width = 256
    _height = 256

    def __init__(self):
        pyxel.init(self._width, self._height, caption="Gamejam - FullSave")

        assets = os.path.join(os.path.dirname(__file__), 'assets')
        # pyxel.image(0).load(0, 0, os.path.join(assets, 'logo.png')) 

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass


if __name__ == '__main__':
    Game()
