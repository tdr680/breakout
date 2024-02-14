import random
from game.config import *
from game.state.base import BaseState
from game.paddle import Paddle
from game.ball import Ball


class PlayState(BaseState):

    def __init__(self):
        self.paused = True
        self.paddle = Paddle()
        self.ball = Ball('green')
        self.ball.dx = random.randint(-200, 200)
        self.ball.dy = random.randint(50, 150)

    def update(self, dt):
        if self.paused:
            if len(KEY_DOWN) > 0 and not KEY_DOWN.get(pg.K_ESCAPE):
                self.paused = False
                pg.mixer.Sound.play(AUDIO['pause'])
        if not self.paused:
            if KEY_DOWN.get(pg.K_ESCAPE):
                self.paused = True
                pg.mixer.Sound.play(AUDIO['pause'])
            else:
                self.paddle.update(dt)
                self.ball.update(dt)
                if self.ball.collides(self.paddle.surface.get_rect().move(self.paddle.x, self.paddle.y)):
                    self.ball.dy = -self.ball.dy

    def draw(self) -> list:
        return [self.paddle.draw(), self.ball.draw()]
