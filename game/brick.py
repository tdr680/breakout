from game.config import *


class Brick:

    def __init__(self, x, y, color, tier):
        self.active = True
        self.x = x
        self.y = y
        self.color = color
        self.tier = tier
        self.surface = BRICK[self.color][self.tier]

    def hit(self):
        self.active = False
        pg.mixer.Sound.play(AUDIO['brick-hit-2'])

    def draw(self):
        if self.active:
            SCREEN.blit(self.surface, (self.x, self.y))
