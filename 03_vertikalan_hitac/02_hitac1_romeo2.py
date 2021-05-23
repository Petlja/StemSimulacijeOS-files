import math
from simanim import *

# konstante:
scena_w, scena_h = 4.6, 6
h1 = 2.11 # Rastojanje izmedju Romeove i Julijine sake

def setup(m):
    PixelsPerUnit(72)
    ViewBox((0, 0), 4.6, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(5)

    m.v0 = InputFloat(5.1, (3.1, 9.9))
    m.H = InputFloat(2.6,(1.2, 4.2)) # rastojanje izmedju Julijine i Romeove sake

    m.y_gornje_sl = m.H - h1

    m.h = 0 # visina slike ruze
    m.v = m.v0 # m.v ce biti brzina ruze navise (ako je negativna, nanize)
    m.g = 10 # koristimo g = 10 da bi se rezultat slagao sa jednostavnijim racunanjem

def update(m):
    dv = - m.g * m.dt
    dh = m.v * m.dt - m.g * m.dt * m.dt / 2

    m.h += dh
    m.v += dv

    if m.h <= 0 or (abs(m.h - m.H) < 0.05 and abs(m.v) <= 0.1):
        if m.h < 0:
            m.h = 0 # ne nize od Romeove ruke
            m.v = m.v0
        Finish()


def draw(m):
    gornji_deo = Image("romeo2_upper.png", (0, m.y_gornje_sl), scena_w, scena_h)
    donji_deo = Image("romeo2_lower.png", (0, 0), scena_w, scena_h)
    ruza = Image("rose.png", (0, m.h), scena_w, scena_h)
    romeo = Image("romeo1_romeo.png", (0, 0), scena_w, scena_h)

    tekst_t = Text((3, 5.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.2
    tekst_v = Text((3, 5.5), f'v ={abs(m.v):6.2f}m/s')
    tekst_h = Text((3, 5.3), f'h ={(m.h):6.2f}m')

    Draw(donji_deo, gornji_deo, ruza, romeo, tekst_t, tekst_v, tekst_h)

Run(setup, update, draw)