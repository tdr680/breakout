import pygame as pg


def paddles(sheet):
    pd = {}
    for h, color in ((0, 'blue'), (32, 'green'), (64, 'red'), (96, 'violet')):
        p = []
        for q in ((0, 64 + h, 32, 16), (32, 64 + h, 64, 16), (96, 64 + h, 128, 16), (0, 80 + h, 144, 16)):
            r = pg.Rect(q)
            i = pg.Surface(r.size).convert_alpha()
            i.blit(sheet, (0, 0), r)
            i.set_colorkey(i.get_at((0, 0)), pg.RLEACCEL)
            p.append(i)
        pd[color] = p
    return pd


def balls(sheet):
    b = {}
    for t, color in (((96, 48, 8, 8), 'blue'),
                     ((96 + 8, 48, 8, 8), 'green'),
                     ((96 + 2 * 8, 48, 8, 8), 'red'),
                     ((96 + 3 * 8, 48, 8, 8), 'violet'),
                     ((96, 48 + 8, 8, 8), 'yellow'),
                     ((96 + 8, 48 + 8, 8, 8), 'grey'),
                     ((96 + 2 * 8, 48 + 8, 8, 8), 'orange')):
        r = pg.Rect(t)
        i = pg.Surface(r.size).convert_alpha()
        i.blit(sheet, (0, 0), r)
        i.set_colorkey(i.get_at((0, 0)), pg.RLEACCEL)
        b[color] = i
    return b


def bricks(sheet):
    b = {}
    m = {
      'blue': [(0, 0, 32, 16), (32, 0, 32, 16), (64, 0, 32, 16), (96, 0, 32, 16)],
      'green': [(128, 0, 32, 16), (160, 0, 32, 16), (0, 16, 32, 16), (32, 16, 32, 16)],
      'red': [(64, 16, 32, 16), (96, 16, 32, 16), (128, 16, 32, 16), (160, 16, 32, 16)],
      'violet': [(0, 32, 32, 16), (32, 32, 32, 16), (64, 32, 32, 16), (96, 32, 32, 16)],
      'extra': [(128, 32, 32, 16), (160, 32, 32, 16), (0, 48, 32, 16), (32, 48, 32, 16), (64, 48, 32, 16)]
    }
    for _, color in enumerate(m):
        p = []
        for q in m[color]:
            r = pg.Rect(q)
            i = pg.Surface(r.size).convert_alpha()
            i.blit(sheet, (0, 0), r)
            i.set_colorkey(i.get_at((0, 0)), pg.RLEACCEL)
            p.append(i)
        b[color] = p
    return b
