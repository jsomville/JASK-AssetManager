import pygame
from pygame.locals import *

from pygame_framework.Util import Util
from pygame_framework.Colors import Colors

class ShipDash(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        #Load Dash Image
        img = "images/dash/dash.png"
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey(Colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.font = pygame.font.SysFont("Arial", 14)


    def set_ship(self, ship):
        self.ship = ship


    def set_map(self, map):
        self.map = map


    def draw(self, surface):
        #Draw the Dash
        surface.blit(self.image, self.rect)

        #Draw Shield
        self.draw_shield(surface)

        #Draw Speed
        self.draw_speed(surface)

        #Draw Enable Weapon
        self.draw_weapon_enabled(surface)

        #Draw Radar
        self.draw_radar(surface)


    def draw_shield(self, surface):
        pourcent = self.ship.shield / self.ship.shield_max

        width = 100
        x = self.rect.centerx - width // 2
        y = self.rect.centery - 20
        on_color = Colors.BLUE
        off_color = Colors.RED
        step = 3
        self.draw_graph(surface, pourcent, x, y, width, on_color, off_color, step)


    def draw_speed(self, surface):
        pourcent = self.ship.speed / self.ship.speed_max
        width = 100
        x = self.rect.centerx - width // 2
        y = self.rect.centery - 50
        on_color = Colors.ORANGE
        off_color = Colors.DARK_GRAY
        step = 6
        self.draw_graph(surface, pourcent, x, y, width, on_color, off_color, step)


    def draw_graph(self, surface, pour, x, y, width, on_color, off_color, step):
         #Handle shield
        height = 14
        spacer = 2
        double_spacer = 2 * spacer
        
        shield_base_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, Colors.GRAY, shield_base_rect)

        shield_red_rect = pygame.Rect(x + spacer, y + spacer, width - double_spacer, height - double_spacer)
        pygame.draw.rect(surface, off_color, shield_red_rect)

        #Get the Shield slider width from shild and shield max
        #width = int(self.ship.shield * (width - double_spacer)) // self.ship.shield_max
        g_width = int(pour * (width - double_spacer))
        shield_rect = pygame.Rect(x + spacer, y + spacer, g_width, height - double_spacer)
        pygame.draw.rect(surface, on_color, shield_rect)

        #Draw separators
        inc = (width - double_spacer) // (step)
        for i in range(1,step):
            start_pos = (int((x + spacer) + i * inc), y + spacer)
            end_pos = (int((x + spacer) + i * inc), y + height - double_spacer)

            pygame.draw.line(surface, Colors.GRAY, start_pos, end_pos, width=2)


    def draw_weapon_enabled(self, surface):
        x = self.rect.centerx + 100
        y = self.rect.centery - 60
        radius = 5
        on_color = Colors.RED
        off_color = Colors.TEAL
        bg_color = Colors.DARK_GRAY

        center = (x,y)
        color = bg_color
        pygame.draw.circle(surface, color, center, radius + 2)
        color = off_color
        if self.ship.enable_weapon:
            color = on_color

        pygame.draw.circle(surface, color, center, radius)

        text_x = x - 4
        text_y = y + radius * 2 + 1
        Util().draw_text(surface, "E", self.font, Colors.WHITE, text_x, text_y)


    def draw_radar(self, surface):
        x = self.rect.centerx - 140
        y = self.rect.centery - 10
        width = 104
        height = 104
        radar_surface = pygame.Surface((width, height))
        rect = radar_surface.get_rect()

        #Draw radar background
        pygame.draw.rect(radar_surface, Colors.DARK_GRAY, rect, width=2, border_radius = 8)

        self.map.draw_small_map(radar_surface)
        rect.center = (x,y)
        surface.blit(radar_surface, rect)



