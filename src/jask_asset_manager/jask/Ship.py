 #!/usr/bin/env python3
from enum import IntEnum
import pygame
from pygame.locals import *

from pygame_framework.Colors import Colors

class ShipClass(IntEnum):
    NONE = 0
    FIGHTER = 1
    HAULER = 2
    FREIGHTER = 3
    CARRIER = 4

class Ship(pygame.sprite.Sprite):

    def __init__(self, name, type, img, shield_max, shield_regen, speed_max, damage_min, damage_max):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.type = type 

        #Properties
        self.shield_max = shield_max
        self.shield_regen = shield_regen
        self.speed_max = speed_max
        self.damage_min = damage_min
        self.damage_max = damage_max

        print(f"shield : {self.shield_max}")

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()

        #Ship Default Values
        self.shield = self.shield_max
        self.angle = 0
        self.speed = 0
        self.pos = (0,0)

        #To improve
        self.angle_increment = 1
        self.speed_increment = 1
        self.scale = 1
        self.power_counter = 0
        self.power_counter_max = 5
        self.power_index = 0
        self.power_force = None
        self.power_offset =  8

        self.init_effects()
    
    def update(self, pos, angle, speed, shield):
        self.rect.center = pos

        self.angle = angle
        self.speed = speed
        self.shield = shield

        print(f"shield : {self.shield}")
    
    def draw(self, surface):
        #Handle Ship Transform
        cur_image = pygame.transform.rotozoom(self.image, self.angle, self.scale)
        rect = cur_image.get_rect()
        rect.center = self.rect.center
        surface.blit(cur_image, rect)

        self.draw_power(surface)

        self.draw_shield(surface)
       
    def draw_shield(self, surface):
         #Handle shield
        shield_height = 14
        shield_ship_offset = 300
        shield_spacer = 2
        shield_double_spacer = 2 * shield_spacer
        left = self.rect.left
        top = self.rect.bottom + shield_ship_offset

        shield_base_rect = pygame.Rect(left, top, self.rect.width, shield_height)
        pygame.draw.rect(surface, Colors.GRAY, shield_base_rect)

        shield_red_rect = pygame.Rect(left + shield_spacer, top + shield_spacer, self.rect.width - shield_double_spacer, shield_height - shield_double_spacer)
        pygame.draw.rect(surface, Colors.RED, shield_red_rect)

        width = int(self.shield * (self.rect.width - shield_double_spacer)) // self.shield_max
        shield_rect = pygame.Rect(left + shield_spacer, top + shield_spacer, width, shield_height - shield_double_spacer)
        pygame.draw.rect(surface, Colors.BLUE, shield_rect)

        step = 6
        inc = (self.rect.width - shield_double_spacer) // (step)
        for i in range(1,step):
            start_pos = (int((left + shield_spacer) + i * inc), top + shield_spacer)
            end_pos = (int((left + shield_spacer) + i * inc), top + shield_height - shield_double_spacer)

            pygame.draw.line(surface, Colors.GRAY, start_pos, end_pos, width=2)

    def init_effects(self):
        self.effects = dict()

         #ion Flare
        self.effects['ion flare'] = dict()
        self.effects['ion flare']["tiny"] = list()

        img = "images/effects/ion flare/tiny/tiny0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["tiny"].append(image)

        img = "images/effects/ion flare/tiny/tiny1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["tiny"].append(image)

        self.effects['ion flare']["small"] = list()
        
        img = "images/effects/ion flare/small/small0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["small"].append(image)

        img = "images/effects/ion flare/small/small1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["small"].append(image)

        self.effects['ion flare']["medium"] = list()
        
        img = "images/effects/ion flare/medium/medium0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["medium"].append(image)

        img = "images/effects/ion flare/medium/medium1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["medium"].append(image)

        self.effects['ion flare']["large"] = list()
        
        img = "images/effects/ion flare/large/large0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["large"].append(image)

        img = "images/effects/ion flare/large/large1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects['ion flare']["large"].append(image)


    def draw_power(self, surface):
        if self.power_force != None :

            #bad practice --> logic in render method
            self.power_counter += 1
            if self.power_counter >= self.power_counter_max:
                self.power_counter = 0

                if self.power_index == 1:
                    self.power_index = 0
                else:
                    self.power_index = 1

            #Render effect
            image = self.effects['ion flare'][self.power_force][self.power_index]
            rect = image.get_rect()
            rect.center = (self.rect.centerx, self.rect.bottom + self.power_offset)
            surface.blit(image, rect)

    def handle_power(self):
        if self.speed == 0:
            self.power_index = 0
            self.power_force = None
        elif self.speed < 3:
            self.power_force = "tiny"
        elif self.speed < 7:
            self.power_force = "small"
        elif self.speed < 11:
            self.power_force = "medium"
        elif self.speed < 20:
            self.power_force = "large"
        elif self.speed < 25:
            self.power_force = "huge"


    def turn_left(self):
        self.angle += self.angle_increment 
        if self.angle >= 360:
            self.angle = 0

    def turn_right(self):
        self.angle -= self.angle_increment
        if self.angle <= -360:
            self.angle = 0

    def reset_turn(self):
        self.angle = 0

    def power_up(self):
        self.speed += self.speed_increment
        if self.speed > self.speed_max:
            self.speed = self.speed_max

        self.handle_power()

    def power_down(self):
        #TO TAKE CARE : Going backward....
        self.speed -= self.speed_increment
        if self.speed < 0:
            self.speed = 0

        self.handle_power()

    def brake(self):
        self.speed = 0
        self.handle_power()


