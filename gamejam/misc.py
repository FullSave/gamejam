#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file is part of FullSave Gamejam.
Copyrights 2018 by Fullsave
"""

import os

import pyxel

SPRITESHEET_IMAGE = 0


class SpriteSheet(object):
    """ A singleton class that handles sprites
    """
    _sprites = {}

    def __new__(cls):
        """ Singleton.
        """
        try:
            return cls._inst
        except AttributeError:
            cls._inst = super(SpriteSheet, cls).__new__(cls)
            cls._inst.initialized = False
            return cls._inst

    def __init__(self):
        """Initialise the instance.
        """
        if self.initialized:
            return

        assets = os.path.join(os.path.dirname(__file__), 'assets')
        pyxel.image(SPRITESHEET_IMAGE).load(
                0, 0, os.path.join(assets, 'spritesheet.png'))

        self.initialized = True

    def add_sprite(self, name, sprite):
        self._sprites[name] = sprite

    def get_sprite(self, name):
        return self._sprites[name]

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError as exc:
            raise KeyError(exc.message)

    def __setitem__(self, key, value):
        try:
            setattr(self, key, value)
        except AttributeError as exc:
            raise KeyError(exc.message)

    def __delitem__(self, key):
        try:
            delattr(self, key)
        except AttributeError as exc:
            raise KeyError(exc.message)


class Sprite(object):
    def __init__(self, x, y, w, h, mask):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._mask = mask

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def w(self):
        return self._w
    
    @property
    def h(self):
        return self._h

    def render(self):
        return SPRITESHEET_IMAGE, self._x, self._y, \
                self._w, self._h, self._mask


class Hitbox(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def x2(self):
        return self.x + self.w

    @property
    def y2(self):
        return self.y + self.h


class Item(object):
    sprite = None

    def get_sprite(self, name):
        self.sprite = SpriteSheet().get_sprite(name)

    def copy(self):
        # Return a copy of this element to predict movements
        return Item(self.sprite)

    def draw(self, x, y, offset_x=0, offset_y=0):
        # Drawn the sprite at the element coords
        pyxel.blt(x + offset_x, y + offset_y, *self.sprite.render())


class Element(Item):
    def __init__(self, x, y, w, h):
        """Basic Game Element

        Arguments:
            * x, y, w, h: x, y, width, height
            * spritesheet: a SpriteSheet object
            * sx, sy: the coords, in multiple of w and h in the spritesheet
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # The element hitbox
        self.hitbox = Hitbox(x, y, w, h)

    def draw(self, offset_x=0, offset_y=0):
        Item.draw(self, self.x, self.y, offset_x, offset_y)

    def copy(self):
        # Return a copy of this element to predict movements
        return Element(self.x, self.y, self.w, self.h)

    def is_colliding(self, element):
        # Is this element colliding with element
        return self.hitbox.x < element.hitbox.x2 and \
               self.hitbox.x2 > element.hitbox.x and \
               self.hitbox.y < element.hitbox.y2 and \
               self.hitbox.y2 > element.hitbox.y
