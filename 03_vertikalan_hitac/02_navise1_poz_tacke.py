import math
from simanim import *

scena_w, scena_h = 4.6, 6

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(5)
    UpdatesPerFrame(1)

    m.x = InputFloat(1, (0, scena_w))
    m.y = InputFloat(1, (0, scena_h))


def update(m):
    Finish()


def draw(m):
    scena = Image("romeo1_background.png", (0, 0), scena_w, scena_h)
    romeo = Image("romeo1_romeo.png", (0, 0), scena_w, scena_h)
    tacka = Circle((m.x, m.y), 0.02)
    tacka.fill_color = '#ff0000'
    Draw(scena, romeo, tacka)


Run(setup, update, draw)