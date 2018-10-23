#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel

from .misc import SpriteSheet, Sprite
from .map import Map
from .scoreboard import ScoreBoard


class Menu(object):
    _width = 255
    _height = 255

    def __init__(self):
        pyxel.init(
            self._width, self._height, caption="Gamejam - FullSave", fps=60)

        # Load sprites
        SpriteSheet().add_sprite("cpu", Sprite(0, 0, 16, 16, 7))
        SpriteSheet().add_sprite("ram", Sprite(16, 0, 16, 16, 7))
        SpriteSheet().add_sprite("server", Sprite(32, 0, 16, 16, 7))
        SpriteSheet().add_sprite('wall', Sprite(48, 0, 8, 8, 7))
        SpriteSheet().add_sprite("rack0", Sprite(0, 16, 32, 32, 7))
        SpriteSheet().add_sprite("rack1", Sprite(32, 16, 32, 32, 7))
        SpriteSheet().add_sprite("power", Sprite(64, 16, 32, 32, 7))
        SpriteSheet().add_sprite("network", Sprite(96, 16, 32, 32, 7))
        SpriteSheet().add_sprite("player_left0", Sprite(128, 16, 32, 32, 7))
        SpriteSheet().add_sprite("player_left1", Sprite(160, 16, 32, 32, 7))
        SpriteSheet().add_sprite("player_right0", Sprite(192, 16, 32, 32, 7))
        SpriteSheet().add_sprite("player_right1", Sprite(224, 16, 32, 32, 7))
        SpriteSheet().add_sprite("chicken_front", Sprite(128, 144, 32, 32, 14))
        SpriteSheet().add_sprite("chicken_right", Sprite(160, 144, 32, 32, 14))
        SpriteSheet().add_sprite("chicken_back", Sprite(192, 144, 32, 32, 14))
        SpriteSheet().add_sprite("chicken_left", Sprite(224, 144, 32, 32, 14))
        SpriteSheet().add_sprite("provider_cpu", Sprite(0, 48, 32, 32, 7))
        SpriteSheet().add_sprite("provider_ram", Sprite(32, 48, 32, 32, 7))
        SpriteSheet().add_sprite("provider_case", Sprite(64, 48, 32, 32, 7))
        SpriteSheet().add_sprite("table", Sprite(96, 48, 32, 32, 7))

        self.map = Map(0, 24)
        self.scoreboard = ScoreBoard(self.map)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            # Restart the game
            pass

        self.map.update()

        if self.map.game_over:
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        # Draw UI
        self.scoreboard.draw()

        # Draw Map
        self.map.draw()


if __name__ == '__main__':
    Menu()
