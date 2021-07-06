#!/usr/bin/env python3
from enum import IntEnum
import pygame

class PlanetType(IntEnum):
    NONE = 0
    CLOUD = 1
    DESERT = 2
    DUST = 3
    EARTH = 4
    FOREST = 5
    GAS = 6
    ICE = 7
    LAVA = 8
    OCEAN = 9
    ROCK = 10

class Planet(pygame.sprite.Sprite):

    def __init__(self, name, type, img):
        self.name = name
        self.type = type

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()
    
    def update(self, pos):
        self.rect.center = pos
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
