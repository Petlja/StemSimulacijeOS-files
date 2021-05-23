import math
from simanim import *

masa = 100
brod_w, brod_h = 1.5, 1.5
strelica_w, strelica_h = 0.5, 0.5

def setup(m):
    PixelsPerUnit(50)
    ViewBox((-5, -5), 10, 10)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.smer = InputList("gore", ["gore", "desno", "dole", "levo"])
    m.x = 0
    m.y = 0

def update(m):
    Finish()

def draw(m):
    brod = Image('spaceship.png', (m.x - brod_w/2, m.y - brod_h/2), brod_w, brod_h)
    Draw(brod)

    x0 = m.x - brod_w/2 - strelica_w
    y0 = m.y - strelica_h/2
    strelica = Image('strelica_na_levo.png', (x0, y0), strelica_w, strelica_h)
    if m.smer == "levo":
        ugao = 0
    elif m.smer == "desno":
        ugao = math.pi
    elif m.smer == "dole":
        ugao = -math.pi/2
    elif m.smer == "gore":
        ugao = math.pi/2

    with Rotate((m.x, m.y), ugao):
        Draw(strelica)

Run(setup, update, draw)
