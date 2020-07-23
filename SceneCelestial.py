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
        lbl["type"] = MenuObjectType.LABEL
        lbl["text"] = "Celestials"
        self.menu.append(lbl)

        btn = dict()
        btn["name"] = "btnClose"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Close"
        self.menu.append(btn)

    def on_init(self):
        self.menu_util.on_init(self.menu)

        menu_pos = self.menu_util.get_menu_position(self.size, len(self.menu), self.v_orientation, self.h_orientation)

        x_value = menu_pos[0]
        y_value = menu_pos[1]

        for control in self.menu:
            #Control Position
            control["rect"] = pygame.Rect((x_value, y_value), self.theme["base_size"])

            if control["type"] == MenuObjectType.LABEL:
                control["back_color"] = self.theme["lbl_back_color"]
                control["text_color"] = self.theme["lbl_text_color"]
            elif control["type"] == MenuObjectType.BUTTON:
                control["back_color"] = self.theme["btn_back_color"]
                control["text_color"] = self.theme["btn_text_color"]
                control["mouse_down"] = False

            y_value += self.theme["base_size"][1] + 4

        self.inited = True

    def on_event(self, event):
        pass

    def on_loop(self):
        pass

    def on_render(self, surface):
        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.draw_image(surface)
        self.menu_util.draw_menu(surface, self.menu)

        # Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)

    def draw_image(self, surface):
        pass

