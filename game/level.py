import random
from game.brick import Brick


class Level:

    @staticmethod
    def map(level):
        ba = []
        r = random.randint(1, 5)
        c = random.randint(7, 13)
        for y in range(r):
            for x in range(c):
                b = Brick(x * 32            # the screen should have 8 pixels of padding
                          + 8               # we can fit 13 cols + 16 pixels total
                          + (13 - c) * 16,  # left-side padding for when there are fewer than 13 columns
                          y * 16 + 8,       # y
                          'blue',           # color
                          level)
                ba.append(b)
        return ba
