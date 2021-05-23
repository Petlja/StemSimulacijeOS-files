import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
visina_suda = 1.9 
sud_d = 0.03    # debljina zidova suda
dno_h = -2.1    # y koordinata dna (y koordinata povrsine tecnosti je 0)
g = 10          # ubrzanje zemljine teze

gustine = { 
    "алкохол" : 700, 
    "уље" : 800, 
    "вода" : 1000, 
    "жива" : 13530 
}
boje = { 
    "алкохол" : "#e9ebf0", 
    "уље" : "#decc04", 
    "вода" : "#afd1ed", 
    "жива" : "#686d75" 
}

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, dno_h), 6, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.маса_тега = InputFloat(1000, (100, 21000))
    m.течност = InputList("алкохол", ("алкохол", "уље", "вода", "жива"))
    m.boja_tecnosti = boje[m.течност]
    m.ro = gustine[m.течност]

    m.v_u_tecnosti = 0 # zapremina uronjenog dela bureta
    m.F_potiska = 0
    m.h = 0 # polozaj dna bureta, na pocetku je na povrsini tecnosti

def update(m):
    m.h = m.маса_тега / (s0 * m.ro)
    m.v_u_tecnosti = m.h * s0
    m.F_potiska = m.h * s0 * m.ro * g

    if  m.h > visina_suda:
        m.h = -dno_h
        m.v_u_tecnosti = visina_suda * s0
        m.F_potiska = 0 # u sud je usla tecnost, nema potiska
        
    Finish()

def draw(m):
    pozadina = Box((0, dno_h), 6, 4)
    pozadina.fill_color = '#ffffff'
    
    tecnost = Box((0, dno_h), 2, -dno_h)
    tecnost.fill_color = m.boja_tecnosti
    
    sud = Box((0.5, -m.h), 1.0, visina_suda)
    sud.fill_color = '#753904'
    
    teg_w, teg_h = 0.33, 0.38
    teg = Image("weight.png", (1 - teg_w/2, -m.h), teg_w, teg_h)

    Draw(pozadina, tecnost, sud, teg)

    v_ukupno = Text((2.2, 0.2), f'V ={(visina_suda * s0):6.2f} m³')  
    v_ukupno.pen_color = '#000000'
    v_ukupno.font_size = 0.25
    t_zap = Text((2.2, 0.0), f'v ={m.v_u_tecnosti:6.2f} m³')

    t_fp = Text((2.2, -0.8), f'Fp ={abs(0.001*m.F_potiska):6.2f} KN')
    t_mg = Text((2.2, -1.0), f'mg ={abs(0.001*g*m.маса_тега):6.2f} KN')

    Draw(v_ukupno, t_zap, t_fp, t_mg)


Run(setup, update, draw)