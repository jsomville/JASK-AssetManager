#!/usr/bin/env python3
from enum import Enum
from datetime import datetime

import pygame
from pygame.locals import *

from pygame_framework.MenuTheme import MenuTheme
from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation
from pygame_framework.Colors import Colors

from .jask.LibraryManager import LibraryManager

from .SceneSplash import SceneSplash
from .SceneMenu import SceneMenu
from .SceneAsteroid import SceneAsteroid
from .SceneShip import SceneShip
from .ScenePlanet import ScenePlanet
from .SceneStar import SceneStar
from .SceneStation import SceneStation
from .SceneMonster import SceneMonster

class App:
    FPS = 60

    # Handle scenes
    scenes = dict()
    active_scene = None

    theme = MenuTheme()

    v_orientation = MenuVOrientation.CENTER
    h_orientation = MenuHOrientation.RIGHT

    def __init__(self):
        """ App object initialization function, here you set variables default values"""
        self._running = True
        self._display_surf = None
        self.image = None

        self.clock =  pygame.time.Clock()


    def on_init(self):
        """Game initialisation function, here you load scenes, images, sounds, etc."""

        full_size = (self.theme["window_width"], self.theme["window_height"])

        # pygame initialisation
        pygame.init()
        self._display_surf = pygame.display.set_mode(full_size)

        # Set the window caption
        pygame.display.set_caption("JASK - Asset Manager")

        # Load scenes
        #***************************************************
        new_scene = SceneSplash()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["splash"] = new_scene

        new_scene = SceneMenu()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["menu"] = new_scene

        new_scene = SceneShip()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["ship"] = new_scene

        new_scene = SceneAsteroid()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["asteroid"] = new_scene

        new_scene = ScenePlanet()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["planet"] = new_scene

        new_scene = SceneStar()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["star"] = new_scene

        new_scene = SceneMonster()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["monster"] = new_scene

        new_scene = SceneStation()
        new_scene.size = full_size
        new_scene.on_init()
        self.scenes["station"] = new_scene
        # ***************************************************

        #Display First Scene
        self.active_scene = self.scenes["splash"]

        self.debug_font = pygame.font.SysFont("Arial", 14)

        #Load Library Content
        lm = LibraryManager()

    def on_event(self, event):
        """Function designed to hanlde events such as user input (keyboard, mouse, etc"""

        # Quit Event
        if event.type == pygame.QUIT:
            print ("Event Quit")
            self._running = False
        elif event.type == pygame.USEREVENT:
            #Switch scene event
            if "goto" in event.__dict__:
                # Scene on_event
                print("Goto : " + event.__dict__["goto"])

                if event.__dict__["goto"] in self.scenes:
                    self.active_scene = self.scenes[event.__dict__["goto"]]
                else:
                    raise Exception('Scene' + event.__dict__["goto"] + " not found")

        #Event on active Scene
        if self.active_scene is not None:
            self.active_scene.on_event(event)

    def on_loop(self):
        """Function to specify the game logic"""

        # Scene on_loop
        if self.active_scene is not None:
            self.active_scene.on_loop()

            #Active scene is cleared
            if self.active_scene.next is None:
                print(self.active_scene.name)
                #Handle splash to menu
                if self.active_scene.name == "splash":
                    print("Switch to Menu Scene")
                    self.active_scene = self.scenes["menu"]

            self.active_scene = self.active_scene.next

            #Quit application if no more active scenes
            if self.active_scene is None:
                print ("quit app, no more scene to render")
                self._running = False

    def on_render(self):
        """Function specialized for surface rendering only"""

        # Scene on_render
        if self.active_scene is not None:
            self.active_scene.on_render(self._display_surf)

        #Display actual FPS
        text = str(int(self.clock.get_fps()))
        self.draw_text(text, self.debug_font, Colors.WHITE, 100, 100)
    
    def draw_text(self, text, font, text_col, x, y):
        """Draw Text Function"""
        img = font.render(text, True, text_col)
        self._display_surf.blit(img, (x, y))


    def on_cleanup(self):
        """Function to handle app uninitialized"""
        pygame.quit()

    def on_execute(self):
        """Main Execute function and main loop, calls on_init, on_event, on_loop, on_logic  """
        # Init application
        self.on_init()

        # Main Loop
        while self._running:
            # Handle Events
            for event in pygame.event.get():
                self.on_event(event)

            # Game Logic
            self.on_loop()

            # Render code
            self.on_render()

            #Ensure FPS is respected
            self.clock.tick(self.FPS)

        self.on_cleanup()
