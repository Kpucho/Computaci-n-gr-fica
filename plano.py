import pygame
import math as np

TamanoCudrito = 45
Theta = 30
Alfa = 135
ANCHO = 700
ALTO = 700
ORIGEN =  [ANCHO/2, 1.5*ALTO/3]
BLANCO = [150, 150, 150]
NOSE = [218, 3, 255]
VERDE = [0, 247, 0]
AZUL = [0, 0, 255]
AMARILLO = [255, 255,0]
ROJO = [255,0,0]
NEGRO = [0,0,0]
#Traslacion para cada vista
Tfrontal = [-200,-300]
Tsuperior = [30,-350]
Tlateral = [340,-300]

#x' = x + z
#y' = y - z
def _3d_to_2d(Pto):
    Pto2d = [Pto[0]+Pto[2],Pto[1]-Pto[2]]
    return Pto2d

#x' = XCos(theta) + ZSin(theta)
#y' = Y
#z' = ZCos(theta) - XSen(theta)
def RotarEnY(Pto, Angulo):
    Angulo = np.radians(Angulo)
    x = Pto[0]*np.cos(Angulo) + Pto[2]*np.sin(Angulo)
    z = Pto[2]*np.cos(Angulo) - Pto[0]*np.sin(Angulo)

def Vistar(Move,List,ventana, COLOR):
    caraux = []
    for i in List:
        #traslado = [0, -Distancia(i)*np.tan(Angulo(i))]
        #aux = Traslacion(i, traslado)
        caraux.append(Traslacion(i,Move))
    pygame.draw.polygon(ventana, COLOR, caraux)

def Distancia(Pto1):
    Pto1 = PuntoCartesiano(Pto1)
    Distance = np.sqrt(np.pow(Pto1[0],2)+np.pow(Pto1[1],2))
    return Distance

def Angulo(Pto):
    if Pto[0] == 0:
        if Pto[1] == 0:
            return 0
        else:
            return 90
    return np.atan(Pto[1]/Pto[0])

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

def RotarHorario(v, pos, a):
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


def Traslacion(pos, t):
    pos = PuntoCartesiano(pos)
    x = pos[0] + t[0]
    y = pos[1] + t[1]
    return PuntoPantalla([x, y])

def Escalar(punto, valor):
    punto = PuntoCartesiano(punto);
    punto[0] = punto[0] * valor
    punto[1] = punto[1] * valor

    return punto

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

def PolarCartesiano(p):
    a = np.radians(p[1])
    x = int(p[0]*np.cos(a))
    y = int(p[0]*np.sin(a))

    return PuntoPantalla([x, y])

def Polar(r, a):
    p = [r, a]
    pr = RotarAntiHorario(v, p, 30)
    return pr
