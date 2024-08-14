import pygame as pg

class DemoDraw:
    def __init__(self):
        # initialize the pygame
        pg.init()
        # set the screen size
        self.screen = pg.display.set_mode((800, 600))
        # set the screen title
        pg.display.set_caption("Basic Draw")
        # get the clock object
        self.clock = pg.time.Clock()
        
    
    def draw(self):
        # draw a line from (100, 100) to (200, 200)
        pg.draw.line(self.screen, (200, 10, 50), (100, 100), (200, 200))
        # draw a rectangle at (300, 100) with width 100 and height 200
        pg.draw.rect(self.screen, (0, 250, 100), (300, 100, 100, 200))
        # draw a circle at (500, 200) with radius 50
        pg.draw.circle(self.screen, (0, 90, 120), (500, 200), 50)
    
    def run(self):
        running = True
        while running:
            # check the events in game
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            # fill the screen with white color
            self.screen.fill((255, 255, 255))
            # draw the shapes
            self.draw()
            # update the screen
            pg.display.flip()
            # set the frame per second
            self.clock.tick(60)
        # quit the pygame
        pg.quit()

if __name__ == "__main__":
    demo = DemoDraw()
    demo.run()