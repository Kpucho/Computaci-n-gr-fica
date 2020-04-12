import pygame
from plano import *


def dibujarfigura(rotarAng):

    #Figura lateral-Perfil-------------------------
    #figura L
    a1 = [0, 0, 0]
    a2 = [0, 160, 0]
    a3 = [0, 160, 100]
    a4 = [0, 120, 100]
    a5 = [0, 120, 40]
    a6 = [0, 0, 40]
    acara = [a1, a2, a3, a4, a5, a6]

    #mitad grande
    j1 = [70, 0, 0]
    j2 = [70, 80, 0]
    j3 = [70, 80, 40]
    j4 = [70, 0, 40]
    jcara = [j1, j2, j3, j4]

    #mitad pequenita
    k1 = [80, 120, 80]
    k2 = [80, 160, 80]
    k3 = [80, 160, 100]
    k4 = [80, 120, 100]
    kcara = [k1, k2, k3, k4]

    #Figura frontal-------------------------------------------
    #figura 1.1 pequenita
    b1 = [0, 0, 0]
    b2 = [0, 0, 40]
    b3 = [30, 0, 40]
    b4 = [30, 0, 0]
    bcara = [b1, b2, b3, b4]

    #figura 1.2
    c1 = [70, 0, 0]
    c2 = [70, 0, 40]
    c3 = [100, 0, 40]
    c4 = [100, 0, 0]
    ccara = [c1, c2, c3, c4]

    #figura Centro en medio de las figuras 1.1 y 1.2
    d1 = [30, 80, 0]
    d2 = [30, 80, 40]
    d3 = [70, 80, 40]
    d4 = [70, 80, 0]
    dcara = [d1, d2, d3, d4]

    #figura castillo
    e1 = [0, 120, 40]
    e2 = [0, 120, 100]
    e3 = [20, 120, 100]
    e4 = [20, 120, 80]
    e5 = [80, 120, 80]
    e6 = [80, 120, 100]
    e7 = [100, 120, 100]
    e8 = [100, 120, 40]
    ecara = [e1, e2, e3, e4, e5, e6, e7, e8]

    #--------------------------------------------------------
    #plano superior
    #figura
    f1 = [0, 120, 100]
    f2 = [0, 160, 100]
    f3 = [20, 160, 100]
    f4 = [20, 120, 100]
    fcara = [f1, f2, f3, f4]

    #figura
    g1 = [80, 120, 100]
    g2 = [80, 160, 100]
    g3 = [100, 160, 100]
    g4 = [100, 120, 100]
    gcara = [g1, g2, g3, g4]

    #superior en medio de pequenitas
    h1 = [20, 120, 80]
    h2 = [20, 160, 80]
    h3 = [80, 160, 80]
    h4 = [80, 120, 80]
    hcara = [h1, h2, h3, h4]

    #superior mitad en forma mitad h
    i1 = [0, 0, 40]
    i2 = [0, 120, 40]
    i3 = [100, 120, 40]
    i4 = [100, 0, 40]
    i5 = [70, 0, 40]
    i6 = [70, 80, 40]
    i7 = [30, 80, 40]
    i8 = [30, 0, 40]
    icara = [i1, i2, i3, i4, i5, i6, i7, i8]


    #====================FIGURA================================
    #ListaCaras
    listCarasFrontalExc = [dcara]
    listCarasLateralExc = [jcara]
    listCarasSuperiorExc = [hcara]
    listCarasFrontal = [bcara, ccara, ecara]
    listCarasLateral = [acara, kcara]
    listCarasSuperior = [fcara, gcara, icara]

    #Dibujar figura isometrica
    ang = [30 + rotarAng, 150 + rotarAng]
    dibujarCaras(ventana, listCarasFrontalExc, AZUL, ang)
    dibujarCaras(ventana, listCarasLateralExc,  VERDE, ang)
    dibujarCaras(ventana, listCarasSuperiorExc, AMARILLO, ang)
    dibujarCaras(ventana, listCarasSuperior, AMARILLO, ang)
    dibujarCaras(ventana, listCarasFrontal, AZUL, ang)
    dibujarCaras(ventana, listCarasLateral, VERDE, ang)

    #====================Vistas===========================

    #VISTA SUPERIOR
    dibujarVistaSuperior([fcara, gcara, icara, hcara], rotarAng)

    #VISTA LATERAL
    colores = [VERDE, VERDE, AZUL, AZUL, AZUL, AZUL, VERDE]
    dibujarVistaLateral([kcara, jcara, dcara, ecara, bcara, ccara, acara], rotarAng, colores)

    #VISTA FRONTAL
    colores =[AZUL, AZUL, AZUL, VERDE, VERDE, VERDE, AZUL]
    dibujarVistaFrontal([dcara, ccara, ecara, acara, jcara, kcara, bcara], rotarAng, colores)


def aplanarZ(listaPuntos, ang):
    listanueva = []
    for punto in listaPuntos:
        puntonuevo = RotarAntiHorario(PuntoPantalla([punto[0], punto[1]]), ang)
        puntonuevo = Traslacion(puntonuevo, [750, 210])
        listanueva.append(puntonuevo)
    return listanueva

def dibujarVistaSuperior(caras, ang):
    for cara in caras:
        caranueva = aplanarZ(cara, ang)
        pygame.draw.polygon(ventana, AMARILLO, caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)

def aplanarX(listaPuntos, ang):
    listanueva = []
    a = np.radians(180 + ang)
    b = np.radians(ang)
    for punto in listaPuntos:
        x = int(punto[1]*np.cos(a)) - int(punto[0]*np.sin(b))
        puntonuevo = PuntoPantalla([x, punto[2]])
        puntonuevo = Traslacion(puntonuevo, [910, 500])
        listanueva.append(puntonuevo)
    return listanueva

def dibujarVistaLateral(caras, ang, colores):
    i=0
    for cara in caras:
        caranueva = aplanarX(cara, ang)
        pygame.draw.polygon(ventana, colores[i], caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)
        i+=1

def aplanarY(listaPuntos, ang):
    listanueva = []
    a = np.radians(ang)
    for punto in listaPuntos:
        x = int(punto[0]*np.cos(a)) - int(punto[1]*np.sin(a))
        puntonuevo = PuntoPantalla([x, punto[2]])
        puntonuevo = Traslacion(puntonuevo, [750, 650])
        listanueva.append(puntonuevo)
    return listanueva

def dibujarVistaFrontal(caras, ang, colores):
    i=0
    for cara in caras:
        caranueva = aplanarY(cara, ang)
        pygame.draw.polygon(ventana, colores[i], caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)
        i+=1

def dibujarCaras(ventana, caras, color, ang):
    for cara in caras:
        caranueva = listPuntos3dA2d(cara, ang)
        pygame.draw.polygon(ventana, color, caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)

def listPuntos3dA2d(list3d, ang):
    list2d = []
    for punto3d in list3d:
        punto2d = p3dA2d(punto3d, ang)
        list2d.append(punto2d)
    return list2d

def p3dA2d(v, ang):
    a = np.radians(ang[0])
    b = np.radians(ang[1])
    x = int(v[0]*np.cos(a)) + int(v[1]*np.cos(b))
    y = int(v[0]*np.sin(a)) + int(v[1]*np.sin(b) + v[2])
    return PuntoPantalla([x, y])



if __name__ == '__main__':

    pygame.init()
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Puto el que lo lea")
    reloj=pygame.time.Clock()


    dibujarfigura(0)

    fin=False
    while not fin:
        for event in pygame.event.get():
            #Gestion de eventos
            if event.type == pygame.QUIT:
                fin=True

            #control

            #Refresco
            # ventana.fill(NEGRO)
            pygame.display.flip()
            reloj.tick(60)
