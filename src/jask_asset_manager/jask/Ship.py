 #!/usr/bin/env python3
from enum import IntEnum
import math

import pygame
from pygame.locals import *

from pygame_framework.Colors import Colors

from .Projectile import Projectile
from .Projectile import ProjectileType
from .MathUtil import MathUtil

class ShipClass(IntEnum):
    FIGHTER = 1
    HAULER = 2
    FREIGHTER = 3
    CARRIER = 4


class ShipPowerForce(IntEnum):
    NONE = 0
    TINY = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    HUGE = 5


class ShipEngineType(IntEnum):
    ION = 1


class Ship(pygame.sprite.Sprite):

    def __init__(self, name, type, img, shield_max, shield_regen, shield_delay, speed_max, damage_min, damage_max, turn, accell, fire_delay, effects):
        pygame.sprite.Sprite.__init__(self)

        #Properties
        self.name = name
        self.type = type 
        self.shield_max = shield_max
        self.shield_regen = shield_regen # per shield_delay
        self.shield_delay = shield_delay
        self.speed_max = speed_max
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.turn = turn
        self.accell = accell
        self.fire_delay = fire_delay

        #Load image
        image = pygame.image.load(img).convert_alpha()
        self.image = image
        self.rect = self.image.get_rect()

        #Effects
        self.effects = effects

        #To improve
        self.scale = 1
        self.power_counter = 0
        self.power_counter_max = 5
        self.power_offset =  8
        self.engine_type = ShipEngineType.ION

        #Ship Default Values
        self.shield = 0
        self.angle = 0
        self.speed = 0
        self.pos = (0,0)
        self.next_shield_recharge = pygame.time.get_ticks() + self.shield_delay
        self.next_fire = pygame.time.get_ticks() + self.fire_delay
        self.enable_weapon = False
        self.power_force = None
        self.power_image_index = 0
        self.x = 0
        self.y = 0

        #Projectiles
        self.projectiles = list()
    

    def update(self, pos, angle, speed, shield):
        self.rect.center = pos

        self.angle = angle
        self.speed = speed
        self.shield = shield
    

    def on_loop(self):
        #Ship Position
        self.rad_angle = self.angle / 360 * MathUtil.TWO_PI
        self.x = self.x - math.sin(self.rad_angle) * (self.speed / 100)
        self.y = self.y - math.cos(self.rad_angle) * (self.speed / 100)

        #Power Ion switching
        self.power_counter += 1
        if self.power_counter >= self.power_counter_max:
            self.power_counter = 0
            if self.power_image_index == 1:
                self.power_image_index = 0
            else:
                self.power_image_index = 1

        #Handle projectiles
        for projectile in self.projectiles:
            projectile.on_loop()
            #if projectile.life > projectile.life_max:
            if projectile.distance >= 200:
                self.projectiles.pop(self.projectiles.index(projectile))

        #Shield Recharge
        if pygame.time.get_ticks() > self.next_shield_recharge:
            self.next_shield_recharge = pygame.time.get_ticks() + self.shield_delay
            if self.shield < self.shield_max:
                self.shield += self.shield_regen
                if self.shield > self.shield_max:
                    self.shield = self.shield_max


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

    


    def draw_power(self, surface, yoffset):
        if self.speed > 0:
            self.get_power_force_from_speed()

            render_rect = surface.get_rect()

            #Render effect
            image = self.effects[self.engine_type][self.power_force][self.power_image_index]
            rect = image.get_rect()
            rect.center = (render_rect.centerx, yoffset)
            surface.blit(image, rect)

    #******************************************************
    #Could be improved....
    def get_power_force_from_speed(self):
        if self.speed == 0:
            self.power_image_index = 0
            self.power_force = None
        elif self.speed < 3:
            self.power_force = ShipPowerForce.TINY
        elif self.speed < 7:
            self.power_force = ShipPowerForce.SMALL
        elif self.speed < 11:
            self.power_force = ShipPowerForce.MEDIUM
        elif self.speed < 20:
            self.power_force = ShipPowerForce.LARGE
        elif self.speed > 25:
            self.power_force = ShipPowerForce.HUGE

    def turn_left(self):
        self.angle += self.turn 
        if self.angle >= 360:
            self.angle = 0

    def turn_right(self):
        self.angle -= self.turn
        if self.angle <= -360:
            self.angle = 0

    def reset_turn(self):
        self.angle = 0

    def power_up(self):
        self.speed += self.accell
        if self.speed > self.speed_max:
            self.speed = self.speed_max

    def power_down(self):
        #TO TAKE CARE : Going backward....
        self.speed -= self.accell
        if self.speed < 0:
            self.speed = 0

    def brake(self):
        self.speed = 0

    def shoot(self):
        if self.enable_weapon :
            if pygame.time.get_ticks() > self.next_fire:
                self.next_fire = pygame.time.get_ticks() + self.fire_delay

                dist = self.rect.height // 2

                x = self.rect.centerx - math.sin(self.rad_angle) * dist
                y = self.rect.centery - math.cos(self.rad_angle) * dist

                projectile = Projectile(ProjectileType.ION_BOLT, x, y, self.angle)
                self.projectiles.append(projectile)

    def toggle_weapon(self):
        self.enable_weapon = not self.enable_weapon



