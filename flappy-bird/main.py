import pygame as pg 
from config import Config
from bird import Bird


class FlappyBirdGame:
    running : bool = True 
    screen = pg.display.set_mode(Config.SCREEN_SIZE)

    def __init__(self):
        
        self.bird = Bird(self.screen, pos=(200, 200))

        # set gravity to bird :
        self.bird.set_gravity(v0=1, g=0.1)

    def clean_screen(self):
        self.screen.fill(Config.BG_COLOR)

    def update(self):
        pg.display.update()

    def exit_game(self):
        self.running = False

    def handle(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            self.exit_game()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.bird.gravity.up()
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                ...

    def run(self):
        while self.running:
            self.clean_screen()
            
            for event in pg.event.get():
                self.handle(event) 

            # add draw bird : 
            self.bird.draw()
            
            # add gravity to bird : 
            self.bird.gravity.add()

            # make updates : 
            self.update()



if __name__ == "__main__":

    game = FlappyBirdGame()
    game.run()
