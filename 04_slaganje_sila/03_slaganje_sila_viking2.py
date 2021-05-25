import math
from simanim import *

dubina_mora = 9
dno_broda = -1.1 # y koordinata dna slike broda
scena_w, scena_h  = 50, 30
brod_w, brod_h =  12, 9

def setup(m):
    PixelsPerUnit(15)
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

    ## koordinate i razmera vektora pri crtanju 
    # (razmera je ovde odnos intenziteta vektora i njegove duzine)
    kf = 0.0008     # 1N (jedan Njutn) u duznim jedinicama simulacije
    ka = 0.7 * kf   # 1m/s² u duznim jedinicama simulacije
    x_f = m.x + brod_w/2 # x koordinata napadne tacke (poceci svih vektora)
    y_a = 15        # y koordinata vektora ubrzanja na slici
    y_frez = 10
    y_fvesla = dno_broda + 0.5
    y_fstruja = dno_broda

    # vektor sile struje
    crtaj_vodoravan_vektor(x_f, y_fstruja, m.f_struje*kf, '#ff0000')
    str_struja = f'Fs={abs(0.001*m.f_struje):0.0f}KN'
    tekst_struja = Text((x_f + m.f_struje*kf - 1, y_fstruja - 2), str_struja)
    tekst_struja.pen_color = '#ff0000'
    tekst_struja.font_size = 2
    Draw(tekst_struja)

    # vektor sile vesala
    crtaj_vodoravan_vektor(x_f, y_fvesla, m.f*kf, '#ffff00')
    tekst_vesla = Text((x_f, y_fvesla - 2), f'F={(0.001*m.f):0.1f}KN')
    tekst_vesla.pen_color = '#ffff00'
    Draw(tekst_vesla)

    # vektor rezultante
    crtaj_vodoravan_vektor(x_f, y_frez, (m.f_struje + m.f)*kf, '#008000')
    str_frez = f'Frez={(0.001*abs(m.f_struje+m.f)):0.1f}KN'
    if abs(m.a) < 0.3:
        if m.f_struje + m.f > 0:
            str_frez += ' (на десно)'
        elif m.f_struje + m.f < 0:
            str_frez += ' (на лево)'
    tekst_frez = Text((x_f, y_frez + 2), str_frez)
    tekst_frez.pen_color = '#008000'
    Draw(tekst_frez)
        

    # vektor ubrzanja
    crtaj_vodoravan_vektor(x_f, y_a, (m.f_struje + m.f)*ka, '#ffffff')
    str_a = f'a={abs(m.a):0.2f}m/s²'
    if abs(m.a) < 0.3:
        if m.a > 0:
            str_a += ' (на десно)'
        elif m.a < 0:
            str_a += ' (на лево)'
    tekst_a = Text((x_f, y_a + 2), str_a)
    tekst_a.pen_color = '#ffffff'
    tekst_m = Text((x_f, y_a + 4), f'm={m.brod_masa}Kg')
    Draw(tekst_a, tekst_m)

Run(setup, update, draw)
