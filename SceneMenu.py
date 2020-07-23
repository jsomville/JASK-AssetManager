#!/usr/bin/env python3
from enum import IntEnum

import pygame
from pygame.locals import *

from Colors import Colors
from Scene import Scene

class MenuObjectType(IntEnum):
    LABEL = 1
    BUTTON = 2

class MenuVOrientation(IntEnum):
    TOP = 1
    CENTER = 2
    BOTTOM = 3

class MenuHOrientation(IntEnum):
    LEFT = 3
    CENTER = 4
    RIGHT = 5

class SceneMenu(Scene):
    name = "menu"
    menu = list()
    menu_theme = dict()
    inited = False
    v_orientation = MenuVOrientation.TOP
    h_orientation = MenuHOrientation.CENTER

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        self.BACKGROUND = Colors.BLACK

        #Menu definition
        lbl = dict()
        lbl["name"] = "lblMenu"
        lbl["type"] = MenuObjectType.LABEL
        lbl["text"] = "Menu"
        lbl["heading"] = 1
        self.menu.append(lbl)

        btn = dict()
        btn["name"] = "btnCelestialObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Celestial Object"
        btn["heading"] = 2
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnShipObject"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Ship Object"
        btn["heading"] = 2
        self.menu.append(btn)

        btn = dict()
        btn["name"] = "btnQuit"
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = "Quit"
        btn["heading"] = 2
        self.menu.append(btn)

        #Style
        self.menu_theme["base_size"] = (200, 40)
        self.menu_theme["space"] = 10
        self.menu_theme["font"] = 'Comic Sans MS'

        self.menu_theme["heading"] = dict()
        self.menu_theme["heading"][1] = 30
        self.menu_theme["heading"][2] = 25
        self.menu_theme["heading"][3] = 20

        self.menu_theme["btn_back_color"] = Colors.DARK_GRAY
        self.menu_theme["btn_back_hover_color"] = Colors.LIGHT_GRAY
        self.menu_theme["btn_text_color"] = Colors.WHITE

        self.menu_theme["lbl_back_color"] = Colors.DARK_GRAY
        self.menu_theme["lbl_text_color"] = Colors.ORANGE

        # If font is not installed, use another one
        self.myFont = pygame.font.SysFont(self.menu_theme["font"], 30)

    def on_init(self):
        menu_height = len(self.menu) * self.menu_theme["base_size"][1]
        if self.v_orientation == MenuVOrientation.TOP:
            y_start = 0
        elif self.v_orientation == MenuVOrientation.CENTER:
            y_start = self.center[1] - menu_height//2
        elif self.v_orientation == MenuVOrientation.BOTTOM:
            y_start = self.height - menu_height

        if self.h_orientation == MenuHOrientation.LEFT:
            x_start = 0
        if self.h_orientation == MenuHOrientation.CENTER:
            x_start = self.center[0] - self.menu_theme["base_size"][0] // 2
        if self.h_orientation == MenuHOrientation.RIGHT:
            x_start = self.width - self.menu_theme["base_size"][0]



        #x_value = self.center[0] - self.menu_theme["base_size"][0] // 2
        #y_start = self.center[1] - 100 # for now
        y_value = y_start
        x_value = x_start
        for control in self.menu:
            #Control Position
            control["rect"] = pygame.Rect((x_value, y_value), self.menu_theme["base_size"])

            if control["type"] == MenuObjectType.LABEL:
                control["back_color"] = self.menu_theme["lbl_back_color"]
                control["text_color"] = self.menu_theme["lbl_text_color"]
            elif control["type"] == MenuObjectType.BUTTON:
                control["back_color"] = self.menu_theme["btn_back_color"]
                control["text_color"] = self.menu_theme["btn_text_color"]
                control["mouse_down"] = False

            y_value += self.menu_theme["base_size"][1] + 4

            print (control["rect"])

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
                        control["back_color"] = self.menu_theme["btn_back_hover_color"]
                    else:
                        control["hover"] = False
                        control["mouse_down"] = False
                        control["back_color"] = self.menu_theme["btn_back_color"]

    def goto_scene(self, control):
        if control["name"] == "btnShipObject":
            # Send Custom Event
            event_dict = dict()
            event_dict["goto"] = "ship"
            new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
            pygame.event.post(new_event)
        elif control["name"] == "btnCelestialObject":
            event_dict = dict()
            event_dict["goto"] = "celestial"
            new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
            pygame.event.post(new_event)

    def on_loop(self):
        pass

    def on_render(self, surface):

        # Fill Background color
        surface.fill(self.BACKGROUND)

        self.draw_menu(surface)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)

    def draw_menu(self, surface):
        for control in self.menu:

            # Handle Click
            control_center = control["rect"].center
            if control["type"] == MenuObjectType.BUTTON:
                if control["mouse_down"]:
                    control_center = (control_center[0] +2, control_center[1] + 2 )

            # Draw background
            pygame.draw.rect(surface, control["back_color"], control["rect"])
            #print (control["rect"])

            # Draw Text
            text = control["text"]
            text_surface = self.myFont.render(text, False, control["text_color"])
            #text_size = self.myFont.size(text)
            #text_rect = self.centerx - text_size[0] // 2, self.centery + 30
            text_rect = text_surface.get_rect()
            text_rect.center = control_center
            surface.blit(text_surface, text_rect)
