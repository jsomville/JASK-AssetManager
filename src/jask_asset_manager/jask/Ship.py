 #!/usr/bin/env python3
from enum import IntEnum
import pygame
from pygame.locals import *

from pygame_framework.Colors import Colors

from .Projectile import Projectile
from .Projectile import ProjectileType

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
        self.angle_increment = 3
        self.speed_increment = 1
        self.scale = 1
        self.power_counter = 0
        self.power_counter_max = 5
        self.power_index = 0
        self.power_force = None
        self.power_offset =  8

        #Projectiles
        self.projectiles = list()

        #Init effects
        self.init_effects() 
    
    def update(self, pos, angle, speed, shield):
        self.rect.center = pos

        self.angle = angle
        self.speed = speed
        self.shield = shield

        print(f"shield : {self.shield}")
    

    def draw(self, surface):

        #Create Temporary Surface
        tmp_ship = pygame.Surface((self.rect.width, self.rect.height * 2))
        tmp_rect = tmp_ship.get_rect()

        #Draw Ship
        tmp_ship_rect = self.rect.copy()
        tmp_ship_rect.center = tmp_rect.center
        tmp_ship.blit(self.image, tmp_ship_rect)

        #Draw Power
        yoffset = tmp_ship_rect.bottom + self.power_offset
        self.draw_power(tmp_ship, yoffset)

        #Handle Ship Transform
        cur_image = pygame.transform.rotozoom(tmp_ship, self.angle, self.scale)
        rect = cur_image.get_rect()
        rect.center = self.rect.center
        surface.blit(cur_image, rect)

        #Handle projectiles
        for projectile in self.projectiles:
            projectile.draw(surface)
    
    def on_loop(self):
        #Power Ion switching
        self.power_counter += 1
        if self.power_counter >= self.power_counter_max:
            self.power_counter = 0

            if self.power_index == 1:
                self.power_index = 0
            else:
                self.power_index = 1

        #Handle projectiles
        for projectile in self.projectiles:
            projectile.on_loop()
            if projectile.life > projectile.life_max:
                self.projectiles.pop(self.projectiles.index(projectile))    


    #******************************************************
    #Could be improved
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


    def draw_power(self, surface, yoffset):
        if self.power_force != None :
            render_rect = surface.get_rect()

            #Render effect
            image = self.effects['ion flare'][self.power_force][self.power_index]
            rect = image.get_rect()
            rect.center = (render_rect.centerx, yoffset)
            surface.blit(image, rect)

    #******************************************************
    #Could be improved....
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

    def shoot(self):
        x = self.rect.centerx
        y = self.rect.top

        projectile = Projectile(ProjectileType.ION_BOLT, x, y, self.angle)
        self.projectiles.append(projectile)


