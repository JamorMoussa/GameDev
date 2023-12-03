import pygame as pg 
from config import Config
from bird import Bird
from pipe import Pipe, GroupeOfPipes


class FlappyBirdGame:
    running : bool = True 
    screen = pg.display.set_mode(Config.SCREEN_SIZE)

    def __init__(self):
        
        self.bird = Bird(self.screen, pos=(200, 200))

        self.grp_pipes = GroupeOfPipes(self.screen, 3)
        #self.pipe.set_height(0.2)

        # set gravity to bird :
        self.bird.set_gravity(v0=5, g=0.1)

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

            # draw pipe : 
            self.grp_pipes.draw()

            # move :
            self.grp_pipes.move_x(0.1, -1)

            #print(self.pipe.success(self.bird))

            # make updates : 
            self.update()



if __name__ == "__main__":

    game = FlappyBirdGame()
    game.run()
