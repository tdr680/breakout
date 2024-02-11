from game.state.base import BaseState
from game.config import *


class StartState(BaseState):

    def __init__(self):
        self.selected = 1

    def update(self, dt):
        if KEY_DOWN.get(pg.K_DOWN) or KEY_DOWN.get(pg.K_UP):
            self.selected = self.selected == 1 and 2 or 1
            pg.mixer.Sound.play(AUDIO['paddle-hit'])
        if KEY_DOWN.get(pg.K_RETURN):
            if self.selected == 1:
                SM.change('play')
                pg.mixer.Sound.play(AUDIO['confirm'])

    def draw(self):
        title = FONT['large'].render(CAPTION, True, COLOR_WHITE)
        title_rect = title.get_rect()
        title_rect.center = (WIDTH//2, HEIGHT//2)
        SCREEN.blit(title, title_rect)

        start = FONT['medium'].render('start', True, COLOR_SELECTED if self.selected == 1 else COLOR_WHITE)
        start_rect = start.get_rect()
        start_rect.center = (WIDTH//2, HEIGHT//2 + 80)
        SCREEN.blit(start, start_rect)

        score = FONT['medium'].render('high scores', True, COLOR_SELECTED if self.selected == 2 else COLOR_WHITE)
        score_rect = score.get_rect()
        score_rect.center = (WIDTH//2, HEIGHT//2 + 110)
        SCREEN.blit(score, score_rect)
