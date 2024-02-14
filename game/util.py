import pygame as pg


def paddles(sheet):
    pd = {}
    for h, color in ((0, 'blue'), (32, 'green'), (64, 'red'), (96, 'violet')):
        p = []
        for q in ((0, 64 + h, 32, 16), (32, 64 + h, 64, 16), (96, 64 + h, 128, 16), (0, 80 + h, 144, 16)):
            r = pg.Rect(q)
            i = pg.Surface(r.size).convert_alpha()
            i.blit(sheet, (0, 0), r)
            ck = i.get_at((0, 0))
            i.set_colorkey(ck, pg.RLEACCEL)
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
        ck = i.get_at((0, 0))
        i.set_colorkey(ck, pg.RLEACCEL)
        b[color] = i
    return b
