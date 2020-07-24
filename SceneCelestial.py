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

from LibraryManager import LibraryManager

class SceneCelestial(Scene):
    name = "celestial"
    menu = list()

    v_orientation = MenuVOrientation.TOP
    h_orientation = MenuHOrientation.RIGHT

    def __init__(self):
        Scene.__init__(self)

        self.BACKGROUND = Colors.BLACK

        self.theme = MenuTheme()
        self.menu_util = MenuUtil()

        # Menu definition
        lbl = dict()
        lbl["name"] = "lblMenu"
        lbl["type"] = MenuObjectType.TITLE
        lbl["text"] = "Celestial"
        self.menu.append(lbl)

        lbl = dict()
        lbl["name"] = "lblItem"
        lbl["type"] = MenuObjectType.LABEL
        lbl["text"] = "Celestial"
        self.menu.append(lbl)
        self.item = lbl

        btn = dict()
        btn["name"] = "container1"
        btn["type"] = MenuObjectType.CONTAINER
        btn["content"] = list()

        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnNext"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Next"
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnPrevious"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Previous"
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnClose"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Close"
        self.menu.append(btn)

        self.library = LibraryManager()
        self.index = 0
        self.update_object()

    def on_init(self):
        self.menu_util.on_init(self.size, self.menu, self.v_orientation, self.h_orientation)

        self.inited = True

    def on_event(self, event):
        self.menu_util.on_event(event, self.menu)

    def on_loop(self):
        for control in self.menu:
            if control["type"] == MenuObjectType.BUTTON:
                if control["click"]:
                    control["click"] = False
                    if control["name"] == "btnClose":
                        self.fire_goto_event("menu")

                    elif control["name"] == "btnNext":
                        self.index += 1
                        if self.index >= len(self.library.celestialsObjectsLibrary.celestialObjectList):
                            self.index = 0
                        self.update_object()

                    elif control["name"] == "btnPrevious":
                        self.index -= 1
                        if self.index < 0:
                            self.index = len(self.library.celestialsObjectsLibrary.celestialObjectList) - 1
                        self.update_object()

    def on_render(self, surface):
        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.draw_image(surface)
        self.menu_util.draw_menu(surface, self.menu)

        # Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)

    def update_object(self):
        c_object = self.library.celestialsObjectsLibrary.celestialObjectList[self.index]
        self.item["text"] = c_object.name

        self.image = pygame.image.load(c_object.image).convert_alpha()

    def draw_image(self, surface):
        if self.image is not None:
            img = self.image
            rect = img.get_rect()
            rect.center = self.center
            surface.blit(self.image, rect)
