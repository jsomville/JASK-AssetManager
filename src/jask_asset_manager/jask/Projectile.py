from enum import IntEnum
import pygame
from pygame.locals import *

class ProjectileType(IntEnum):
    ION_BOLT = 0

class Projectile(pygame.sprite.Sprite):
    def __init__(self, type, x, y, angle):
        self.x = x
        self.y = y
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

        self.image = self.projectile[ProjectileType.ION_BOLT][0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def on_loop(self):
        self.life += 1

        #To refine
        self.y = self.y - self.speed
        self.rect.center = (self.x, self.y)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



