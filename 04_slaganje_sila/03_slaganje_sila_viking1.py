import math
from simanim import *

dubina_mora = 9
dno_broda = -0.9 # y koordinata dna broda
scena_w, scena_h  = 50, 30
brod_w, brod_h =  12, 9

def setup(m):
    PixelsPerUnit(10)
    ViewBox((0, -dubina_mora), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.f = InputFloat(10_000, (0, 20_000))  # sila koja potice od veslanja
    
    m.f_vetra = 10_000
    m.brod_masa = 10_000
    m.a = (m.f_vetra + m.f) / m.brod_masa
    m.v = 0 # brzina broda na desno
    m.x = 0 # leva tacka broda

def update(m):
    dx = m.v * m.dt + m.a * m.dt * m.dt / 2
    dv = m.a * m.dt
    m.x += dx
    m.v += dv
    
    if m.x + brod_w >= 50:
        Finish()

def draw(m):
    nebo = Box((0, 0), scena_w, scena_h - dubina_mora)
    nebo.fill_color = '#c6d3dc'
    more = Box((0, -dubina_mora), scena_w, dubina_mora)
    more.fill_color = '#8b9dc4'
    oblaci = Image("viking_back.png", (0, 0), scena_w, scena_h - dubina_mora)
    brod = Image("viking_ship.png", (m.x, dno_broda), brod_w, brod_h)
    Draw(nebo, more, oblaci, brod)

    ## koordinate i razmera vektora pri crtanju 
    # (razmera je ovde odnos intenziteta vektora i njegove duzine na sceni)
    kf = 0.0008     # 1N (jedan Njutn) u duznim jedinicama simulacije
    ka = 0.7 * kf   # 1m/s² u duznim jedinicama simulacije
    x_f = m.x + brod_w/2 # x koordinata napadnih tacaka (poceci svih vektora)
    y_a = 15    # y koordinata vektora ubrzanja na sceni
    y_fvetar = dno_broda + 3 * brod_h / 4 # y koord. vektora sile vetra 
    y_frez = dno_broda + 2 * brod_h / 4   # y koord. vektora rezultantne sile
    y_fvesla = dno_broda # y koord. vektora sile veslaca

    # vektor sile vetra
    vec_vetar = Arrow((x_f, y_fvetar), (x_f + m.f_vetra*kf, y_fvetar))
    vec_vetar.pen_color = '#0000ff'
    vec_vetar.line_width = 0.4
    vec_vetar.head_len = 1
    str_vetar = f'Fv={(0.001*m.f_vetra):0.0f}KN'
    tekst_vetar = Text((x_f + m.f_vetra*kf + 1, y_fvetar), str_vetar)
    tekst_vetar.pen_color = vec_vetar.pen_color
    tekst_vetar.font_size = 2
    Draw(vec_vetar, tekst_vetar)

    # vektor sile vesala
    if m.f*kf > 1:
        vec_vesla = Arrow((x_f, y_fvesla), (x_f + m.f*kf, y_fvesla))
        vec_vesla.pen_color = '#ffff00'
        str_vesla = f'F={(0.001*m.f):0.1f}KN'
        tekst_vesla = Text((x_f + m.f*kf + 1, y_fvesla), str_vesla)
        tekst_vesla.pen_color = vec_vesla.pen_color
        Draw(vec_vesla, tekst_vesla)

    # vektor rezultante
    vec_rez = Arrow((x_f, y_frez), (x_f + (m.f_vetra + m.f)*kf, y_frez))
    vec_rez.pen_color = '#008000'
    str_rez = f'Frez={(0.001*(m.f_vetra+m.f)):0.1f}KN'
    tekst_frez = Text((x_f + (m.f_vetra + m.f)*kf + 1, y_frez), str_rez)
    tekst_frez.pen_color = vec_rez.pen_color
    Draw(vec_rez, tekst_frez)

    # vektor ubrzanja
    vec_a = Arrow((x_f, y_a), (x_f + (m.f_vetra + m.f)*ka, y_a))
    vec_a.pen_color = '#ffffff'
    str_a = f'a={m.a:0.2f}m/s²'
    tekst_a = Text((x_f + (m.f_vetra + m.f)*ka + 1, y_a), str_a)
    tekst_a.pen_color = vec_a.pen_color
    tekst_m = Text((x_f, y_a + 2), f'm={m.brod_masa}Kg')
    Draw(vec_a, tekst_a, tekst_m)

Run(setup, update, draw)