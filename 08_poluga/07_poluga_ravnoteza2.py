import math
from simanim import *

krak_tereta = 1   # m
masa_tereta = 100 # Kg

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 5, 2)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.крак = InputList(1.0, (0.5, 0.8, 1.0, 1.25)) # m  2000 1250 1000 800
    m.сила = InputList(300.0, (600.0, 750.0, 800.0, 1200.0)) # N

    m.f = 0
    m.g = 10
    m.rez_moment = 0

def update(m):
    moment_tereta = masa_tereta * m.g * krak_tereta
    moment_sile = m.крак * m.сила
    # ukupan moment sile jednak je razlici datih momenata 
    # jer nasa sila i teret deluju na razlicitim stranama poluge
    m.rez_moment = moment_tereta - moment_sile
    Finish()


def draw(m):
    osl_w, osl_h = 0.12, 1.5        # velicina slike oslonca
    poluga_w, poluga_h = 4.2, 0.02  # velicina slike poluge
    teret_w, teret_h = 0.43, 0.68   # velicina slike tereta
    x0, y0 = 1.5, 1.6               # koordinate vrha oslonca

    pozadina = Box((0, 0), 6, 2)
    pozadina.fill_color = '#ffffff'
    oslonac = Image("support.png", (x0 - osl_w/2, y0 - osl_h), osl_w, osl_h)
    Draw(pozadina, oslonac)
    
    # crtanje poluge (klackalice), racunanje napadnih tacaka tereta i sile
    # napadna tacka tereta je (xt, yt)
    # napadna tacka sile kojom delujemo je (xs, ys)
    ugao = 0.1
    w_koso, h_koso = 0.995, 0.0998
    poluga = Image("lever.png", (x0 - krak_tereta * 1.1, y0), poluga_w, poluga_h)
    if m.rez_moment < -0.01: # preteze desno
        xt, yt = x0 - krak_tereta * w_koso, y0 + krak_tereta * h_koso
        xs, ys = x0 + m.крак * w_koso, y0 - m.крак * h_koso
        with Rotate((x0, y0), ugao):
            Draw(poluga)
    elif m.rez_moment > 0.01: # preteze levo
        xt, yt = x0 - krak_tereta * w_koso, y0 - krak_tereta * h_koso
        xs, ys = x0 + m.крак * w_koso, y0 + m.крак * h_koso
        with Rotate((x0, y0), -ugao):
            Draw(poluga)
    else: # ravnoteza
        xt, yt = x0 - krak_tereta, y0
        xs, ys = x0 + m.крак, y0
        Draw(poluga)
    
    teret = Image("load.png", (xt-teret_w/2, yt-teret_h), teret_w, teret_h)
    Draw(teret)

    # vektori sile
    k = 1/2000 # razmera: sili od 1N odgovara vektor-strelica duzine k
    vec_q = Arrow((xt, yt), (xt, yt - masa_tereta * m.g * k))
    vec_q.pen_color = '#ff0000'
    vec_q.line_width = 0.01
    vec_q.head_len = 0.04
    t_q = Text((xt + 0.02, yt - masa_tereta * m.g * k), 'Q')
    t_q.font_size = 0.1
    t_q.pen_color = vec_q.pen_color
    Draw(vec_q, t_q)
    if abs(k * m.сила) >= 0.05:
        vec_sila = Arrow((xs, ys), (xs, ys - m.сила * k))
        vec_sila.pen_color = '#0000ff'
        t_f = Text((xs + 0.02, ys - m.сила * k), 'F')
        t_f.pen_color = vec_sila.pen_color
        Draw(vec_sila, t_f)

    tekst_m = Text((xt-teret_w/2+0.1, yt-teret_h+0.06), f'{masa_tereta:3.0f}Kg')
    tekst_m.font_size = 0.1
    tekst_m.pen_color = '#000000'
    tekst_k = Text((x0 - 0.6*krak_tereta,  y0 + 0.2), f'{krak_tereta:3.0f}m')
    tekst_k.font_size = 0.15
    Draw(tekst_m, tekst_k)


Run(setup, update, draw)