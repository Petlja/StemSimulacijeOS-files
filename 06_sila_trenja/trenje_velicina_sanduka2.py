import math
from simanim import *

def setup(m):
    PixelsPerUnit(60)
    ViewBox((0, 0), 10, 6)
    FramesPerSecond(30)
    UpdatesPerFrame(1)

    m.masa = InputFloat(1.5, (1, 3))


def update(m):
    Finish()


def draw(m):
    sanduk_vel = (2 * m.masa) ** (1/3)
    sanduk = Image('box.png', (1, 1), sanduk_vel, sanduk_vel)
    Draw(sanduk)


Run(setup, update, draw)

