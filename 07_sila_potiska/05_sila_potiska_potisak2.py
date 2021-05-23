import math
from simanim import *

s0 = 1          # povrsina poprecnog preseka suda
sud_d = 0.03    # debljina zidova suda
y0 = 0.5        # y koordinata podloge

def setup(m):
    PixelsPerUnit(100)
    ViewBox((0, 0), 6, 4)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.m = InputFloat(1, (0.1, 1.5))
    m.ro = InputFloat(1000, (500, 14000)) # gustina tecnosti

    m.boja_tecnosti = "#afd1ed" # boja tecnosti
    m.izmeren = False
    m.sila_potiska = 0
    m.g = 10
    m.q1 = 0 # u vazduhu
    m.q2 = 0 # u tecnosti

def update(m):
    m.izmeren = True
    v_krune = m.m / 19300 # 19300 je gustina krune
    m.sila_potiska = v_krune * m.ro * m.g
    m.q1 = m.m * m.g
    m.q2 = m.q1 - m.sila_potiska
    Finish()

def crtaj_merenje(m, x0, q):
    dinm_w, dinm_h = 0.25, 1.6
    x2 = x0 - dinm_w / 2
    y1 = y0 + 0.2 # donja ivica slike krune
    y2 = y1 + 1.0 # tacka vesanja krune
    kruna_razmera = (m.m / 1.5) ** (1/3)
    kruna_w, kruna_h = 1 * kruna_razmera, 0.74 * kruna_razmera
    kruna = Image("crown.png", (x0 - kruna_w/2, y1), kruna_w, kruna_h)
    
    kruna_leva_nit = Line((x0 - 0.434*kruna_w, y1 + 0.696*kruna_h), (x0, y2))
    kruna_leva_nit.pen_color = '#ff0000'
    kruna_leva_nit.line_width = 0.02
    kruna_desna_nit = Line((x0 + 0.423*kruna_w, y1 + 0.705*kruna_h), (x0, y2))

    Draw(kruna, kruna_leva_nit, kruna_desna_nit)
    
    dinm_traka = Image('dynamometer_stripes_vertical.png', (x2, y2), dinm_w, dinm_h)
    dinm_kutija = Image('dynamometer_case_vertical.png', (x2, y2 + 0.1 * q), dinm_w, dinm_h)
    
    str_tekst = f'Q ={abs(q):6.2f} N' if m.izmeren else 'Q = ...'
    tekst_q = Text((x0 + 0.2, y2), str_tekst)
    tekst_q.pen_color = '#ffffff'
    tekst_q.font_size = 0.2
    Draw(dinm_traka,  dinm_kutija, tekst_q)


def draw(m):
    vazduh = Box((0, 0), 6, 4)
    vazduh.fill_color = '#3698bf'
    podloga = Box((0, 0), 6, y0)
    podloga.fill_color = '#6e675f'
    Draw(vazduh, podloga)
    
    sud = Box((3.4-sud_d, y0), 1.2 + 2*sud_d, 1.1)
    sud.fill_color = '#c76f0a'    
    tecnost = Box((3.4, y0 + sud_d), 1.2, 1.0)
    tecnost.fill_color = m.boja_tecnosti
    vazduh_u_sudu = Box((3.4, y0 + sud_d + 1.0), 1.2, 0.1 - sud_d)
    vazduh_u_sudu.fill_color = vazduh.fill_color
    Draw(sud, tecnost, vazduh_u_sudu)

    crtaj_merenje(m, 1, m.q1)
    crtaj_merenje(m, 4, m.q2)


Run(setup, update, draw)