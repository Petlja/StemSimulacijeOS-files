import math
from simanim import *

# konstante:
scena_w, scena_h = 4.6, 6
h1 = 2.24 # Rastojanje izmedju Romeove i Julijine sake

def setup(m):
    PixelsPerUnit(72)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.v0 = InputFloat(7.1, (1, 9))

    m.h = 0     # m.h ce biti visina slike ruze
    m.v = m.v0  # m.v ce biti brzina ruze
    m.g = 10    # koristimo g = 10 da bi se rezultat slagao sa jednostavnijim racunanjem


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

    tx = 2.8
    tekst_t = Text((tx, 5.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.15
    tekst_v = Text((tx, 5.5), f'v ={m.v:6.2f}m/s')
    tekst_h = Text((tx, 5.3), f'h ={m.h:6.2f}m')
    tekst_h1 = Text((tx, 5.1), f'h1 ={h1:5.2f}m')
    Draw(tekst_t, tekst_v, tekst_h, tekst_h1)

Run(setup, update, draw)