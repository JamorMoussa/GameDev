from abc import ABC, abstractmethod
import pygame as pg
from gravity import Gravity

class BaseShape(ABC):

    screen : pg.Surface
    x : int
    y : int 
    x0 : int 
    y0 : int 
    ey : int = 1
    gravity : Gravity

    def __init__(self, screen : pg.Surface, pos : tuple[int]):
        self.screen = screen
        self.x, self.y = pos
        self.x0, self.y0 = pos 
    
    def move_y(self, dy : int, ey : int):
        self.y = ey * dy

    def set_gravity(self, v0 : float = 1, g : float = 0.1, dt : float = 0.1):
        self.gravity = Gravity(self, v0, g, dt)
   
    @abstractmethod
    def rect(self):
        ... 

    @abstractmethod
    def draw(self):
        ...
