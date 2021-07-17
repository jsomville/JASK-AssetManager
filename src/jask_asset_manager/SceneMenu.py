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

class SceneMenu(Scene):
    

    def __init__(self):
        Scene.__init__(self)
        self.name = "menu"

        pygame.font.init()

        self.BACKGROUND = Colors.BLACK

        self.theme = MenuTheme()
        self.theme["btn_text_color"] = Colors.BLACK #dosent work
        self.menu_util = MenuUtil()

        self.menu = list()
        self.fast_menu = dict()

        #Menu definition
        lbl = dict()
        lbl["name"] = "lblMenu"
        lbl["type"] = MenuObjectType.TITLE
        lbl["text"] = "Menu"
        self.menu.append(lbl)
        
        btn = dict()
        btn["name"] = "btnShipObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Ships"
        btn["goto"] = "ship"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn

        btn = dict()
        btn["name"] = "btnAsteroidObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Asteroids"
        btn["goto"] = "asteroid"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn

        btn = dict()
        btn["name"] = "btnPlanetObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Planet"
        btn["goto"] = "planet"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn

        btn = dict()
        btn["name"] = "btnStarObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Star"
        btn["goto"] = "star"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn

        btn = dict()
        btn["name"] = "btnStationObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Station"
        btn["goto"] = "station"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn

        btn = dict()
        btn["name"] = "btnMonsterObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Monster"
        btn["goto"] = "monster"
        self.menu.append(btn)
        self.fast_menu[btn["name"]] = btn


        btn = dict()
        btn["name"] = "btnQuit"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Quit"
        self.menu.append(btn)

    def on_init(self):
        self.menu_util.on_init(self.size, self.menu, MenuVOrientation.CENTER, MenuHOrientation.CENTER)

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
                    else:
                        if control["name"] in self.fast_menu:
                            self.fire_goto_event(control["goto"])

                    #Clear Click Event
                    control["click"] = False

    def on_render(self, surface):

        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.menu_util.draw_menu(surface, self.menu)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)


