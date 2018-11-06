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

        for cpu in range(0, 3):
            for ram in range(0, 3):
                SpriteSheet().add_sprite(
                    "server_%s_%s" % (cpu, ram),
                    Sprite(STATIC_IMAGES, 32 * ram, 32 + 32 * cpu, 32, 32, 11))

        SpriteSheet().add_sprite("player_bottom0", Sprite(PLAYER_IMAGE, 0, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_bottom1", Sprite(PLAYER_IMAGE, 32, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_bottom2", Sprite(PLAYER_IMAGE, 64, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_bottom3", Sprite(PLAYER_IMAGE, 96, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_right0", Sprite(PLAYER_IMAGE, 128, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_right1", Sprite(PLAYER_IMAGE, 160, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_right2", Sprite(PLAYER_IMAGE, 192, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_right3", Sprite(PLAYER_IMAGE, 224, 0, 32, 32, 6))
        SpriteSheet().add_sprite("player_top0", Sprite(PLAYER_IMAGE, 0, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_top1", Sprite(PLAYER_IMAGE, 32, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_top2", Sprite(PLAYER_IMAGE, 64, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_top3", Sprite(PLAYER_IMAGE, 96, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_left0", Sprite(PLAYER_IMAGE, 128, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_left1", Sprite(PLAYER_IMAGE, 160, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_left2", Sprite(PLAYER_IMAGE, 192, 32, 32, 32, 6))
        SpriteSheet().add_sprite("player_left3", Sprite(PLAYER_IMAGE, 224, 32, 32, 32, 6))

        # Background elements that can be in front of the player
        for i in range(1, 6):
            SpriteSheet().add_sprite(
                "racks_%s_top" % i,
                Sprite(BACKGROUND_IMAGE, 36 + 32*(i-1), 85, 24, 26, 6))
            SpriteSheet().add_sprite(
                "racks_%s_top" % (i + 5),
                Sprite(BACKGROUND_IMAGE, 36 + 32*(i-1), 21, 24, 26, 6))
        SpriteSheet().add_sprite("wall_left", Sprite(BACKGROUND_IMAGE, 0, 143, 72, 25, 6))
        SpriteSheet().add_sprite("wall_middle", Sprite(BACKGROUND_IMAGE, 108, 143, 8, 25, 6))
        SpriteSheet().add_sprite("wall_right", Sprite(BACKGROUND_IMAGE, 152, 143, 72, 25, 6))
        SpriteSheet().add_sprite("table_left", Sprite(BACKGROUND_IMAGE, 0, 200, 96, 8, 6))
        SpriteSheet().add_sprite("table_right", Sprite(BACKGROUND_IMAGE, 160, 200, 64, 8, 6))
        SpriteSheet().add_sprite("trash_top", Sprite(BACKGROUND_IMAGE, 134, 204, 17, 12, 7))

        self.map = Map(self, 0, 24)
        self.leaderboard = LeaderBoard(self)

        self.current_state = self.leaderboard

        pyxel.run(self.update, self.draw)

    def start_map(self):
        self.map.reset()
        self.current_state = self.map

    def complete_map(self):
        player_name = "Unamed player"  # FIXME: get player name
        score = self.map.score
        ranking = self.leaderboard.add_score(player_name, score)
        self.current_state = self.leaderboard

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            # Restart the game
            pass

        self.current_state.update()

        #if self.map.game_over:
        #    pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # Draw Map
        self.current_state.draw()

if __name__ == '__main__':
    Menu()
