#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
from pyxel.constants import FONT_WIDTH, FONT_HEIGHT


TXT_COLOR = 7
TXT_SPACE = 2
BORDER_COLOR = 7
FULL_ORDER_COLOR = 6
EMPTY_ORDER_COLOR = 5


class Margin(object):

    def __init__(self, top, right, down, left):
        self.top = top
        self.right = right
        self.down = down
        self.left = left


class Order(object):

    def __init__(self):
        pass

    def validate(self, server):
        pass


class ScoreBoard(object):

    def __init__(self, map):
        self._map = map
        self._margin = Margin(5, 5, 5, 5)
        self._orders = []

    def get_pos(self):
        return (0, 0)

    def get_size(self):
        return (256, 24)

    def get_margin(self):
        return self._margin

    def get_score(self):
        return 19850

    def get_timer(self):
        return 320

    def _draw_borders(self, x, y, w, h):
        pyxel.line(x, y+h-1, x+w, y+h-1, BORDER_COLOR)

    def _draw_score(self, x, y):
        margin = self.get_margin()
        x += margin.left
        y += margin.top
        pyxel.text(x, y, "TIME: {:d}".format(self.get_timer()), TXT_COLOR)
        y += FONT_HEIGHT + TXT_SPACE
        pyxel.text(x, y, "SCORE: {:d}".format(self.get_score()), TXT_COLOR)

    def _draw_order(self, x, y, order=None):
        if order:
            pyxel.rectb(x+2, y+2, x+61, y+20, FULL_ORDER_COLOR)
        else:
            pyxel.rectb(x+2, y+2, x+61, y+20, EMPTY_ORDER_COLOR)

    def _draw_orders(self, x, y):
        for i in range(0, 3):
            if len(self._orders) > i:
                order = self._orders[i]
            else:
                order = None
            self._draw_order(i*64+x, y, order)

    def draw(self):
        (x, y) = self.get_pos()
        (w, h) = self.get_size()
        self._draw_borders(x, y, w, h)
        self._draw_score(x, y)
        self._draw_orders(x+64, y)
