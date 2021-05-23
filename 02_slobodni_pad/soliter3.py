import math
from simanim import *

def setup(m):
    PixelsPerUnit(5)
    ViewBox((-10, -10), 140, 70)
    FramesPerSecond(60)
    UpdatesPerFrame(20)

    m.sprat = InputList(10,range(1,11))

    predmeti = {"lopta": ("tocak.svg",1,(5,5), 5**2),
                "loptica": ("tocak.svg",(3/5)**3,(3,3), 3**2)}
    m.predmet = InputList("loptica", predmeti.keys())
    m.telo_img, m.m, (m.telo_w, m.telo_h), m.A = predmeti[m.predmet]

    m.h0 = m.sprat * 5
    m.h = m.h0
    m.v = 0
    planete = {"Mesec":1.62, "Mars":3.71,"Zemlja":9.81, "Neptun":14.07,"Jupiter":25.95 }
    m.planeta = InputList("Zemlja", planete.keys())
    m.g = planete[m.planeta]
    m.a = m.g

    m.prolazna = []

def update(m):
    if m.t >= len(m.prolazna):
        m.prolazna += [(m.t, m.h, m.a)]

    m.h = max(m.h - m.v * m.dt,0)
    m.v += m.g*m.dt 

    if m.h == 0:
        Finish()

def draw(m):
    podloga = Box((-20,-2),220,2)
    podloga.fill_color = '#00BB00'

    soliter = Box((-6,0),6,55)
    soliter.fill_color = '#777777'

    telo = Image(m.telo_img, (1, m.h), m.telo_w, m.telo_h)

    Draw(podloga, soliter, telo)

    for i in range(11):
        prozor=Box((-5,5*i),4,4)
        prozor.fill_color = '#BBBBBB'
        Draw(prozor)

    t_m = Text((90, 50), f'm ={m.m:6.3f}kg')
    t_m.pen_color = '#000000'
    t_g = Text((90, 45), f'g ={m.g:5.2f}m/s²')
    t_t = Text((90, 40), f't ={m.t:6.3f}s')
    t_h = Text((90, 35), f'h ={m.h:6.3f}m')

    Draw(t_m, t_g, t_t, t_h)

    for t, h, a in m.prolazna:
        crtica = Line((6,h), (8,h))
        crtica.pen_color = "#000000"
        txt = Text((9,h-1),f"s={m.h0-h:6.2f}, a ={a:5.2f}, t ={t:5.2f}")
        txt.pen_color = "#880000"
        txt.font_size=4
        Draw(crtica, txt)

Run(setup, update, draw)