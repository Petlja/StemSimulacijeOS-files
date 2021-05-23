from simanim import *

def setup(m):
    PixelsPerUnit(5)
    ViewBox((-10, -10), 120, 60)
    UpdatesPerFrame(100)

    m.h = InputFloat(30, (10,40))
    m.v = 0
    m.g = 9.81

def update(m):
    dv = m.g * m.dt 
    dh = - (m.v * m.dt + m.g * m.dt ** 2 / 2)

    m.v += dv
    m.h += dh

    if m.h <= 0:
        m.h = 0
        Finish()

def draw(m):
    podloga = Box((-10,-10),120,10)
    podloga.fill_color = '#00AA00'
    telo = Box((0,m.h),10,10)
    telo.fill_color = '#777777'
    Draw(podloga,telo)

    txt_h = Text((50, 35), f'h ={m.h:6.3f}m')
    txt_h.pen_color = '#009900'
    txt_t = Text((50, 30), f't ={m.t:6.3f}s')
    Draw(txt_t, txt_h)

Run(setup, update, draw)