import pygame as pg
import game.sm
import game.util

FPS = 60
CAPTION = "breakout"
SIZE = WIDTH, HEIGHT = 436, 280

CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(SIZE)

IMG = {
    'background': pg.transform.scale(pg.image.load('img/background.png').convert(), (WIDTH+1, HEIGHT+3)),
    'main': pg.image.load('img/breakout.png').convert()
}

FONT = {
    'small': pg.font.Font('font/font.ttf', 8),
    'medium': pg.font.Font('font/font.ttf', 16),
    'large': pg.font.Font('font/font.ttf', 32)
}

AUDIO = {
    'paddle-hit': pg.mixer.Sound("audio/paddle_hit.wav"),
    'confirm': pg.mixer.Sound("audio/confirm.wav"),
    'pause': pg.mixer.Sound("audio/pause.wav"),
    'wall_hit': pg.mixer.Sound("audio/wall_hit.wav"),
    'brick-hit-1': pg.mixer.Sound("audio/brick-hit-1.wav"),
    'brick-hit-2': pg.mixer.Sound("audio/brick-hit-2.wav")
}

COLOR_WHITE = (255, 255, 255)
COLOR_SELECTED = (50, 255, 50)

KEY_DOWN = {}

SM = game.sm.StateMachine()

PADDLE = game.util.paddles(IMG['main'])
BALL = game.util.balls(IMG['main'])
BRICK = game.util.bricks(IMG['main'])

PADDLE_SPEED = 350
