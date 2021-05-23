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
    m.uspori = InputList(1, [1, 2, 5, 10]) # usporava simulaciju zadati broj puta

    m.h_oblak = [0] * br_oblaka
    for i in range(br_oblaka):
        m.h_oblak[i] = y0_oblak[i]

    m.x_avion = 1
    m.h_avion = 1
    m.v = m.v0 # brzina padobranca (tj. svega ostalog u odnosu na padobranca)
    m.g = 10
    m.a = m.g
    m.Fg = 0
    m.Fotp = 0
    m.avion_vidljiv = True
    m.padobran = False
    m.s_ravn = 0
    m.grafik = [(g_x0, g_y0 + 0.25 * m.v)]

def update(m):
    t = m.t / m.uspori
    dt = m.dt / m.uspori
    if m.update_count % 10 == 0:
        m.grafik += [(g_x0 + 2 * t, g_y0 + 0.25 * m.v)]
    
    if t >= 1.0: # posle koliko vremena otvara padobran
        m.padobran = True

    m.Fg = masa * m.g
    m.Fotp = k_otp * m.v if m.padobran else 0
    m.a = (m.Fg - m.Fotp) / masa
    dh = m.v * dt + m.a * dt * dt / 2
    dv = m.a * dt

    # azuriranje stanja

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

    # uslov za kraj je 3.3 sekunde priblizno ravnomernog kretanja
    if abs(m.a) < 0.001:
        m.s_ravn += dh
        if m.s_ravn >= 3.3:
            Finish()


def crtaj_uspravan_vektor(x, y, d, boja):
    if d != 0:
        vec = Arrow((x, y), (x, y + d))
        vec.pen_color = boja
        vec.line_width = 0.05
        vec.head_len = 0.2 if abs(d) > 0.2 else abs(d)/2
        Draw(vec)


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
    
    # tekstualni podaci
    tekst_v = Text((6.4, 7.0), f'v    ={abs(m.v):6.2f}')
    tekst_v.pen_color = '#000000'
    tekst_v.font_size = 0.5
    tekst_fg = Text((6.4, 6.5), f'Fg   ={abs(m.Fg):6.2f}')
    tekst_fg.pen_color = '#0000ff'
    tekst_fotp = Text((6.4, 6.0), f'Fotp ={abs(m.Fotp):6.2f}')
    tekst_fotp.pen_color = '#ff0000'
    tekst_fr = Text((6.4, 5.5), f'Fr   ={abs(m.Fg-m.Fotp):6.2f}')
    tekst_fr.pen_color = '#008000'
    Draw(tekst_v, tekst_fg, tekst_fotp, tekst_fr)
    crtaj_uspravan_vektor(6.0, 3.3, m.Fotp, '#ff0000') # uvis
    crtaj_uspravan_vektor(6.0, 3.3, -m.Fg, '#0000ff') # na dole
    crtaj_uspravan_vektor(6.1, 3.3, m.Fotp-m.Fg, '#008000')
    crtaj_uspravan_vektor(6.2, 3.3, -0.25*m.v, '#000000') # na dole
    # tekst_a = Text((7, 7), f'a ={m.a:6.2f}')
    # Draw(tekst_a)
    
    # grafik
    grafik_ose = Image('parachute_coordinates.png', (0, 0), scena_w, 4)
    grafik = PolyLine(m.grafik)
    grafik.pen_color = '#000000'
    grafik.line_width = 0.02
    grafik.line_dashed = True
    Draw(grafik_ose, grafik)

    # padobranac
    padobran = Image('parachute.png', (4, 4), 2, 2)
    if m.padobran:
        Draw(padobran)
    padobranac = Image('bird.png', (4, 2.5), 2, 2)
    Draw(padobranac)


Run(setup, update, draw)