from simanim import *

def setup(m):
    PixelsPerUnit(5)
    ViewBox((-10, -10), 120, 60)

    m.h = 30
    m.v = 0
    m.g = 9.81

def update(m):
    dv = m.g * m.dt 
    dh = - (m.v * m.dt + m.g * m.dt ** 2 / 2)

    m.v += dv
    m.h += dh

    if m.h <= 0:
        Finish()

def draw(m):
    telo = Box((0,m.h),10,10)
    telo.fill_color = '#777777'
    txt_t = Text((40, 30), f't ={m.t:6.3f}s')
    txt_t.pen_color = '#009900'
    Draw(telo, txt_t)

Run(setup, update, draw)