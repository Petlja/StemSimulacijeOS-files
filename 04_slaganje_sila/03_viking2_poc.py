import math
from simanim import *

dubina_mora = 9
dno_broda = -0.9 # y koordinata dna broda
scena_w, scena_h  = 50, 30
brod_w, brod_h =  12, 9

def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, -dubina_mora), 50, 30)
    FramesPerSecond(60)
    UpdatesPerFrame(10)

    m.f = InputFloat(10_000, (0, 20_000))  # N
    
    m.f_struje = -10_000
    m.brod_masa = 10_000
    m.a = (m.f_struje + m.f) / m.brod_masa
    m.v = 0 # brzina broda na desno
    m.x = 25 - brod_w/2 # leva tacka broda 
                        # (na pocetku tako da je brod u sredini slike)


def update(m):
    dx = m.v * m.dt + m.a * m.dt * m.dt / 2
    dv = m.a * m.dt
    m.x += dx
    m.v += dv
    
    # ako je brod dotakao levu ili desnu ivicu ekrana, 
    # ili se ne krece, zavrsi simulaciju
    if m.a == 0 or m.x <= 0 or m.x + brod_w >= 50:
        Finish()


def crtaj_vodoravan_vektor(x, y, d, boja):
    if d != 0:
        vec = Arrow((x, y), (x + d, y))
        vec.pen_color = boja
        vec.line_width = 0.3
        vec.head_len = 1 if abs(d) > 1 else abs(d)/2
        Draw(vec)
    

def draw(m):
    nebo = Box((0, 0), scena_w, scena_h - dubina_mora)
    nebo.fill_color = '#c6d3dc'
    more = Box((0, -dubina_mora), scena_w, dubina_mora)
    more.fill_color = '#8b9dc4'
    oblaci = Image("viking_back.png", (0, 0), scena_w, scena_h - dubina_mora)
    brod = Image("viking_ship.png", (m.x, dno_broda), brod_w, brod_h)
    Draw(nebo, more, oblaci, brod)

    kf = 0.0008     # 1N (jedan Njutn) u duznim jedinicama simulacije
    x_f = m.x + brod_w/2 # x koordinata napadne tacke (poceci svih vektora)
    y_frez = 10
    y_fvesla = dno_broda + 0.5
    y_fstruja = dno_broda
    crtaj_vodoravan_vektor(x_f, y_fstruja, m.f_struje*kf, '#ff0000')
    crtaj_vodoravan_vektor(x_f, y_fvesla, m.f*kf, '#ffff00')
    crtaj_vodoravan_vektor(x_f, y_frez, (m.f_struje + m.f)*kf, '#008000')

Run(setup, update, draw)
