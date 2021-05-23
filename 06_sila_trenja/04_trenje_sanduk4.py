import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.mi = InputFloat(0.2, (0.15, 0.4)) # koeficijent trenja klizanja
    m.mi_klizanja = m.mi
    m.mi_mirovanja = m.mi + 0.1
    m.masa = InputFloat(1.5, (1, 2.7))

    m.g = 10
    m.F = 0.0
    m.Ftr = 0.0
    m.Fr = 0.0 # rezultanta sila
    m.v = 0.0
    m.x = 0.0
    m.tabela = []

    max_tr_mir = m.mi_mirovanja * m.masa * m.g
    dF = max_tr_mir / 3
    dF = round(dF*2)/2 # zaokruzeno na 0.5N
    i = 0
    m.sila = []
    while i*dF + 1e-6 < max_tr_mir:
        m.sila.append(i*dF)
        i += 1
    m.sila += [max_tr_mir, max_tr_mir + 0.01]
    if i*dF - 1e-6 < m.sila[-1]:
        i += 1
    m.sila.append(i*dF)
    m.brojac = 0


def update(m):
    if (m.update_count % 20 == 0) and (m.brojac < len(m.sila)):
        # azuriramo obe sile
        m.F = m.sila[m.brojac]
        m.brojac += 1

        mi  = m.mi_mirovanja if m.v == 0 else m.mi_klizanja
        m.Ftr = mi * m.masa * m.g
        if m.Ftr > m.F: # ako vucna sila jos nije dovoljno velika
            m.Ftr = m.F 
        elif m.Ftr < m.F: # ako je telo proklizalo
            m.Ftr = m.mi_klizanja * m.masa * m.g

        m.tabela += [(m.F, m.Ftr)]

    # rez. sila, ubrzanje, brzina, polozaj
    m.Fr = m.F - m.Ftr
    a = m.Fr / m.masa

    dv = a * m.dt
    dx = m.v * m.dt + a * m.dt * m.dt / 2
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


def hex_boja(k):
    r, g, b = map(int, (k*218, k*241, k*248))
    return f'#{r:02x}{g:02x}{b:02x}'


def draw(m):
    pozadina = Box((0, 0), 10, 6)
    pozadina.fill_color = '#3698bf' # plava

    y0 = 2.5
    pod = Box((0, 0), 10, y0)
    pod.fill_color = hex_boja(1 - m.mi) # tamnija za vece trenje
    
    dinm_w = 1.6 # traka dinamometra od 16 crta zauzima dinm_w duznih jedinica
    k_dinm = dinm_w/32 # 1N je dinm_w/32 duznih jedinica
    x0 = 2.5 + m.x
                  
    sanduk_vel = (2 * m.masa) ** (1/3)
    sanduk = Image('box.png', (x0, y0-0.65), sanduk_vel, sanduk_vel)
    x1 = x0 + sanduk_vel
    kutija = Image('dynamometer_case.png', (x1, y0 + 0.1), dinm_w, 0.5)
    traka = Image('dynamometer_stripes.png', (x1 + k_dinm * m.Ftr, y0 + 0.1), dinm_w, 0.5)
    x2 = x1 + k_dinm * m.Ftr + dinm_w
    
    Draw(pozadina, pod, sanduk, traka, kutija)

    # aktivna sila, sila trenja, rezultanta
    k = 0.1
    crtaj_vektor(x2, y0 + 0.35, m.F * k, 0, '#ffff00')
    crtaj_vektor(x0, y0 - 0.1, -m.Ftr * k, 0, '#ff0000')
    crtaj_vektor(x1, y0 - 0.1, m.Fr * k, 0, '#008000')
    
    # uspravne sile
    mg = abs(m.masa * m.g)
    crtaj_vektor(x0 + sanduk_vel/2, y0 + sanduk_vel/2, 0, -k * mg, '#000000') # mg
    crtaj_vektor(x0 + sanduk_vel/2, y0 + sanduk_vel/2, 0, k * mg, '#805000') # N

    tekst_F = Text((6, 1.2), f'  F={abs(m.F):6.2f}N')
    tekst_F.font_size = 0.5
    tekst_F.pen_color = '#ffff00'
    tekst_Ftr = Text((6, 0.7), f'Ftr={abs(m.Ftr):6.2f}N')
    tekst_Ftr.pen_color = '#ff0000'
    tekst_Fr = Text((6, 0.2),  f' Fr={abs(m.Fr):6.2f}N')
    tekst_Fr.pen_color = '#008000'

    tekst_n = Text((0.5, 0.7),  f' N={mg:6.2f}N')
    tekst_n.pen_color = '#805000'
    tekst_mg = Text((0.5, 0.2),  f' mg={mg:6.2f}N')
    tekst_mg.pen_color = '#000000'
    Draw(tekst_F, tekst_Ftr, tekst_Fr, tekst_n, tekst_mg)
    
    xt, yt, dyt = 0.1, 5.70, 0.25
    tekst_pozadina = Box((xt, yt), dyt*10, dyt*0.9)
    tekst_pozadina.fill_color = '#404040'
    tekst_1 = Text((xt, yt), '    F')
    tekst_1.font_size = dyt
    tekst_1.pen_color = '#ffff00'
    tekst_2 = Text((xt, yt), '             Ftr')
    tekst_2.pen_color = '#ff0000'
    Draw(tekst_pozadina, tekst_1, tekst_2)
    tacke_grafika = []
    for  f, ftr in m.tabela:
        tacke_grafika.append( (7 + f/5, 3 + ftr/5) )
        yt -= dyt
        tekst_pozadina = Box((xt, yt), dyt*10, dyt*0.9)
        tekst_pozadina.fill_color = '#404040'
        tekst_1 = Text((xt, yt),  f'{abs(f):6.2f}N')
        tekst_1.pen_color = '#ffff00'
        tekst_2 = Text((xt, yt),  f'         {abs(ftr):6.2f}N')
        tekst_2.pen_color = '#ff0000'
        Draw(tekst_pozadina, tekst_1, tekst_2)

    if len(tacke_grafika) > 0:
        if m.brojac == len(m.sila):
            tacke_grafika.append( (10, tacke_grafika[-1][1]) )
        grafik_ose = Image('friction_force_coordinates.png', (6.7, 2.7), 3.3, 3.3)
        grafik = PolyLine(tacke_grafika)
        grafik.pen_color = '#000000'
        grafik.line_width = 0.02
        grafik.line_dashed = True
        Draw(grafik_ose, grafik)

Run(setup, update, draw)
