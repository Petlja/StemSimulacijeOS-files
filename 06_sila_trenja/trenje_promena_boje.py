import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.mi = InputFloat(0.2, (0.15, 0.4)) # koeficijent trenja klizanja

def update(m):
    Finish()

def hex_boja(k):
    r, g, b = int(k*218), int(k*241), int(k*248)
    return f'#{r:02x}{g:02x}{b:02x}'

def draw(m):
    pozadina = Box((0, 0), 10, 6)
    pozadina.fill_color = '#3698bf' # neka plava

    pod = Box((0, 0), 10, 2.5)
    pod.fill_color = hex_boja(1 - m.mi) # tamnija za vece trenje

    Draw(pozadina, pod)

Run(setup, update, draw)
