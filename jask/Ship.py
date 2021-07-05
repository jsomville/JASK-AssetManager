 #!/usr/bin/env python3
from enum import IntEnum
import pygame

class ShipClass(IntEnum):
    NONE = 0
    FIGHTER = 1
    HAULER = 2
    FREIGHTER = 3
    CARRIER = 4

class Ship(pygame.sprite.Sprite):

    def __init__(self, name, type, img, shield_max, shield_regen, speed_max, damage_min, damage_max):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.type = type 

        #Properties
        self.shield_max = shield_max
        self.shield_regen = shield_regen
        self.speed_max = speed_max
        self.damage_min = damage_min
        self.damage_max = damage_max

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()

        #Ship Default Values
        self.shield = self.shield_max
        self.angle = 0
        self.speed = 0
        self.pos = (0,0)
    
    def update(self, pos, angle, speed, shield):
        self.rect.center = pos

        self.angle = angle
        self.speed = speed
        self.shield = shield
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


