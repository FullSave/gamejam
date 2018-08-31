#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element


class Rack(Element):
    def __init__(self, x, y, w, h, number):
        Element.__init__(self, x, y, w, h)
        self.get_sprite("rack0")
        self.number = number

    @property
    def is_full(self):
        return False  # FIXME: implement
