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
        self.y = y
        self.type = type
        self.angle = angle
        self.rad_angle = (self.angle / 360) * MathUtil.TWO_PI

        self.posix = x
        self.posiy = y
        self.startx = x
        self.starty = y
        self.distance = 0

        #To improve
        self.speed = 2
        self.max_dist = 300

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
        #Get the distance made by projectile
        self.distance = math.sqrt( (self.x - self.startx)**2 + (self.y - self.starty)**2 )

        #To have a decimal calculation of the position (a small angle dosent move)
        self.posix = self.posix - math.sin(self.rad_angle) * self.speed
        self.posiy = self.posiy - math.cos(self.rad_angle) * self.speed

        self.x = int(self.posix)
        self.y = int(self.posiy)

        self.rect.center = (self.x, self.y)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



