import random
from game.config import *
from game.state.base import BaseState
from game.paddle import Paddle
from game.ball import Ball
from game.level import Level


class PlayState(BaseState):

    def __init__(self):
        self.paused = True
        self.paddle = Paddle()
        self.ball = Ball('blue')
        self.ball.dx = random.randint(-200, 200)
        self.ball.dy = random.randint(50, 150)
        self.bricks = Level.map(0)

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
                for b in self.bricks:
                    if b.active and self.ball.collides(b.surface.get_rect().move(b.x, b.y)):
                        b.active = False

    def draw(self):
        self.paddle.draw()
        self.ball.draw()
        for b in self.bricks:
            b.draw()
