#!/usr/bin/env python3
from enum import IntEnum


class CelestialObjectType(IntEnum):
    NONE = 0
    STAR = 1
    PLANET = 2
    STAR_BASE = 3
    WORM_HOLE = 4
    ASTEROID = 5
    JUMP_GATE = 6


class AsteroidType(IntEnum):
    NONE = 0
    ROCK = 1
    METAL = 2
    GOLD = 3
    IRON = 4
    LEAD = 5
    SILICON = 6
    SILVER = 7
    TITANIUM = 8
    YOTTRITE = 9


class CelestialObject:
    name = ""
    type = CelestialObjectType.NONE
    image = "..images/img.png"

    properties = dict()

    def __init__(self, d=None):
        if d is not None:
            self.name = d["name"]
            self.type = d["type"]
            self.image = d["image"]

            if "properties" in d:
                self.properties = d["properties"]
