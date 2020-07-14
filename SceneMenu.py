import pygame
from pygame.locals import *

from Colors import Colors
from Scene import Scene

class SceneMenu(Scene):
    name = "menu"

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        self.BACKGROUND = Colors.BLACK

        # If font is not installed, use another one
        self.myFont = pygame.font.SysFont('Comic Sans MS', 30)

    def on_event(self, events):
        pass

    def on_loop(self):
        pass

    def on_render(self, surface):

        # Fill Background color
        surface.fill(self.BACKGROUND)

        # Draw Menu
        version = "MENU"
        text_surface = self.myFont.render(version, False, Colors.WHITE)
        text_size = self.myFont.size(version)
        text_position = self.centerx - text_size[0] // 2, self.centery + 30
        surface.blit(text_surface, text_position)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)