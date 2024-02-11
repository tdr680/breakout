from game.config import *
from game.state.base import BaseState
from game.paddle import Paddle


class PlayState(BaseState):

    def __init__(self):
        self.paddle = Paddle()
        self.paused = True

    def update(self, dt):
        if self.paused:
            print('paused')
            if len(KEY_DOWN) > 0 and not KEY_DOWN.get(pg.K_ESCAPE):
                self.paused = False
                pg.mixer.Sound.play(AUDIO['pause'])
        if not self.paused:
            print('running')
            if KEY_DOWN.get(pg.K_ESCAPE):
                self.paused = True
                pg.mixer.Sound.play(AUDIO['pause'])
            else:
                self.paddle.update(dt)

    def draw(self):
        self.paddle.draw()
