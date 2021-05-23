import math
from simanim import *

masa = 0.1
k_otp = 0.5 # koeficijent otpora
x_oblak = (0.9, 3.2, 3.7, 6.6, 8.1)
y0_oblak = (2.5, 7.6, 3.3, 9.2, 5.3)
br_oblaka = len(x_oblak)
g_x0, g_y0 = 0.3, 0.3 # koordinatni pocetak grafika
scena_w, scena_h = 10, 8
oblak_w, oblak_h = 2, 0.8

def setup(m):
    PixelsPerUnit(50)
    ViewBox((0, 0), scena_w, scena_h)
    FramesPerSecond(30)
    UpdatesPerFrame(10)

    m.v0 = InputFloat(7, (0, 20)) # pocetna brzina

    m.h_oblak = [0] * br_oblaka
    for i in range(br_oblaka):
        m.h_oblak[i] = y0_oblak[i]

    m.x_avion = 1
    m.h_avion = 1
    m.v = m.v0 # brzina padobranca (tj. svega ostalog u odnosu na padobranca)
    m.g = 10
    m.a = m.g # pozitivno kada je vektor ubrzanja usmeren na dole
    m.avion_vidljiv = True
    m.padobran = False
    m.s_ravn = 0

def update(m):
    if m.t >= 1.0: # posle koliko vremena otvara padobran
        m.padobran = True

    f = masa * m.g
    f_otp = k_otp * m.v if m.padobran else 0
    m.a = (f - f_otp) / masa
    dh = m.v * m.dt + m.a * m.dt * m.dt / 2
    dv = m.a * m.dt

    # visini objekata dodajemo dh jer smo u ref. sistemu padobranca,
    # tj. padobranac stoji a sve ostalo se krece suprotno (na gore)
    for i in range(br_oblaka):
        m.h_oblak[i] += dh
        if m.h_oblak[i] > scena_h:
            m.h_oblak[i] -= (scena_h + oblak_h) # "novi oblak"

    if m.avion_vidljiv:
        m.x_avion += 0.05
        m.h_avion += dh
        if m.x_avion > scena_w or m.h_avion > scena_h:
            m.avion_vidljiv = False

    m.v += dv

    if abs(m.a) < 0.001:
        m.s_ravn += dh
        if m.s_ravn >= 3.3:
            Finish()

def draw(m):
    # pozadina
    pozadina = Box((0, 0), scena_w, scena_h)
    pozadina.fill_color = '#cadade'
    Draw(pozadina)
    
    # oblaci
    for i in range(br_oblaka):
        ime_slike = 'cloud' + str(i) + '.png'
        oblak = Image(ime_slike, (x_oblak[i], m.h_oblak[i]), oblak_w, oblak_h)
        Draw(oblak)
    
    # avion
    if m.avion_vidljiv:
        avion = Image('plane.png', (m.x_avion, m.h_avion), 8, 4)
        Draw(avion)
    # zemlja
    zemlja = Box((0, 0), scena_w, m.s_ravn)
    zemlja.fill_color = '#d9c9b6'
    Draw(zemlja)
    
    tekst_v = Text((7, 7.5), f'v ={abs(m.v):6.2f}')
    tekst_v.pen_color = '#000000'
    tekst_v.font_size = 0.5
    Draw(tekst_v)

    # padobranac
    padobran = Image('parachute.png', (4, 4), 2, 2)
    if m.padobran:
        Draw(padobran)
    padobranac = Image('bird.png', (4, 2.5), 2, 2)
    Draw(padobranac)


Run(setup, update, draw)