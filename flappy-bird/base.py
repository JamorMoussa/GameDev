from abc import ABC, abstractmethod
import pygame as pg

class BaseShape(ABC):

    screen : pg.Surface
    x : int
    y : int 
    x0 : int 
    y0 : int 
    ey : int = 1

    def __init__(self, screen : pg.Surface, pos : tuple[int]):
        self.screen = screen
        self.x, self.y = pos
        self.x0, self.y0 = pos 
    
    def move_y(self, dy : int, ey : int, repl : bool = True):
        if repl:
            self.y = ey * dy
        else:
            self.y += ey * dy 

    def move_x(self, dx : int, ex : int):
        self.x += ex * dx
   
    @abstractmethod
    def rect(self) -> pg.Rect:
        ... 

    @abstractmethod
    def draw(self):
        ...
