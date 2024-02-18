from game.config import *


class Ball:

    def __init__(self, color):
        self.x = WIDTH//2 - 4
        self.y = 8
        self.dx = 0
        self.dy = 0
        self.color = color
        self.surface = BALL[color]

    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt

        if self.x <= 0:
            self.x = 0
            self.dx = -self.dx
            pg.mixer.Sound.play(AUDIO['wall_hit'])

        if self.x + self.surface.get_rect().width >= WIDTH:
            self.x = WIDTH - self.surface.get_rect().width
            self.dx = -self.dx
            pg.mixer.Sound.play(AUDIO['wall_hit'])

        if self.y <= 0:
            self.y = 0
            self.dy = -self.dy
            pg.mixer.Sound.play(AUDIO['wall_hit'])

        if self.y + self.surface.get_rect().height >= HEIGHT:
            self.y = HEIGHT - self.surface.get_rect().height
            self.dy = -self.dy
            pg.mixer.Sound.play(AUDIO['wall_hit'])

    def draw(self):
        SCREEN.blit(self.surface, (self.x, self.y))

    def collides(self, r) -> bool:
        return self.surface.get_rect().move(self.x, self.y).colliderect(r)
