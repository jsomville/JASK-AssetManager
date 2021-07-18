from enum import IntEnum
import math

import pygame
from pygame.locals import *
from .MathUtil import MathUtil

class ProjectileType(IntEnum):
    ION_BOLT = 0

class Projectile(pygame.sprite.Sprite):
    def __init__(self, type, x, y, angle):
        self.x = x
        self.posix = x
        self.y = y
        self.posiy = y
        self.angle = angle
        self.type = type

        self.speed = 2

        self.life = 1
        self.life_max = 60

        #Load Images
        self.projectile = dict()
        self.projectile[ProjectileType.ION_BOLT] = list()

        img = "images/effects/ion bolt/ion bolt0.png"
        image = pygame.image.load(img).convert_alpha()
        self.projectile[ProjectileType.ION_BOLT].append(image)

        img = "images/effects/ion bolt/ion bolt1.png"
        image = pygame.image.load(img).convert_alpha()
        self.projectile[ProjectileType.ION_BOLT].append(image)

        img = "images/effects/ion bolt/ion bolt2.png"
        image = pygame.image.load(img).convert_alpha()
        self.projectile[ProjectileType.ION_BOLT].append(image)

        img = "images/effects/ion bolt/ion bolt3.png"
        image = pygame.image.load(img).convert_alpha()
        self.projectile[ProjectileType.ION_BOLT].append(image)

        img = self.projectile[ProjectileType.ION_BOLT][0]

        self.image = pygame.transform.rotozoom(img, self.angle, 1)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def on_loop(self):
        self.life += 1
        
        rad_angle = (self.angle / 360) * MathUtil.TWO_PI

        self.posix = self.posix - math.sin(rad_angle) * self.speed
        self.posiy = self.posiy - math.cos(rad_angle) * self.speed

        self.x = int(self.posix)
        self.y = int(self.posiy)

        self.rect.center = (self.x, self.y)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



