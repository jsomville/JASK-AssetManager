#!/usr/bin/env python3

import pygame
from pygame.locals import *

from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation
from pygame_framework.MenuObjectType import MenuObjectType
from pygame_framework.MenuTheme import MenuTheme


class MenuUtil:
    BASE_MENU_OFFSET = 4
    TITLE_BAR_HEIGHT = 5

    def __init__(self):

        self.theme = MenuTheme()

        self.myFont = pygame.font.SysFont(self.theme["font"], 30)


    def get_menu_position(self, window_size, menu_control_count, v_orientation, h_orientation):

        control_width = self.theme["base_size"][0]
        control_height = self.theme["base_size"][1]

        menu_height = menu_control_count * control_height
        center_x = window_size[0]//2
        center_y = window_size[1]//2

        y_start = 0
        if v_orientation == MenuVOrientation.TOP:
            y_start = 0
        elif v_orientation == MenuVOrientation.CENTER:
            y_start = center_y - menu_height // 2
        elif v_orientation == MenuVOrientation.BOTTOM:
            y_start = window_size[1] - menu_height - MenuUtil.BASE_MENU_OFFSET  # 20 for space of Title Bar

        x_start = 0
        if h_orientation == MenuHOrientation.LEFT:
            x_start = MenuUtil.BASE_MENU_OFFSET
        if h_orientation == MenuHOrientation.CENTER:
            x_start = center_x - control_width // 2
        if h_orientation == MenuHOrientation.RIGHT:
            x_start = window_size[0] - control_width

        return x_start, y_start

    def on_init(self, menu):
        pass

    def draw_menu(self, surface, menu):
        for control in menu:

            # Handle Click
            control_center = control["rect"].center
            if control["type"] == MenuObjectType.BUTTON:
                if control["mouse_down"]:
                    control_center = (control_center[0] + 2, control_center[1] + 2)

            # Draw background
            pygame.draw.rect(surface, control["back_color"], control["rect"])

            # Draw Text
            text = control["text"]
            text_surface = self.myFont.render(text, False, control["text_color"])
            text_rect = text_surface.get_rect()
            text_rect.center = control_center
            surface.blit(text_surface, text_rect)
