import math
from simanim import *

krak_tereta = 1   # m
masa_tereta = 100 # Kg

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 5, 2)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.крак = InputFloat(2, (0.1, 3))     # m
    m.сила = InputFloat(400, (100, 3000))  # N

    m.f = 0
    m.g = 10
    m.rez_moment = masa_tereta * m.g * krak_tereta
    m.odgovor = ""

def update(m):
    moment_tereta = masa_tereta * m.g * krak_tereta
    moment_sile = m.крак * m.сила
    # ukupan moment sile jednak je razlici datih momenata 
    # jer nasa sila i teret deluju na razlicitim stranama poluge
    m.rez_moment = moment_tereta - moment_sile

    if m.rez_moment < -0.01:
        m.odgovor = "Десна страна претеже"
    elif m.rez_moment > 0.01:
        m.odgovor = "Лева страна претеже"
    else:
        m.odgovor = "Равнотежа"
    Finish()


def draw(m):
    osl_w, osl_h = 0.12, 1.5        # velicina slike oslonca
    poluga_w, poluga_h = 4.2, 0.02  # velicina slike poluge
    teret_w, teret_h = 0.43, 0.68   # velicina slike tereta
    x0, y0 = 1.5, 1.6               # koordinate vrha oslonca
    xt, yt = x0 - krak_tereta, y0   # napadna tacka tereta 
    xs, ys = x0 + m.крак, y0        # napadna tacka sile kojom delujemo 

    pozadina = Box((0, 0), 6, 2)
    pozadina.fill_color = '#ffffff'
    oslonac = Image("support.png", (x0 - osl_w/2, y0 - osl_h), osl_w, osl_h)
    teret = Image("load.png", (xt-teret_w/2, yt-teret_h), teret_w, teret_h)
    
    poluga = Image("lever.png", (x0 - krak_tereta * 1.1, y0), poluga_w, poluga_h)

    tekst_odgovor = Text((x0, y0 + 0.1), m.odgovor)
    tekst_odgovor.pen_color = '#007F00'
    tekst_odgovor.font_size = 0.25
    Draw(pozadina, oslonac, poluga, teret, tekst_odgovor)

    tekst_m = Text((xt-teret_w/2+0.1, yt-teret_h+0.06), f'{masa_tereta:3.0f}Kg')
    tekst_m.pen_color = '#000000'
    tekst_m.font_size = 0.1
    tekst_k = Text((x0 - 0.6*krak_tereta,  y0 + 0.2), f'{krak_tereta:3.0f}m')
    Draw(tekst_m, tekst_k)


Run(setup, update, draw)