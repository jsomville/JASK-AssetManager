#!/usr/bin/env python3

import pygame
from pygame.locals import *

from pygame_framework.Scene import Scene
from pygame_framework.Colors import Colors
from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation
from pygame_framework.MenuTheme import MenuTheme
from pygame_framework.MenuUtil import MenuUtil
from pygame_framework.MenuObjectType import MenuObjectType

from SceneCelestial import SceneCelestial


class SceneMenu(Scene):
    name = "menu"
    menu = list()

    v_orientation = MenuVOrientation.CENTER
    h_orientation = MenuHOrientation.CENTER

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        self.BACKGROUND = Colors.BLACK

        self.theme = MenuTheme()
        self.menu_util = MenuUtil()

        #Menu definition
        lbl = dict()
        lbl["name"] = "lblMenu"
        lbl["type"] = MenuObjectType.TITLE
        lbl["text"] = "Menu"
        self.menu.append(lbl)

        btn = dict()
        btn["name"] = "btnCelestialObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Celestial Object"
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnShipObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Ship Object"
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnQuit"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Quit"
        self.menu.append(btn)

    def on_init(self):
        self.menu_util.on_init(self.size, self.menu, self.v_orientation, self.h_orientation)

        self.inited = True

    def on_event(self, event):
        #Handle menu specific events
        self.menu_util.on_event(event, self.menu)

    def on_loop(self):
        for control in self.menu:
            if control["type"] == MenuObjectType.BUTTON:
                if control["click"]:
                    if control["name"] == "btnQuit":
                        self.next = None

                    elif control["name"] == "btnShipObject":
                        self.fire_goto_event("ship")

                    elif control["name"] == "btnCelestialObject":
                        self.fire_goto_event("celestial")

                    #Clear Click Event
                    control["click"] = False

    def on_render(self, surface):

        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.menu_util.draw_menu(surface, self.menu)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)


