import math
from simanim import *

# konstante:
scena_w, scena_h = 4.6, 6
ruza_w, ruza_h = 0.25, 0.5

h0 = 0.2 # visina poda (prikazana kao 0)
h_b = 3.15 # Visina donje tacke balona u slici

def setup(m):
    PixelsPerUnit(72)
    ViewBox((0, 0), 5, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(20)

    m.v0 = InputFloat(10, (0.1, 29.9)) # pocetna brzina na dole
    m.H = InputFloat(3.3,(2.3,4.3)) # rastojanje od pocetne pozicije balona do poda

    m.h = m.H + h0 # visina (donje tacke) balona u simulaciji
    m.y_gornje_sl = m.h - h_b
    m.v = m.v0 # m.v ce biti brzina nanize
    m.g = 10 # koristimo g = 10 da bi se rezultat slagao sa jednostavnijim racunanjem

def update(m):
    dv = m.g * m.dt
    dh = - m.v * m.dt - m.g * m.dt * m.dt / 2

    m.h += dh
    m.v += dv
    if m.h < h0:
        m.h = h0 # ne nize od poda

    if m.h <= h0:
        Finish()

def draw(m):
    sl_dole = Image("romeo3_lower.png", (0, 0), scena_w, scena_h)
    sl_gore = Image("romeo3_upper.png", (0, m.y_gornje_sl), scena_w, scena_h)
    sl_tata = Image("romeo3_upper_b.png", (0, m.y_gornje_sl), scena_w, scena_h)
    balon = Image("romeo3_balloon.png", (0, m.h - h_b), scena_w, scena_h)
    romeo = Image("romeo3_romeo.png", (0, 0), scena_w, scena_h)

    tekst_t = Text((2.8, 5.7), f't ={m.t:6.2f}s')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 0.25
    tekst_v = Text((2.8, 5.5), f'v ={abs(m.v):6.2f}m/s')
    tekst_h = Text((2.8, 5.3), f'h ={(m.h-h0):6.2f}m')

    Draw(sl_dole, sl_gore, sl_tata, romeo, balon, tekst_t, tekst_v, tekst_h)

Run(setup, update, draw)