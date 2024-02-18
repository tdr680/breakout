from game.config import *


class Paddle:

    def __init__(self):
        self.x = WIDTH//2 - 32
        self.y = HEIGHT - 32
        self.dx = 0
        self.color = 'blue'
        self.size = 1
        self.surface = PADDLE[self.color][self.size]

    def update(self, dt):
        self.dx = 0
        if pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT]:
            self.dx = -PADDLE_SPEED
        if pg.key.get_pressed()[pg.K_RIGHT] and not pg.key.get_pressed()[pg.K_LEFT]:
            self.dx = PADDLE_SPEED
        self.x = self.x + self.dx * dt
        self.x = max(0, min(self.x, WIDTH-self.surface.get_rect().width))

    def draw(self):
        SCREEN.blit(self.surface, (self.x, self.y))
