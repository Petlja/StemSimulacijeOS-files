import math
from simanim import *

def setup(m):
    PixelsPerUnit(100)
    ViewBox((98, 9), 4, 2)
    FramesPerSecond(30)
    UpdatesPerFrame(1)
    m.x = InputFloat(100.0, (95.0, 105.0))
    m.y = InputFloat(10.0, (5.0, 15.0))

def update(m):
    Finish()


def draw(m):
    linija = Line((0, 0), (100, 0))
    linija.pen_color = '#000000'
    linija.line_width = 0.02
    with Rotate((0, 0), -0.1):
        Draw(linija)

    gore = Line((m.x, m.y + 0.1), (m.x, m.y + 0.5)) 
    gore.pen_color = '#ff0000'
    dole = Line((m.x, m.y - 0.1), (m.x, m.y - 0.5)) 
    levo = Line((m.x - 0.1, m.y), (m.x - 0.5, m.y))
    desno = Line((m.x + 0.1, m.y), (m.x + 0.5, m.y))
    Draw(gore, dole, levo, desno)


Run(setup, update, draw)