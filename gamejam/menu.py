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
    _width = 255
    _height = 255

    def __init__(self):
        pyxel.init(
            self._width, self._height, caption="Gamejam - FullSave", fps=60)

        # Load sprites
        SpriteSheet().add_sprite("cpu", Sprite(STATIC_IMAGES, 0, 0, 16, 16, 7))
        SpriteSheet().add_sprite("ram", Sprite(STATIC_IMAGES, 16, 0, 16, 16, 7))
        SpriteSheet().add_sprite("server", Sprite(STATIC_IMAGES, 32, 0, 16, 16, 7))
        SpriteSheet().add_sprite("wall", Sprite(STATIC_IMAGES, 48, 0, 8, 8, 7))
        SpriteSheet().add_sprite("rack0", Sprite(STATIC_IMAGES, 0, 16, 32, 32, 7))
        SpriteSheet().add_sprite("rack1", Sprite(STATIC_IMAGES, 32, 16, 32, 32, 7))
        SpriteSheet().add_sprite("power", Sprite(STATIC_IMAGES, 64, 16, 32, 32, 7))
        SpriteSheet().add_sprite("network", Sprite(STATIC_IMAGES, 96, 16, 32, 32, 7))
        SpriteSheet().add_sprite("provider_cpu", Sprite(STATIC_IMAGES, 0, 48, 32, 32, 7))
        SpriteSheet().add_sprite("provider_ram", Sprite(STATIC_IMAGES, 32, 48, 32, 32, 7))
        SpriteSheet().add_sprite("provider_case", Sprite(STATIC_IMAGES, 64, 48, 32, 32, 7))
        SpriteSheet().add_sprite("table", Sprite(STATIC_IMAGES, 96, 48, 32, 32, 7))

        # SpriteSheet().add_sprite("player_left0", Sprite(128, 16, 32, 32, 7))
        # SpriteSheet().add_sprite("player_left1", Sprite(160, 16, 32, 32, 7))
        # SpriteSheet().add_sprite("player_right0", Sprite(192, 16, 32, 32, 7))
        # SpriteSheet().add_sprite("player_right1", Sprite(224, 16, 32, 32, 7))
        # SpriteSheet().add_sprite("chicken_front", Sprite(128, 144, 32, 32, 14))
        # SpriteSheet().add_sprite("chicken_right", Sprite(160, 144, 32, 32, 14))
        # SpriteSheet().add_sprite("chicken_back", Sprite(192, 144, 32, 32, 14))
        # SpriteSheet().add_sprite("chicken_left", Sprite(224, 144, 32, 32, 14))

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
        SpriteSheet().add_sprite("racks_1_top", Sprite(BACKGROUND_IMAGE, 36, 85, 24, 26, 6))
        SpriteSheet().add_sprite("racks_2_top", Sprite(BACKGROUND_IMAGE, 68, 85, 24, 26, 6))
        SpriteSheet().add_sprite("racks_3_top", Sprite(BACKGROUND_IMAGE, 100, 85, 24, 26, 6))
        SpriteSheet().add_sprite("racks_4_top", Sprite(BACKGROUND_IMAGE, 132, 85, 24, 26, 6))
        SpriteSheet().add_sprite("racks_5_top", Sprite(BACKGROUND_IMAGE, 164, 85, 24, 26, 6))
        SpriteSheet().add_sprite("racks_6_top", Sprite(BACKGROUND_IMAGE, 36, 21, 24, 26, 6))
        SpriteSheet().add_sprite("racks_7_top", Sprite(BACKGROUND_IMAGE, 68, 21, 24, 26, 6))
        SpriteSheet().add_sprite("racks_8_top", Sprite(BACKGROUND_IMAGE, 100, 21, 24, 26, 6))
        SpriteSheet().add_sprite("racks_9_top", Sprite(BACKGROUND_IMAGE, 132, 21, 24, 26, 6))
        SpriteSheet().add_sprite("racks_10_top", Sprite(BACKGROUND_IMAGE, 164, 21, 24, 26, 6))
        SpriteSheet().add_sprite("wall_left", Sprite(BACKGROUND_IMAGE, 0, 143, 72, 25, 6))
        SpriteSheet().add_sprite("wall_middle", Sprite(BACKGROUND_IMAGE, 108, 143, 8, 25, 6))
        SpriteSheet().add_sprite("wall_right", Sprite(BACKGROUND_IMAGE, 152, 143, 72, 25, 6))
        SpriteSheet().add_sprite("table_left", Sprite(BACKGROUND_IMAGE, 0, 200, 96, 8, 6))
        SpriteSheet().add_sprite("table_right", Sprite(BACKGROUND_IMAGE, 160, 200, 64, 8, 6))

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
