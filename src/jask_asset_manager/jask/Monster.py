#!/usr/bin/env python3
import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, name, img, nb_sprites, shield_max, shield_regen, damage_min, damage_max):
        self.name = name
        self.type = type
        self.shield_max = shield_max
        self.shield_regen = shield_regen
        self.damage_min = damage_min
        self.damage_max = damage_max

        #Load image Sprites
        self.images = list()
        for i in range(nb_sprites):
            file = img + f"{self.name}{i}.png"
            image = pygame.image.load(file).convert_alpha()
            self.images.append(image)

        self.index = 0
        self.direction = 1
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.counter = 0
        self.counter_max = 3
    
    def update(self, pos):
        self.rect.center = pos

        self.counter += 1
        if self.counter >= self.counter_max:
            self.counter = 0

            self.index += self.direction
            if self.index >= len(self.images) -1:
                self.index = len(self.images) -1
                self.direction = -1
            elif self.index < 0:
                self.direction = 1
                self.index = 1

        self.image = self.images[self.index]
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

