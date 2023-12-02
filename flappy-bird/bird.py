import pygame as pg
from config import Config
from typing import overload
from base import BaseShape


class Bird(BaseShape):

    def rect(self):
        return pg.Rect(self.x - Config.BIRD_RADIUS, self.y - Config.BIRD_RADIUS, *[Config.BIRD_RADIUS, ]*2)

    def draw(self):
        pg.draw.circle(self.screen, Config.BIRD_COLOR, (self.x, self.y), Config.BIRD_RADIUS)