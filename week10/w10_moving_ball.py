import pygame
from w10_base_game import BaseGame
from w10_ball import Ball, LEFT, RIGHT, UP, DOWN

class MovingBallGame(BaseGame):
    def __init__(self, ball):
        super().__init__("Moving Ball")
        self.ball = ball
    
    def draw(self):
        self.ball.draw(self.screen)
    
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ball.move(LEFT)
        if keys[pygame.K_RIGHT]:
            self.ball.move(RIGHT)
        if keys[pygame.K_UP]:
            self.ball.move(UP)
        if keys[pygame.K_DOWN]:
            self.ball.move(DOWN)

if __name__ == "__main__":
    ball = Ball(400, 300, 50, (0, 0, 255))
    game = MovingBallGame(ball)
    game.run()