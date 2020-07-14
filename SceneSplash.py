#!/usr/bin/env python3
import pygame
from pygame.locals import *

from Colors import Colors
from Scene import Scene
import random

class SceneSplash(Scene):
    name = "splash"

    rect_list = list()
    exit = False

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        #Set the background color
        self.BACKGROUND = Colors.BLACK

        #If font is not installed, use another one
        #self.myFont = pygame.font.SysFont('Comic Sans MS', 20)
        self.myFont = pygame.font.SysFont('Helvetica', 20)

        #Load Images
        self.image = pygame.image.load("jask.png").convert_alpha()

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
        #Draw pygame version
        version = 'Version : ' + str(pygame.version.ver)
        text_surface = self.myFont.render(version, False, Colors.WHITE)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0]//2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        #Draw Celestial Object Library Version
        yoffset += yincrement
        version = 'CelestialObjectLibrary.txt'
        text_surface = self.myFont.render(version, False, Colors.WHITE)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        # Draw System Map Version
        yoffset += yincrement
        version = 'SystemMap.txt'
        text_surface = self.myFont.render(version, False, Colors.WHITE)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        # Draw Ship Library Version
        yoffset += yincrement
        version = 'ShipLibrary.txt'
        text_surface = self.myFont.render(version, False, Colors.WHITE)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + yoffset
        surface.blit(text_surface, text_position)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)
		