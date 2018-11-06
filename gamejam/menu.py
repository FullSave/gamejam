#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel

from .leaderboard import LeaderBoard
from .misc import SpriteSheet, Sprite, STATIC_IMAGES, PLAYER_IMAGE, \
    BACKGROUND_IMAGE
from .map import Map


class Menu(object):
    _width = 224
    _height = 248

    def __init__(self):
        pyxel.init(
            self._width, self._height, caption="Gamejam - FullSave", fps=60)

        # Load sprites
        SpriteSheet().add_sprite(
            "item_cpu", Sprite(STATIC_IMAGES, 0, 0, 32, 32, 11))
        SpriteSheet().add_sprite(
            "item_ram", Sprite(STATIC_IMAGES, 32, 0, 32, 32, 11))
        SpriteSheet().add_sprite(
            "error_bubble", Sprite(STATIC_IMAGES, 64, 0, 32, 32, 11))
        SpriteSheet().add_sprite(
            "wall_texture", Sprite(STATIC_IMAGES, 96, 0, 32, 32, 11))
        SpriteSheet().add_sprite(
            "gamejam_logo", Sprite(STATIC_IMAGES, 0, 128, 96, 32, 11)
        )
        SpriteSheet().add_sprite(
            "fullsave_logo", Sprite(STATIC_IMAGES, 96, 64, 32, 32, 11)
        )
        SpriteSheet().add_sprite(
            "devfest_logo", Sprite(STATIC_IMAGES, 96, 96, 32, 32, 11)
        )

        # Server CPU/RAM combination
        for cpu in range(0, 3):
            for ram in range(0, 3):
                SpriteSheet().add_sprite(
                    "server_%s_%s" % (cpu, ram),
                    Sprite(STATIC_IMAGES, 32 * ram, 32 + 32 * cpu, 32, 32, 11))

        # Player down
        for i in range(0, 4):
            SpriteSheet().add_sprite(
                "player_bottom%s" % i,
                Sprite(PLAYER_IMAGE, 32 * i, 0, 32, 32, 6)
            )

        # Player right
        for i in range(0, 4):
            SpriteSheet().add_sprite(
                "player_right%s" % i,
                Sprite(PLAYER_IMAGE, 128 + 32 * i, 0, 32, 32, 6)
            )

        # Player up
        for i in range(0, 4):
            SpriteSheet().add_sprite(
                "player_top%s" % i,
                Sprite(PLAYER_IMAGE, 32 * i, 32, 32, 32, 6)
            )

        # Player left
        for i in range(0, 4):
            SpriteSheet().add_sprite(
                "player_left%s" % i,
                Sprite(PLAYER_IMAGE, 128 + 32 * i, 32, 32, 32, 6)
            )

        # Background elements that can be in front of the player
        for i in range(1, 6):
            SpriteSheet().add_sprite(
                "rack_%s" % i,
                Sprite(BACKGROUND_IMAGE, 36 + 32*(i-1), 85, 24, 42, 6))
            SpriteSheet().add_sprite(
                "rack_%s" % (i + 5),
                Sprite(BACKGROUND_IMAGE, 36 + 32*(i-1), 21, 24, 42, 6))

        # Walls
        SpriteSheet().add_sprite(
            "wall_left", Sprite(BACKGROUND_IMAGE, 0, 143, 72, 25, 6))
        SpriteSheet().add_sprite(
            "wall_middle", Sprite(BACKGROUND_IMAGE, 108, 143, 8, 25, 6))
        SpriteSheet().add_sprite(
            "wall_right", Sprite(BACKGROUND_IMAGE, 152, 143, 72, 25, 6))

        # Tables
        SpriteSheet().add_sprite(
            "table_0", Sprite(BACKGROUND_IMAGE, 0, 200, 32, 24, 6))
        SpriteSheet().add_sprite(
            "table_1", Sprite(BACKGROUND_IMAGE, 32, 200, 32, 24, 6))
        SpriteSheet().add_sprite(
            "table_2", Sprite(BACKGROUND_IMAGE, 64, 200, 32, 24, 6))
        SpriteSheet().add_sprite(
            "table_3", Sprite(BACKGROUND_IMAGE, 160, 200, 32, 24, 6))
        SpriteSheet().add_sprite(
            "table_4", Sprite(BACKGROUND_IMAGE, 192, 200, 32, 24, 6))

        # Trash
        SpriteSheet().add_sprite(
            "trash", Sprite(STATIC_IMAGES, 96, 32, 32, 32, 11))

        self.map = Map(self, 0, 24)
        self.leaderboard = LeaderBoard(self)

        self.current_state = self.leaderboard

        pyxel.run(self.update, self.draw)

    def start_map(self):
        self.map.reset()
        self.current_state = self.map

    def complete_map(self, player_name):
        score = self.map.score
        ranking = self.leaderboard.add_score(player_name, score)
        self.current_state = self.leaderboard

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            # Restart the game
            pass

        self.current_state.update()

    def draw(self):
        pyxel.cls(0)
        # Draw Map
        self.current_state.draw()


if __name__ == '__main__':
    Menu()
