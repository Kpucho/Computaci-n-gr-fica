import pygame
import math as np


ANCHO = 1000
ALTO = 700
ORIGEN =  [ANCHO/4, ALTO/2]
Z_Figura = 120
Y_Figura = 160
X_Figura = 120
NOSE = [150, 30, 70] #Color
NEGRO = [0, 0, 0]
VERDE = [0, 255, 0]
ROJO = [255, 0, 0]
AMARILLO = [255, 255, 0]
BLANCO = [255, 255, 255]
AZUL = [0, 0, 255]
ROSADO = [255, 0, 255]
Cpantalla = BLANCO
Cplano = NEGRO
VistaSuperior = [710, 185]
VistaLateral = [810, 460]
VistaFrontal = [710, 610]
Itstime = pygame.USEREVENT
DEATH = False

def Dibujar(v, origen):
    pygame.draw.line(v, BLANCO, [origen[0], 0], [origen[0], ALTO], 1)
    pygame.draw.line(v, BLANCO, [0, origen[1]], [ANCHO, origen[1]], 1)

def PuntoCartesiano(pos):
    x = pos[0] - ORIGEN[0]
    y = ORIGEN[1] - pos[1]
    return [x, y]

def PuntoPantalla(pos):
    x = pos[0] + ORIGEN[0]
    y = ORIGEN[1] - pos[1]
    return [x, y]

def Vector(v, pos, orig):
    pygame.draw.line(v, NOSE, orig, pos, 1)

def Punto(v, pos, color):
    pygame.draw.circle(v, color, pos, 5)

#modificacion --> eliminar variable v innecesaria
def RotarHorario(pos, a):
    pos = PuntoCartesiano(pos)
    a = np.radians(a)
    x = int(pos[0]*np.cos(a) + pos[1]*np.sin(a))
    y = int(pos[1]*np.cos(a) - pos[0]*np.sin(a))
    return PuntoPantalla([x, y])

def RotarAntiHorario(pos, a):
    pos = PuntoCartesiano(pos)
    a = np.radians(a)
    x = int(pos[0]*np.cos(a) - pos[1]*np.sin(a))
    y = int(pos[1]*np.cos(a) + pos[0]*np.sin(a))
    return PuntoPantalla([x, y])

def Escalamiento(v, puntos, m):
    ls = [0] * 3
    for i in range(3):
        x = puntos[i][0] * m
        y = puntos[i][1] * m
        print x, y
        ls[i] = [x, y]

    print ls
    ls[0] = PuntoPantalla(ls[0])
    ls[1] = PuntoPantalla(ls[1])
    ls[2] = PuntoPantalla(ls[2])
    pygame.draw.polygon(v, NOSE, ls, 2)

#modificacion para entre solo puntos cartesianos
def Traslacion(pos, t):
    pos = PuntoCartesiano(pos)
    t = PuntoCartesiano(t)
    x = pos[0] + t[0]
    y = pos[1] + t[1]
    return PuntoPantalla([x, y])

#modificacion para que retorne en puntopantalla
def Escalar(punto, valor):
    punto = PuntoCartesiano(punto);
    punto[0] = punto[0] * valor
    punto[1] = punto[1] * valor

    return PuntoPantalla(punto)

def DibujarEquilatero(v, X):
    Y = RotarAntiHorario(v, X, 120)
    H = RotarAntiHorario(v, Y, 120)
    pygame.draw.line(v, NOSE, X, Y)
    pygame.draw.line(v, NOSE, Y, H)
    pygame.draw.line(v, NOSE, H, X)

def DibujarFiguraRegular(v, X, lados):
    a = 360 / lados
    n = a
    puntos = []
    puntos.append(X)
    i = 0
    while i < lados:
        p = RotarAntiHorario(v, X, n)
        puntos.append(p)
        n += a
        i += 1

    pygame.draw.polygon(v, NOSE, puntos, 2)

def PolarPantalla(radio, ang):
    a = np.radians(ang)
    x = int(radio*np.cos(a))
    y = int(radio*np.sin(a))
    return PuntoPantalla([x, y])

def Polar(r, a):
    p = [r, a]
    pr = RotarAntiHorario(v, p, 30)
    return pr
