#!/usr/bin/env python3
from datetime import datetime

import pygame
from pygame.locals import *

import pygame_framework
from pygame_framework.Scene import Scene
from pygame_framework.Colors import Colors


class SceneSplash(Scene):
    name = "splash"

    rect_list = list()
    exit = False
    splash_timeout = None
    DISPLAY_TIME = 1 #in seconds

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        #Set the background color
        self.BACKGROUND = Colors.BLACK

        #If font is not installed, use another one
        self.myFont = pygame.font.SysFont('Helvetica', 20)

        #Load Images
        self.image = pygame.image.load("images/jask.png").convert_alpha()

    def on_init(self):
        pass

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #Click on logo --> exit flag
                rect = self.image.get_rect()
                rect.center = self.center
                if rect.collidepoint(event.pos):
                    self.exit = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    def on_loop(self):

        if self.splash_timeout is None:
            self.splash_timeout = datetime.now().timestamp() + self.DISPLAY_TIME
        else:
            if datetime.now().timestamp() > self.splash_timeout:
                self.exit = True

        #Handle end of scene
        if self.exit:
            self.next = None

    def on_render(self, surface):
        #Fill Background color
        surface.fill(self.BACKGROUND)

        #Draw image at center screen
        img = self.image
        rect = img.get_rect()
        rect.center = self.center
        surface.blit(self.image, rect)

        yoffset = 120
        yincrement = 30
        text_color = Colors.WHITE

        #Draw pygame version
        version = 'Version : ' + str(pygame.version.ver)
        text_surface = self.myFont.render(version, False, text_color)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0]//2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        #Draw Celestial Object Library Version
        yoffset += yincrement
        version = 'CelestialObjectLibrary.json'
        text_surface = self.myFont.render(version, False, text_color)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        # Draw System Map Version
        yoffset += yincrement
        version = 'SystemMap.json'
        text_surface = self.myFont.render(version, False, text_color)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        # Draw Ship Library Version
        yoffset += yincrement
        version = 'ShipLibrary.json'
        text_surface = self.myFont.render(version, False, text_color)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)
		