import math
from simanim import *

# konstante:            
scena_w, scena_h = 4.6, 6
h1 = 2.24 # Rastojanje izmedju Romeove i Julijine sake

def setup(m):
    PixelsPerUnit(72)
    ViewBox((0, 0), 4.6, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.v0 = InputFloat(7.1, (1, 9))

    m.h = 0    # m.h ce biti visina slike ruze
    m.v = m.v0  # m.v ce biti brzina ruze
    m.g = 10    # koristimo g = 10 zbog jednostavnijeg racunanja


def update(m):
    dv = - m.g * m.dt
    dh = m.v * m.dt - m.g * m.dt * m.dt / 2

    m.h += dh
    m.v += dv
    if m.h < 0:
        m.h = 0 # ne nize od Romeove ruke

    if m.h == 0 or (abs(m.h - h1) < 0.05 and abs(m.v) <= 0.1):
        Finish()


def draw(m):
    pozadina = Image("romeo1_background.png", (0, 0), scena_w, scena_h)
    ruza = Image("rose.png", (0, m.h), scena_w, scena_h)
    romeo = Image("romeo1_romeo.png", (0, 0), scena_w, scena_h)
    Draw(pozadina, ruza, romeo)


Run(setup, update, draw)