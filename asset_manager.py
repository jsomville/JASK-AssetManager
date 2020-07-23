#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
import pygame
from pygame.locals import *

from pygame_framework.MenuTheme import MenuTheme
from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation

from SceneSplash import SceneSplash
from SceneMenu import SceneMenu
from LibraryManager import LibraryManager


class App:
    FPS = 35

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
        self.frame_per_sec = None


    def on_init(self):
        """Game initialisation function, here you load scenes, images, sounds, etc."""

        full_size = (self.theme["window_width"], self.theme["window_height"])

        # pygame initialisation
        pygame.init()
        self._display_surf = pygame.display.set_mode(full_size)
        self.frame_per_sec = pygame.time.Clock()

        # Set the window caption
        pygame.display.set_caption("Advanced template for a pygame application")

        # Load scenes
        scene_splash = SceneSplash()
        scene_splash.size = full_size
        scene_splash.on_init()
        self.scenes["splash"] = scene_splash

        scene_menu = SceneMenu()
        scene_menu.size = full_size
        scene_menu.on_init()
        self.scenes["menu"] = scene_menu

        #Display First Scene
        self.active_scene = scene_splash

        #TEMP
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

            self.frame_per_sec.tick(self.FPS)

        self.on_cleanup()


if __name__ == "__main__":
    """Program entry function"""
    theApp = App()
    theApp.on_execute()
