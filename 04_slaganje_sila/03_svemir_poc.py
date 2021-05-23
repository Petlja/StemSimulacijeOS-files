import math
from simanim import *

masa = 100
brod_w, brod_h = 1.5, 1.5

def setup(m):
    PixelsPerUnit(50)
    ViewBox((-5, -5), 10, 10)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.Fa = InputFloat(0, (0, 200))
    m.Fb = InputFloat(0, (0, 200))
    m.Fc = InputFloat(0, (0, 200))
    m.Fd = InputFloat(0, (0, 200))

    m.Fx = m.Fd - m.Fb # sila na desno
    m.ax = m.Fx / masa # ubrzanje na desno
    m.vx = 0
    m.x = 0

    m.Fy = m.Fc - m.Fa # sila na gore
    m.ay = m.Fy / masa # ubrzanje na gore
    m.vy = 0
    m.y = 0


def update(m):
    dx = m.vx * m.dt + m.ax * m.dt * m.dt / 2
    dvx = m.ax * m.dt

    dy = m.vy * m.dt + m.ay * m.dt * m.dt / 2
    dvy = m.ay * m.dt
    
    m.x += dx
    m.vx += dvx
    m.y += dy
    m.vy += dvy

    if m.x < -5 or m.x >= 5 or m.y < -5 or m.y >= 5:
        Finish()


def draw(m):
    mreza = Image('grid.png', (-5, -5), 10, 10)
    brod = Image('spaceship.png', (m.x - brod_w/2, m.y - brod_h/2), brod_w, brod_h)
    
    trag = Line((0, 0), (m.x, m.y))
    trag.pen_color = '#ffffff'
    trag.line_width = 0.1
    trag.line_dashed = True
    Draw(mreza, trag, brod)


Run(setup, update, draw)
