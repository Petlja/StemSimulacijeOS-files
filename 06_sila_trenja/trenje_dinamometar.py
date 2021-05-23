import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.F = InputFloat(15, (10, 30))


def update(m):
    Finish()


def draw(m):
    pozadina = Box((0, 0), 10, 6)
    pozadina.fill_color = '#3698bf' # plava

    dinm_w = 1.6 # traka dinamometra od 16 crta zauzima dinm_w duznih jedinica
    k_dinm = dinm_w/32 # 1N je dinm_w/32 duznih jedinica

    x1 = 4
    kutija = Image('dynamometer_case.png', (x1, 2.6), dinm_w, 0.5)
    traka = Image('dynamometer_stripes.png', (x1 + k_dinm * m.F, 2.6), dinm_w, 0.5)
    Draw(pozadina, traka, kutija)


Run(setup, update, draw)
