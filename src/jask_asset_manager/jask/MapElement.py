import pygame
from pygame.locals import *

class MapElement:

    def __init__(self, properties):
        self.type = properties["type"]
        self.sub_type = properties["sub_type"]
        self.name = properties["name"]
        self.x = int(properties["x"])
        self.y = int(properties["y"])

        #*******************************************
        #Init image
        img = "images/planet/desert2.png"
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, surface, x, y):
        rect = self.rect
        rect.center = (x,y)

        surface.blit(self.image, rect)
        
      
