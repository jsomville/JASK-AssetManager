#!/usr/bin/env python3
import json
from singleton3 import Singleton

from .Ship import Ship
from .Asteroid import Asteroid
from .Planet import Planet
from .Star import Star
from .Station import Station
from .Monster import Monster


class LibraryManager(metaclass=Singleton):
    dataPath = "data/"
    ship_library_name = "Ship.json"
    asteroid_library_name= "Asteroid.json"
    planet_library_name= "Planet.json"
    star_library_name= "Star.json"
    station_library_name= "Station.json"
    monster_library_name = "Monster.json"

    def __init__(self):
        #Load Asteroid
        self.asteroids = list()
        file_path = self.dataPath + self.asteroid_library_name
        self.load_asteroid(file_path)

        #Load Ship
        self.ships = list()
        file_path = self.dataPath + self.ship_library_name
        self.load_ship(file_path)

        #Load Planet
        self.planets = list()
        file_path = self.dataPath + self.planet_library_name
        self.load_planet(file_path)

        #Load Planet
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
                speed_max = ship["speed_max"]
                damage_min = ship["damage_min"]
                damage_max = ship["damage_max"]

                obj = Ship(name, type, img, shield_max, shield_regen, speed_max, damage_min, damage_max)
                
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

    def load_star(self, file_path):
        with open(file_path) as infile:
            data = json.load(infile)

            for star in data["stars"]:
                name = star["name"]
                type = star["type"]
                image = star["image"]

                obj = Star(name, type, image)

                self.stars.append(obj)
    
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
