#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element


class Wall(Element):
    def __init__(self, x, y, w, h):
        Element.__init__(self, x, y, w, h)
        self.get_sprite('wall')

    def draw(self, offset_x, offset_y):
        count_x = int(self.w / self.sprite.w)
        count_y = int(self.h / self.sprite.h)
        for x in range(count_x):
            for y in range(count_y):
                Element.draw(
                    self,
                    offset_x + x*self.sprite.w,
                    offset_y + y*self.sprite.h
                )
