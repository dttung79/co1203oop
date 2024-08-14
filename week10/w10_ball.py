import pygame as pg

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

class Ball:
    def __init__(self, x, y, radius, color, step_x=5, step_y=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step_x = step_x
        self.step_y = step_y
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self, direction):
        if direction == LEFT:
            self.x -= self.step_x
        elif direction == RIGHT:
            self.x += self.step_x
        elif direction == UP:
            self.y -= self.step_y
        elif direction == DOWN:
            self.y += self.step_y