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
    'main': pg.image.load('img/breakout.png').convert_alpha()
}

FONT = {
    'small': pg.font.Font('font/font.ttf', 8),
    'medium': pg.font.Font('font/font.ttf', 16),
    'large': pg.font.Font('font/font.ttf', 32)
}

AUDIO = {
    'paddle-hit': pg.mixer.Sound("audio/paddle_hit.wav"),
    'confirm': pg.mixer.Sound("audio/confirm.wav"),
    'pause': pg.mixer.Sound("audio/pause.wav")
}

COLOR_WHITE = (255, 255, 255)
COLOR_SELECTED = (50, 255, 50)

KEY_DOWN = {}

SM = game.sm.StateMachine()

PADDLE = game.util.paddles(IMG['main'])

PADDLE_SPEED = 250
