#!/usr/bin/env python3
from enum import IntEnum
import pygame

class AsteroidType(IntEnum):
    NONE = 0
    ROCK = 1
    METAL = 2
    GOLD = 3
    IRON = 4
    LEAD = 5
    SILICON = 6
    SILVER = 7
    TITANIUM = 8
    YOTTRITE = 9


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, name, type, img, min, max):
        self.name = name
        self.type = type
        self.min = min
        self.max = max

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()
    
    def update(self, pos):
        self.rect.center = pos
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

