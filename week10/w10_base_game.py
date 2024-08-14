import pygame as pg
from abc import ABC, abstractmethod

class BaseGame(ABC):
    def __init__(self, title, width=800, height=600, bgcolor=(255, 255, 255)):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.bgcolor = bgcolor
    
    @abstractmethod
    def draw(self):
        pass
    
    def handle_events(self):
        pass

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.handle_events()
            # clear screen
            self.screen.fill(self.bgcolor)
            # redraw shapes on screen
            self.draw()
            # update screen
            pg.display.flip()
            self.clock.tick(60)
        pg.quit()