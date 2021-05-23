import math
from simanim import *

scena_w, scena_h = 4.6, 6
ruza_w, ruza_h = 0.25, 0.5

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
    ruza = Image("rose.png", (m.x - ruza_w/2, m.y - ruza_h/2), ruza_w, ruza_h)
    romeo = Image("romeo1_romeo.png", (0, 0), scena_w, scena_h)
    Draw(scena, ruza, romeo)


Run(setup, update, draw)