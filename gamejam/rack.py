#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

from .misc import Item


class Rack(Item):
    def __init__(self):
        self.get_sprite("rack0")
