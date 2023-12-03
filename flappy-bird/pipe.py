import pygame as pg
from config import Config
from base import BaseShape
import random


class Pipe(BaseShape):
    screen : pg.Surface
    x : int 
    h : int

    def __init__(self, screen : pg.Surface, x0 : int):
        self.screen = screen
        self.x = x0
        self.h = self.screen.get_height()//3


    def set_height(self, ph : float):
        if not (0 <= ph <= 1):
            raise ValueError(f"The value : ph = {ph} is not between 0 and 1")
        self.h = ph * self.screen.get_height()

    def rect(self):
        return (
            pg.Rect(self.x, 0, Config.PIP_WIDTH, self.h),
            pg.Rect(self.x, self.h, Config.PIP_WIDTH, self.screen.get_height() - self.h),
            pg.Rect(self.x, self.screen.get_height() - self.h, Config.PIP_WIDTH, self.screen.get_height())
        )
    
    def success(self, shape : BaseShape):
        return (shape.rect().right > self.rect()[1].right)

    def draw(self):
        pg.draw.rect(self.screen, Config.PIPE_COLOR, self.rect()[0])
        pg.draw.rect(self.screen, Config.PIPE_COLOR, self.rect()[2])



class GroupeOfPipes:

    pipes : list[Pipe]
    screen : pg.Surface 

    def __init__(self, screen : pg.Surface , num_pipes : int):
        self.screen = screen

        self.pipes = [Pipe(self.screen, self.screen.get_width()*random.random()) for i in range(num_pipes)]

    def move_x(self, dx : int , ex: int =1):
        for pipe in self.pipes:
            pipe.move_x(dx, ex)

    def draw(self):
        for pipe in self.pipes:
            pipe.draw()
    