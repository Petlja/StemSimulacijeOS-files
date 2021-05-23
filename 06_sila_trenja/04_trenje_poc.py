import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.mi_klizanja = 0.4 # koeficijent trenja klizanja
    m.mi_mirovanja = 0.5 # koeficijent trenja mirovanja
    m.masa = InputFloat(1.5, (1, 3))

    m.g = 10
    m.F = 0.0
    m.Ftr = 0.0
    m.Frez = 0.0 # rezultanta sila
    m.v = 0.0
    m.x = 0.0


def update(m):
    # povecavamo silu vuce dok sanduk ne postigne dovoljnu brzinu (procena)
    if m.v <= 1:
        m.F = m.F + 0.05
    else:
        # nakon postizanja brzine, vucemo minimalnom dovoljnom silom
        m.F = m.mi_klizanja * m.masa * m.g

    if m.v == 0:
        Ftr = min(m.F, m.mi_mirovanja  * m.masa * m.g)
    else:
        Ftr = m.mi_klizanja  * m.masa * m.g

    Frez = m.F - Ftr
    a = Frez / m.masa
    dv = a * m.dt
    dx = m.v * m.dt + a * m.dt * m.dt / 2

    # pamcenje stanja
    m.Ftr = Ftr
    m.Frez = Frez
    m.v += dv
    m.x += dx

    if m.x >= 10:
        Finish()


def crtaj_vektor(x, y, dx, dy, boja):
    d = math.sqrt(dx*dx + dy*dy)
    if d > 0.001:
        vec = Arrow((x, y), (x + dx, y + dy))
        vec.pen_color = boja
        vec.line_width = 0.05
        vec.head_len = 0.2 if d > 0.2 else d/2
        Draw(vec)


def draw(m):
    pozadina = Box((0, 0), 10, 6)
    pozadina.fill_color = '#3698bf' # plava

    y0 = 2.5
    pod = Box((0, 0), 10, y0)
    pod.fill_color = '#8d9ca1'
    
    sanduk = Image('box.png', (2.5 + m.x, 1.85), 2, 2)
    
    tekst_F = Text((6, 1.2), f'  F={abs(m.F):6.2f}N')
    tekst_F.font_size = 0.5
    tekst_F.pen_color = '#ffff00'
    tekst_Ftr = Text((6, 0.7), f'Ftr={abs(m.Ftr):6.2f}N')
    tekst_Ftr.pen_color = '#ff0000'
    tekst_Fr = Text((6, 0.2),  f' Fr={abs(m.Frez):6.2f}N')
    tekst_Fr.pen_color = '#008000'

    Draw(pozadina, pod, sanduk, tekst_F, tekst_Ftr, tekst_Fr)

    # aktivna sila, sila trenja, rezultanta
    k = 0.07
    crtaj_vektor(m.x + 4.5, y0 + 0.35, m.F * k, 0, '#ffff00')
    crtaj_vektor(m.x + 4.5, y0 - 0.1, -m.Ftr * k, 0, '#ff0000')
    crtaj_vektor(m.x + 4.5, y0 - 0.1, m.Frez * k, 0, '#008000')

Run(setup, update, draw)
