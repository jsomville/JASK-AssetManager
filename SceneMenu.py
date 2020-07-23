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
        lbl["type"] = MenuObjectType.LABEL
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
        if event.type == pygame.MOUSEBUTTONUP:
            for control in self.menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["mouse_down"]:
                        # This is a click
                        control["mouse_down"] = False

                        if control["name"] == "btnQuit":
                            self.next = None
                        else:
                            self.goto_scene(control)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for control in self.menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["rect"].collidepoint(event.pos):
                        control["mouse_down"] = True
                    else:
                        control["mouse_down"] = False
        elif event.type == pygame.MOUSEMOTION:
            for control in self.menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["rect"].collidepoint(event.pos):
                        control["hover"] = True
                        control["back_color"] = self.theme["btn_back_hover_color"]
                    else:
                        control["hover"] = False
                        control["mouse_down"] = False
                        control["back_color"] = self.theme["btn_back_color"]

    def goto_scene(self, control):
        if control["name"] == "btnShipObject":

            # Send Custom Event
            event_dict = dict()
            event_dict["goto"] = "ship"
            new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
            pygame.event.post(new_event)
        elif control["name"] == "btnCelestialObject":

            #************************************
            #Create Celestial Scene
            new_scene = SceneCelestial()
            new_scene.size = self.size
            new_scene.on_init()
            self.next = new_scene
            # ************************************

            event_dict = dict()
            event_dict["goto"] = "celestial"
            new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
            pygame.event.post(new_event)

    def on_loop(self):
        pass

    def on_render(self, surface):

        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.menu_util.draw_menu(surface, self.menu)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)


