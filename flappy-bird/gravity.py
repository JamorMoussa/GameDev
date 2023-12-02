
class Gravity:
    v0 : int = 0
    g : int = 1

    dt : float = 0
    t : float = 0 
    dy : int 

    shape : None 

    def __init__(self, shape ,v0 : int, g : float, dt : float = 0.1):
        self.v0 = v0 
        self.g = g
        self.dt = dt 
        self.shape = shape

    def add(self):
        y = self.shape.y0 - self.v0 * self.t + (1/2) * self.g * self.t**2
        self.dy = - self.v0 + self.g * self.t 
        self.shape.move_y(y, 1) 
        self.t += self.dt 

    def up(self):
        self.dt *= -1 
