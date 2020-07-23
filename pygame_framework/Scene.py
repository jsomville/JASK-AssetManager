#!/usr/bin/env python3
import pygame
from pygame.locals import *


class Scene(pygame.Rect):
    """This scene class is a pygame rectangle and can handle event, loop, render"""
    name = "default scene"

    def __init__(self):
        self.next = self

        print("Init " + self.name + " scene")

    def on_init(self):
        raise Exception('Scene on_init function needs to be override')

    def on_event(self, events):
        raise Exception('Scene on_event function needs to be override')

    def on_loop(self):
        raise Exception('Scene on_loop function needs to be override')

    def on_render(self, surface):
        raise Exception('Scene on_render function needs to be override')

    def switch_to_scene(self, next_scene):
        self.next = next_scene

