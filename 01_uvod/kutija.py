from simanim import *

def setup(m):
    m.x = 0
    m.y = 0
    m.v = 10


def update(m):
    m.x += m.v * m.dt


def draw(m):
    kutija = Box((m.x,m.y), 20, 10)
    kutija.fill_color = '#ff8800'
    Draw(kutija)


Run(setup, update, draw)