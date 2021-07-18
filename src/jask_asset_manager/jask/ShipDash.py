import pygame
from pygame.locals import *

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


    def set_ship(self, ship):
        self.ship = ship

    def draw(self, surface):
        #Draw the Dash
        surface.blit(self.image, self.rect)

        #Draw Shield
        self.draw_shield(surface)

        #Draw Speed
        self.draw_speed(surface)

    def backup_draw_shield(self, surface):
         #Handle shield
        self.shield_height = 14
        self.shield_spacer = 2
        self.shield_double_spacer = 2 * self.shield_spacer
        shield_width = 100

        left = self.rect.centerx - shield_width // 2
        top = self.rect.centery - 20

        shield_base_rect = pygame.Rect(left, top, shield_width, self.shield_height)
        pygame.draw.rect(surface, Colors.GRAY, shield_base_rect)

        shield_red_rect = pygame.Rect(left + self.shield_spacer, top + self.shield_spacer, shield_width - self.shield_double_spacer, self.shield_height - self.shield_double_spacer)
        pygame.draw.rect(surface, Colors.RED, shield_red_rect)

        #Get the Shield slider width from shild and shield max
        width = int(self.ship.shield * (shield_width - self.shield_double_spacer)) // self.ship.shield_max
        shield_rect = pygame.Rect(left + self.shield_spacer, top + self.shield_spacer, width, self.shield_height - self.shield_double_spacer)
        pygame.draw.rect(surface, Colors.BLUE, shield_rect)

        step = 6
        inc = (shield_width - self.shield_double_spacer) // (step)
        for i in range(1,step):
            start_pos = (int((left + self.shield_spacer) + i * inc), top + self.shield_spacer)
            end_pos = (int((left + self.shield_spacer) + i * inc), top + self.shield_height - self.shield_double_spacer)

            pygame.draw.line(surface, Colors.GRAY, start_pos, end_pos, width=2)

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

        
        inc = (width - double_spacer) // (step)
        for i in range(1,step):
            start_pos = (int((x + spacer) + i * inc), y + spacer)
            end_pos = (int((x + spacer) + i * inc), y + height - double_spacer)

            pygame.draw.line(surface, Colors.GRAY, start_pos, end_pos, width=2)

