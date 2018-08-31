#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import pyxel
import random
from pyxel.constants import FONT_WIDTH, FONT_HEIGHT
from .server import Server, RAM, CPU
from .rack import Rack


TXT_COLOR = 7
TXT_SPACE = 2
BORDER_COLOR = 7
ICO_BG_COLOR = 5
FULL_ORDER_COLOR = 6
EMPTY_ORDER_COLOR = 5


class Margin(object):

    def __init__(self, top, right, down, left):
        self.top = top
        self.right = right
        self.down = down
        self.left = left


class Order(object):

    def __init__(self, rack, n_ram, n_cpu):
        self._rack = rack
        self._server = Server(ram=n_ram, cpu=n_cpu)
        self._cpuitem = CPU()
        self._ramitem = RAM()

    def validate(self, rack, server):
        pass

    def draw(self, x, y):
        pyxel.rectb(x+5, y+5, x+16, y+16, 12)
        pyxel.text(x+9, y+8, self._rack.number, TXT_COLOR)
        #self._server.draw(x+19, y+5)
        pyxel.rect(x+19, y+5, x+30, y+16, ICO_BG_COLOR)
        #self._cpuitem.draw(x+33, y+44)
        pyxel.rect(x+33, y+5, x+44, y+16, ICO_BG_COLOR)
        pyxel.text(x+41, y+11, str(self._server._cpu), TXT_COLOR)
        #self._ramitem.draw(x+47, y+58)
        pyxel.rect(x+47, y+5, x+58, y+16, ICO_BG_COLOR)
        pyxel.text(x+55, y+11, str(self._server._ram), TXT_COLOR)


class ScoreBoard(object):

    def __init__(self, map):
        random.seed()
        self._map = map
        self._margin = Margin(5, 5, 5, 5)
        self._orders = []

        order = self.generate_order()
        self._orders.append(order)
        order = self.generate_order()
        self._orders.append(order)

    def get_random_rack(self):
        racks = list(filter(lambda x: not x.is_full, self._map.racks))
        return random.choice(racks)

    def generate_order(self):
        return Order(self.get_random_rack(), n_ram=random.randint(0, 2), n_cpu=random.randint(0, 2))

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
        pyxel.line(x, y+h-2, x+w, y+h-2, BORDER_COLOR)

    def _draw_score(self, x, y):
        margin = self.get_margin()
        x += margin.left
        y += margin.top
        pyxel.text(x, y, "TIME: {:d}".format(self.get_timer()), TXT_COLOR)
        y += FONT_HEIGHT + TXT_SPACE
        pyxel.text(x, y, "SCORE: {:d}".format(self.get_score()), TXT_COLOR)

    def _draw_order(self, x, y, order=None):
        if order:
            pyxel.rectb(x+2, y+2, x+61, y+19, FULL_ORDER_COLOR)
            order.draw(x, y)
        else:
            pyxel.rectb(x+2, y+2, x+61, y+19, EMPTY_ORDER_COLOR)

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
