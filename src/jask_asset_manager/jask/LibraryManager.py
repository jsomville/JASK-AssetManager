#!/usr/bin/env python3
import json
from singleton3 import Singleton

import pygame

from .Ship import Ship, ShipPowerForce, ShipEngineType
from .Asteroid import Asteroid
from .Planet import Planet
from .Star import Star
from .Station import Station
from .Monster import Monster
from .Map import Map
from .MapElement import MapElement


class LibraryManager(metaclass=Singleton):
    dataPath = "data/"
    ship_library_name = "Ship.json"
    asteroid_library_name= "Asteroid.json"
    planet_library_name= "Planet.json"
    star_library_name= "Star.json"
    station_library_name= "Station.json"
    monster_library_name = "Monster.json"

    map_file = "Map.json"

    def __init__(self):
        #Load Asteroid
        self.asteroids = list()
        file_path = self.dataPath + self.asteroid_library_name
        self.load_asteroid(file_path)

        #Load Effects
        self.load_effects()

        #Load Ship
        self.ships = list()
        file_path = self.dataPath + self.ship_library_name
        self.load_ship(file_path)

        #Load Planet
        self.planets = list()
        file_path = self.dataPath + self.planet_library_name
        self.load_planet(file_path)

        #Load Star
        self.stars = list()
        file_path = self.dataPath + self.star_library_name
        self.load_star(file_path)

        #Load Station
        self.stations = list()
        file_path = self.dataPath + self.station_library_name
        self.load_station(file_path)

         #Load Monster
        self.monsters = list()
        file_path = self.dataPath + self.monster_library_name
        self.load_monster(file_path)

        #Load Maps
        file_path = self.dataPath + self.map_file
        self.load_map(file_path)

        print("Library Manager initiated")

    #Load Ship
    def load_ship(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for ship in data["ships"]:
                name = ship["name"]
                type = ship["type"]
                img = ship["image"]
                shield_max = ship["shield_max"]
                shield_regen = ship["shield_regen"]
                shield_delay = ship["shield_delay"]
                speed_max = ship["speed_max"]
                damage_min = ship["damage_min"]
                damage_max = ship["damage_max"]
                turn = ship["turn"]
                accell = ship["accell"]
                fire_delay = ship["fire_delay"]

                obj = Ship(name, type, img, shield_max, shield_regen, shield_delay, speed_max, damage_min, damage_max, turn, accell, fire_delay, self.effects)

                self.ships.append(obj)
    
    #Load Asteroid
    def load_asteroid(self, file_path):
         with open(file_path) as infile:
            data = json.load(infile)

            for asteroid in data["asteroids"]:
                name = asteroid["name"]
                type = asteroid["type"]
                image = asteroid["image"]
                min = asteroid["min"]
                max = asteroid["max"]

                obj = Asteroid(name, type, image, min, max)

                self.asteroids.append(obj)


    def load_planet(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for planet in data["planets"]:
                name = planet["name"]
                type = planet["type"]
                image = planet["image"]

                obj = Planet(name, type, image)

                self.planets.append(obj)

        self.planet_dict = dict()
        for planet in self.planets:
            self.planet_dict[planet.name] = planet


    def load_star(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for star in data["stars"]:
                name = star["name"]
                type = star["type"]
                image = star["image"]

                obj = Star(name, type, image)

                self.stars.append(obj)

        self.star_dict = dict()
        for star in self.stars:
            self.star_dict[star.name] = star
    

    def load_station(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for station in data["stations"]:
                name = station["name"]
                image = station["image"]

                obj = Station(name, image)

                self.stations.append(obj)


    def load_monster(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for monster in data["monsters"]:
                name = monster["name"]
                image = monster["image"]
                nb_sprites = monster["nb_sprites"]
                shield_max = monster["shield_max"]
                shield_regen = monster["shield_regen"]
                damage_min = monster["damage_min"]
                damage_max = monster["damage_max"]

                obj = Monster(name, image, nb_sprites, shield_max, shield_regen, damage_min, damage_max)

                self.monsters.append(obj)


    def load_effects(self):
        self.effects = dict()

        #Ion Flare
        engine_type = ShipEngineType.ION
        self.effects[engine_type] = dict()
        self.effects[engine_type][ShipPowerForce.TINY] = list()

        img = "images/effects/ion flare/tiny/tiny0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.TINY].append(image)

        img = "images/effects/ion flare/tiny/tiny1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.TINY].append(image)

        self.effects[engine_type][ShipPowerForce.SMALL] = list()
        
        img = "images/effects/ion flare/small/small0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.SMALL].append(image)

        img = "images/effects/ion flare/small/small1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.SMALL].append(image)

        self.effects[engine_type][ShipPowerForce.MEDIUM] = list()
        
        img = "images/effects/ion flare/medium/medium0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.MEDIUM].append(image)

        img = "images/effects/ion flare/medium/medium1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.MEDIUM].append(image)

        self.effects[engine_type][ShipPowerForce.LARGE] = list()
        
        img = "images/effects/ion flare/large/large0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.LARGE].append(image)

        img = "images/effects/ion flare/large/large1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.LARGE].append(image)

        self.effects[engine_type][ShipPowerForce.HUGE] = list()
        
        img = "images/effects/ion flare/huge/huge0.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.HUGE].append(image)

        img = "images/effects/ion flare/huge/huge1.png"
        image = pygame.image.load(img).convert_alpha()
        self.effects[engine_type][ShipPowerForce.LARGE].append(image)


    def load_map(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)
            for map in data["maps"]:
                id = map["id"]
                name = map["name"]
                width = map["width"]
                height = map["height"]

                elements = list()
                for element in map["elements"]:
                    elements.append(MapElement(element))  

                self.map = Map(id, name, width, height, elements)



