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
    m.x = 0
    m.y = 0

def update(m):
    Finish()

def draw(m):
    mreza = Image('grid.png', (-5, -5), 10, 10)
    brod = Image('spaceship.png', (m.x - brod_w/2, m.y - brod_h/2), brod_w, brod_h)
    
    a_w, a_h  = 0.005 * m.Fa, 0.5 # velicina slike vatre iz motora A
    b_w, b_h  = 0.005 * m.Fb, 0.5 # velicina slike vatre iz motora B
    c_w, c_h  = 0.005 * m.Fc, 0.5 # velicina slike vatre iz motora C
    d_w, d_h  = 0.005 * m.Fd, 0.5 # velicina slike vatre iz motora D
    vatra_a = Image('jet_fire.png', (m.x - brod_w/2 - a_w, m.y - a_h/2), a_w, a_h)
    vatra_b = Image('jet_fire.png', (m.x - brod_w/2 - b_w, m.y - b_h/2), b_w, b_h)
    vatra_c = Image('jet_fire.png', (m.x - brod_w/2 - c_w, m.y - c_h/2), c_w, c_h)
    vatra_d = Image('jet_fire.png', (m.x - brod_w/2 - d_w, m.y - d_h/2), d_w, d_h)
    Draw(mreza, brod)

    if a_w > 0:
        with Rotate((m.x, m.y), math.pi/2):
            Draw(vatra_a)
    if b_w > 0:
        with Rotate((m.x, m.y), math.pi):
            Draw(vatra_b)
    if c_w > 0:
        with Rotate((m.x, m.y), -math.pi/2):
            Draw(vatra_c)
    if d_w > 0:
        Draw(vatra_d)

Run(setup, update, draw)
