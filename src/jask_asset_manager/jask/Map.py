import math

import pygame
from pygame.locals import *

from pygame_framework.Util import Util
from pygame_framework.Colors import Colors

class Map:
    def __init__(self, id, name, width, height, elements):
        #Default
        self.id = id
        self.name = name
        self.width = int(width)
        self.height = int(height)
        self.tiles = dict()
        
        #Set all tiles
        for i in range(self.width):
            self.tiles[i] = dict()
            for j in range(self.height):
                self.tiles[i][j] = None

        for element in elements:
            self.tiles[element.x][element.y] = element


    def set_ship(self, ship):
        self.ship = ship


    def draw_small_map(self, surface):
        rect = surface.get_rect()
        inc_x = (rect.width)// self.width
        inc_y = (rect.height)// self.height

        #For each tile
        for i in range(self.width):
            for j in range(self.height):
                if self.tiles[i][j] != None:

                    radius = 4
                    x = i * inc_x + radius
                    y = j * inc_y + radius

                    color = Colors.GREEN #Change with color of planet

                    pygame.draw.circle(surface, color, (x,y), radius)

        #Draw current ship position
        color = Colors.BLUE
        rasius = 2
        pygame.draw.circle(surface, color, (self.ship.x, self.ship.y), radius)

        #Draw current direction
        dist = radius * 2
        dirx = self.ship.x - math.sin(self.ship.rad_angle) * dist
        diry = self.ship.y - math.cos(self.ship.rad_angle) * dist
        pygame.draw.line(surface, color, (self.ship.x, self.ship.y), (dirx, diry), width = 2)


    def draw(self, surface):

        if self.width > 0 and self.height > 0:

            MAP_TO_SCREEN = 100
            screen_rect = surface.get_rect()
            width = screen_rect.width // MAP_TO_SCREEN
            height = screen_rect.height //MAP_TO_SCREEN

            offset_x = int(MAP_TO_SCREEN/2 + (int(self.ship.x) - self.ship.x) * MAP_TO_SCREEN)
            offset_x = int(MAP_TO_SCREEN/2 + (int(self.ship.y) - self.ship.y) * MAP_TO_SCREEN)
            for i in range(width):
                for j in range(height):
                    map_x = int(self.ship.x + i - width /2)
                    map_y = int(self.ship.y + j - height /2)
                    if map_x > 0 and map_x < self.width and map_y > 0 and map_y < self.height:
                        if self.tiles[map_x][map_y] != None:
                            color = Colors.GRAY
                            radius = 100
                            x = int(offset_x + (i * MAP_TO_SCREEN) - radius/2)
                            y = int(offset_x + (j * MAP_TO_SCREEN) - radius/2)

                            #pygame.draw.circle(surface, color, (x,y), radius)

                            self.tiles[map_x][map_y].draw(surface, x, y)
