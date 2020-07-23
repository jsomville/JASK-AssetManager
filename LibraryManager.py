#!/usr/bin/env python3
import json

from CelestialObject import CelestialObject
from CelestialObject import CelestialObjectType
from CelestialObject import AsteroidType
from CelestialObjectLibrary import CelestialObjectLibrary


class LibraryManager:
    dataPath = "data/"
    celestialObjectLibraryName = "CelestialObjectLibrary.json"

    celestialObjectLibrary = dict()

    def __init__(self):
        self.celestialObjectLibraryPath = self.dataPath + self.celestialObjectLibraryName

        self.celestialsObjectsLibrary = CelestialObjectLibrary()

        #Testing
        #self.init_asteroid()

        #Load Library
        self.load_library()

        print ("finished loading library")

    def init_asteroid(self):

        #As objects
        obj = CelestialObject()
        obj.name = "rock_small"
        obj.type = CelestialObjectType.ASTEROID
        obj.image = "images/celestialObjects/asteroid/rock_small.png"
        obj.properties = dict()
        obj.properties["asteroid_type"] = AsteroidType.ROCK
        obj.properties["min"] = 100
        obj.properties["max"] = 250
        self.celestialsObjectsLibrary.celestialObjectList.append(obj)

        obj = CelestialObject()
        obj.name = "rock_medium"
        obj.type = CelestialObjectType.ASTEROID
        obj.image = "images/celestialObjects/asteroid/rock_medium.png"
        obj.properties = dict()
        obj.properties["asteroid_type"] = AsteroidType.ROCK
        obj.properties["min"] = 250
        obj.properties["max"] = 400
        self.celestialsObjectsLibrary.celestialObjectList.append(obj)

        obj = CelestialObject()
        obj.name = "rock_large"
        obj.type = CelestialObjectType.ASTEROID
        obj.image = "images/celestialObjects/asteroid/rock_large.png"
        obj.properties = dict()
        obj.properties["asteroid_type"] = AsteroidType.ROCK
        obj.properties["min"] = 400
        obj.properties["max"] = 1000
        self.celestialsObjectsLibrary.celestialObjectList.append(obj)

        obj = CelestialObject()
        obj.name = "gold"
        obj.type = CelestialObjectType.ASTEROID
        obj.image = "images/celestialObjects/asteroid/gold.png"
        obj.properties = dict()
        obj.properties["asteroid_type"] = AsteroidType.GOLD
        obj.properties["min"] = 100
        obj.properties["max"] = 250
        self.celestialsObjectsLibrary.celestialObjectList.append(obj)

        self.write_asteroid()

    def load_library(self):
        print("LOAD")

        #Clear already loaded or inited data
        self.celestialsObjectsLibrary.celestialObjectList.clear()

        file_path = self.celestialObjectLibraryPath
        with open(file_path) as infile:
            data = json.load(infile)

            for asteroid in data["asteroid"]:
                obj = CelestialObject(asteroid)
                self.celestialsObjectsLibrary.celestialObjectList.append(obj)

    def write_asteroid(self):
        data = dict()
        data["asteroid"] = list()
        for obj in self.celestialsObjectsLibrary.celestialObjectList:
            if obj.type == CelestialObjectType.ASTEROID:
                print(obj.get_details())
                print(obj.properties["asteroid_type"])
                data["asteroid"].append(obj.__dict__)

        #Write Celestial
        file_path = self.celestialObjectLibraryPath
        self.write_library(file_path, data)

    def write_library(self, file_path, data):
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)


