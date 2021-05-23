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


def crtaj_vektor(x, y, dx, dy, boja):
    dd = dx*dx + dy*dy
    if dd > 0:
        vec = Arrow((x, y), (x + dx, y + dy))
        vec.pen_color = boja
        vec.line_width = 0.1
        vec.head_len = 0.3 if dd > 0.3*0.3 else math.sqrt(dd)/2
        Draw(vec)


def draw(m):
    mreza = Image('grid.png', (-5, -5), 10, 10)
    brod = Image('spaceship.png', (m.x - brod_w/2, m.y - brod_h/2), brod_w, brod_h)
    
    a_w, a_h  = 0.005 * m.Fa, 0.5 # velicina slike vatre iz motora A
    b_w, b_h  = 0.005 * m.Fb, 0.5 # velicina slike vatre iz motora B
    c_w, c_h  = 0.005 * m.Fc, 0.5 # velicina slike vatre iz motora C
    d_w, d_h  = 0.005 * m.Fd, 0.5 # velicina slike vatre iz motora D
    a = Image('jet_fire.png', (m.x - brod_w/2 - a_w, m.y - a_h/2), a_w, a_h)
    b = Image('jet_fire.png', (m.x - brod_w/2 - b_w, m.y - b_h/2), b_w, b_h)
    c = Image('jet_fire.png', (m.x - brod_w/2 - c_w, m.y - c_h/2), c_w, c_h)
    d = Image('jet_fire.png', (m.x - brod_w/2 - d_w, m.y - d_h/2), d_w, d_h)
    trag = Line((0, 0), (m.x, m.y))
    trag.pen_color = '#ffffff'
    trag.line_width = 0.1
    trag.line_dashed = True
    Draw(mreza, trag, brod)

    if a_w > 0:
        with Rotate((m.x, m.y), math.pi/2):
            Draw(a)
    if b_w > 0:
        with Rotate((m.x, m.y), math.pi):
            Draw(b)
    if c_w > 0:
        with Rotate((m.x, m.y), -math.pi/2):
            Draw(c)
    if d_w > 0:
        Draw(d)
    # izdvojen prikaz vektora sila i njihovog slaganja
    max_vec = max(abs(m.Fa), abs(m.Fb), abs(m.Fc), abs(m.Fd))
    if max_vec > 0:
        x0, y0, k = -3.5, -3.5, 1/max_vec
        crtaj_vektor(x0, y0, 0, -k * m.Fa, '#ff0000') # A
        crtaj_vektor(x0, y0, -k * m.Fb, 0, '#ff8000') # B
        crtaj_vektor(x0, y0, 0, k * m.Fc,  '#ff0000') # C
        crtaj_vektor(x0, y0, k * m.Fd, 0,  '#ff8000') # D
        crtaj_vektor(x0, y0, k*(m.Fd-m.Fb), k*(m.Fc-m.Fa), '#008000') # rez

Run(setup, update, draw)
