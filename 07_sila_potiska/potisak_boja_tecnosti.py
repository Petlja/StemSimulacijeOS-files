import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
visina_suda = 1.9 
sud_d = 0.03    # debljina zidova suda
dno_y = -2.1    # y koordinata dna (y koordinata povrsine tecnosti je 0)

boje = { 
    "алкохол" : "#e9ebf0", 
    "уље" : "#decc04", 
    "вода" : "#afd1ed", 
    "жива" : "#686d75" 
}

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, dno_y), 6, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.течност = InputList("алкохол", ("алкохол", "уље", "вода", "жива"))
    m.boja_tecnosti = boje[m.течност]
    m.y = -1 # visina dna bureta je -1, bure pluta

def update(m):
    m.y = dno_y # stavljamo bure na dno
    Finish()

def draw(m):
    pozadina = Box((0, dno_y), 6, 4)
    pozadina.fill_color = '#ffffff'
    
    tecnost = Box((0, dno_y), 2, -dno_y)
    tecnost.fill_color = m.boja_tecnosti
    
    sud = Box((0.5, m.y), 1.0, visina_suda)
    sud.fill_color = '#753904'
    
    sud_unutra = Box((0.5 + sud_d, m.y + sud_d), 1 - 2*sud_d, visina_suda - sud_d)
    if m.y + visina_suda >= 0: # ako pluta
        sud_unutra.fill_color = sud.fill_color
    else: # potonuo
        sud_unutra.fill_color = m.boja_tecnosti

    Draw(pozadina, tecnost, sud, sud_unutra)


Run(setup, update, draw)