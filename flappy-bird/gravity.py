import math 


class Gravity:
    v0 : int = 0
    g : int = 1

    dt : float = 0
    t : float = 0 
    dy : int 
    et : int = 1
    y0 : int

    shape : None 

    def __init__(self, shape ,v0 : int, g : float, dt : float = 0.1):
        self.v0 = v0 
        self.g = g
        self.dt = dt 
        self.shape = shape
        self.up()

    def add(self):
        y = self.y0 - self.v0 * math.sin(math.pi/4) * self.t + (1/2) * self.g * self.t**2
        self.shape.move_y(y, 1)
        self.t += self.dt 

    def up(self):
        self.y0 = self.shape.y
        self.x0 = self.shape.x
        self.t = 0