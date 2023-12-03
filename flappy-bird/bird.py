import pygame as pg
from config import Config
from base import BaseShape
from gravity import Gravity


class Bird(BaseShape):

    gravity : Gravity

    def set_gravity(self, v0 : float = 1, g : float = 0.1, dt : float = 0.1):
        self.gravity = Gravity(self, v0, g, dt)

    def rect(self):
        return pg.Rect(self.x - Config.BIRD_RADIUS, self.y - Config.BIRD_RADIUS, *[Config.BIRD_RADIUS, ]*2)

    def draw(self):
        pg.draw.circle(self.screen, Config.BIRD_COLOR, (self.x, self.y), Config.BIRD_RADIUS)