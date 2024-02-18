import sys
from game.config import *
from game.state.start import StartState
from game.state.play import PlayState


def init():
    pg.display.set_caption(CAPTION)
    SM.states['start'] = StartState()
    SM.states['play'] = PlayState()
    SM.change('start')


def update(dt):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            KEY_DOWN[event.dict['key']] = True
    SM.update(dt)
    KEY_DOWN.clear()


def draw():
    SCREEN.blit(IMG['background'], (0, 0))
    SM.draw()
    pg.display.flip()


def run():
    init()
    while 1:
        update(CLOCK.get_time() / 1000)
        draw()
        CLOCK.tick(FPS)
