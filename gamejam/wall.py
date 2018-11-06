#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Element


class Wall(Element):
    def __init__(self, x, y, w, h, name, hitbox=None):
        Element.__init__(self, x, y, w, h, hitbox)

        self.get_sprite("wall_%s" % name)
