#!/usr/bin/env python3
from enum import IntEnum
import pygame

class StarType(IntEnum):
    NONE = 0
    A = 1
    B = 2
    F = 3
    G = 4

class Star(pygame.sprite.Sprite):

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
