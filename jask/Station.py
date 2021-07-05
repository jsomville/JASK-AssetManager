#!/usr/bin/env python3
import pygame

class Station(pygame.sprite.Sprite):

    def __init__(self, name, img):
        self.name = name

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()
    
    def update(self, pos):
        self.rect.center = pos
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
