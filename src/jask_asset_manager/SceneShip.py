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

from .jask.LibraryManager import LibraryManager
from .jask.ShipDash import ShipDash

class SceneShip(Scene):
    
    def __init__(self):
        Scene.__init__(self)

        self.BACKGROUND = Colors.BLACK
        self.name = "ship"
        self.menu = list()
        self.v_orientation = MenuVOrientation.TOP
        self.h_orientation = MenuHOrientation.RIGHT
        self.theme = MenuTheme()
        self.menu_util = MenuUtil()

        self.ship = None
        self.ship_dash = None

        # Menu definition
        lbl = dict()
        lbl["name"] = "lblMenu"
        lbl["type"] = MenuObjectType.TITLE
        lbl["text"] = "Ship"
        self.menu.append(lbl)

        lbl = dict()
        lbl["name"] = "lblItem"
        lbl["type"] = MenuObjectType.LABEL
        lbl["text"] = "Title Here "
        self.menu.append(lbl)
        self.item = lbl

        btn = dict()
        btn["name"] = "N/A"
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

        #Library and Objects
        self.library = LibraryManager().ships
        self.map = LibraryManager().map
        

    def on_init(self):
        self.menu_util.on_init(self.size, self.menu, self.v_orientation, self.h_orientation)

        self.inited = True

        #Select first ship
        self.index = 0
        self.load_ship()

        self.ship

    def on_event(self, event):
        self.menu_util.on_event(event, self.menu)

        if event.type == pygame.KEYDOWN:
            if self.ship != None :
                if event.key == pygame.K_UP:
                    self.ship.power_up()
                if event.key == pygame.K_DOWN:
                    self.ship.power_down()
                if event.key == pygame.K_e:
                    self.ship.toggle_weapon()
                if event.key == pygame.K_m:
                    print("M key --> messile | mine")
                if event.key == pygame.K_b:
                    self.ship.brake()
                if event.key == pygame.K_l:
                    print("L Key --> land")

    def on_loop(self):
        for control in self.menu:
            if control["type"] == MenuObjectType.BUTTON:
                if control["click"]:
                    control["click"] = False
                    if control["name"] == "btnClose":
                        self.fire_goto_event("menu")

                    elif control["name"] == "btnNext":
                        self.index += 1
                        if self.index >= len(self.library):
                            self.index = 0
                        self.load_ship()

                    elif control["name"] == "btnPrevious":
                        self.index -= 1
                        if self.index < 0:
                            self.index = len(self.library) - 1
                        self.load_ship()

        #Handle ship rotation
        if self.ship != None :
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.ship.turn_left()
            if keys[K_RIGHT]:
                self.ship.turn_right()
            if keys[K_SPACE]:
                self.ship.shoot()

            self.ship.on_loop()


    def on_render(self, surface):
        # Fill Background color
        surface.fill(self.BACKGROUND)

        #Draw Map
        self.map.draw(surface)

        #Draw Menu
        self.menu_util.draw_menu(surface, self.menu)

        #Draw Ship
        if self.ship != None:
            #print("draw ship")
            self.ship.draw(surface)

        #Draw Dash
        if self.ship_dash != None:
            self.ship_dash.draw(surface)


    def load_ship(self):
        #Load Ship
        self.ship = self.library[self.index]
        
        self.item["text"] = self.ship.name

        #At center screen 
        centerx = self.size[0] // 2
        centery = self.size[1] // 2

        #reset ship values
        angle = 0
        speed = 0
        shield = 0 #self.ship.shield_max
        self.ship.update((centerx, centery), angle, speed, shield)

        if self.ship_dash == None:
            dash_centery = self.size[1] - 100 #ship dash 
            self.ship_dash = ShipDash(centerx, dash_centery)

        #Ship starting position on map
        x = 50
        y = 50
        self.ship.x = x
        self.ship.y = y

        #Set dash references
        self.map.set_ship(self.ship)
        self.ship_dash.set_ship(self.ship)
        self.ship_dash.set_map(self.map)



