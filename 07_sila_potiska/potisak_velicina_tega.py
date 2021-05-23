import math
from simanim import *

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 6, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.маса_тега = InputFloat(1000, (100, 21000))

def update(m):
        Finish()

def draw(m):
    teg_razmera = (m.маса_тега / 21000) ** (1/3)
    teg_w, teg_h = 0.95 * teg_razmera, 1.15 * teg_razmera
    teg = Image("weight.png", (1, 1), teg_w, teg_h)

    Draw(teg)

Run(setup, update, draw)