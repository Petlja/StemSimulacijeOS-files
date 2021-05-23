from simanim import *

def setup(m):
    PixelsPerUnit(5)
    ViewBox((-10, -30),150, 90)
    FramesPerSecond(15)
    UpdatesPerFrame(1)
    BackgroundColor('#99ccff')

    m.x0 = InputFloat(10,(0,40))
    m.y = InputFloat(15,(5,30))
    m.v = InputList(10,[5,10,15,20])

    m.x = m.x0

def update(m):
    m.x += m.v * m.dt

    if m.t >= 5:
        Finish()

def draw(m):
    podloga = Box((-10,-30), 160,30)
    podloga.fill_color = '#00cc00'
    Draw(podloga)

    oblak_deo1 = Circle((90,40),10)
    oblak_deo1.fill_color = '#ccffff'
    oblak_deo2 = Circle((105,40),15)
    oblak_deo3 = Circle((120,40),10)
    Draw(oblak_deo1, oblak_deo2, oblak_deo3)

    slika_w = 20
    slika_h = slika_w * 193/222
    slika_x = m.x - slika_w/2
    slika_y = m.y - slika_h/8
    ptica = Image('ptica-leti-udesno.png', (slika_x, slika_y), slika_w, slika_h)
    vec_v = Arrow((m.x, m.y), (m.x + m.v, m.y))
    vec_v.pen_color = '#0000a0'
    vec_v.line_width = 0.5
    vec_v.head_len = 2
    Draw(ptica, vec_v)

    t_x = Text((0, 55), f'x ={m.x:5.1f}')
    t_x.pen_color = '#000000'
    t_y = Text((0, 50), f'y ={m.y:5.1f}')
    t_t = Text((0, 45), f't ={m.t:5.1f}')
    t_v = Text((0, 40), f'v ={m.v:5.1f}')
    t_v.pen_color = vec_v.pen_color
    Draw(t_x, t_y, t_t, t_v)

Run(setup, update, draw)
