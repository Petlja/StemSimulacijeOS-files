import math
from simanim import *
auto_w, auto_h = 4.3, 2

def setup(m):
    PixelsPerUnit(20)
    ViewBox((0, 0), 40, 20)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.uspori = InputList(1, [1, 2, 5, 10]) # usporava simulaciju zadati broj puta
    m.v = 10 # brzina
    m.x_auta = 0
    m.x_pozadine = 0


def update(m):
    t = m.t / m.uspori
    dt = m.dt / m.uspori
    m.x_auta += m.v * dt

    if t >= 3:
        Finish()


def draw(m):
    t = m.t / m.uspori
    
    pozadina = Image('trees.jpg', (m.x_pozadine, 0), 100, 20)
    auto = Image('automobile.png', (m.x_auta, 0), auto_w, auto_h)
    tekst_t = Text((20, 15), f't ={t:6.2f}')
    tekst_t.pen_color = '#000000'
    tekst_t.font_size = 3
    Draw(pozadina, auto, tekst_t)


Run(setup, update, draw)