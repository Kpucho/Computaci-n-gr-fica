import pygame
from plano import *

# rotarAng ---> int
#   angulo de cuanto se mueve la figura con respecto a su posicion original
def dibujarfigura(rotarAng, escalar):
    #-----------------POLIGONOS DE LA VISTA LATERAL O PERFIL
    #Define los puntos de cada poligono o cara
    #figura L

    a1 = [0, 0, 0]
    a2 = [0, Y_Figura, 0]
    a3 = [0, Y_Figura, Z_Figura]
    a4 = [0, 3*Y_Figura/4, Z_Figura]
    a5 = [0, 3*Y_Figura/4, 2*Z_Figura/5]
    a6 = [0, 0, 2*Z_Figura/5]

    #Define la lista de puntos que conforma el poligono o cara
    acara = [a1, a2, a3, a4, a5, a6] #mitad grande
    j1 = [7*X_Figura/10, 0, 0]
    j2 = [7*X_Figura/10, Y_Figura/2, 0]
    j3 = [7*X_Figura/10, Y_Figura/2, 2*Z_Figura/5]
    j4 = [7*X_Figura/10, 0, 2*Z_Figura/5]
    jcara = [j1, j2, j3, j4]

    #mitad pequenita
    k1 = [4*X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    k2 = [4*X_Figura/5, Y_Figura, 4*Z_Figura/5]
    k3 = [4*X_Figura/5, Y_Figura, Z_Figura]
    k4 = [4*X_Figura/5, 3*Y_Figura/4, Z_Figura]
    kcara = [k1, k2, k3, k4]

    #----------------POLIGONOS DE LA VISTA FRONTAL O ALZADO
    #figura 1.1 pequenita
    b1 = [0, 0, 0]
    b2 = [0, 0, 2*Z_Figura/5]
    b3 = [3*X_Figura/10, 0, 2*Z_Figura/5]
    b4 = [3*X_Figura/10, 0, 0]
    bcara = [b1, b2, b3, b4]

    #figura 1.2
    c1 = [7*X_Figura/10, 0, 0]
    c2 = [7*X_Figura/10, 0, 2*Z_Figura/5]
    c3 = [X_Figura, 0, 2*Z_Figura/5]
    c4 = [X_Figura, 0, 0]
    ccara = [c1, c2, c3, c4]

    #figura Centro en medio de las figuras 1.1 y 1.2
    d1 = [3*X_Figura/10, Y_Figura/2, 0]
    d2 = [3*X_Figura/10, Y_Figura/2, 2*Z_Figura/5]
    d3 = [7*X_Figura/10, Y_Figura/2, 2*Z_Figura/5]
    d4 = [7*X_Figura/10, Y_Figura/2, 0]
    dcara = [d1, d2, d3, d4]

    #figura castillo
    e1 = [0, 3*Y_Figura/4, 2*Z_Figura/5]
    e2 = [0, 3*Y_Figura/4, Z_Figura]
    e3 = [X_Figura/5, 3*Y_Figura/4, Z_Figura]
    e4 = [X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    e5 = [4*X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    e6 = [4*X_Figura/5, 3*Y_Figura/4, Z_Figura]
    e7 = [X_Figura, 3*Y_Figura/4, Z_Figura]
    e8 = [X_Figura, 3*Y_Figura/4, 2*Z_Figura/5]
    ecara = [e1, e2, e3, e4, e5, e6, e7, e8]

    #----------------POLIGONOS DE LA VISTA SUPERIOR O PLANTA
    #figura
    f1 = [0, 3*Y_Figura/4, Z_Figura]
    f2 = [0, Y_Figura, Z_Figura]
    f3 = [X_Figura/5, Y_Figura, Z_Figura]
    f4 = [X_Figura/5, 3*Y_Figura/4, Z_Figura]
    fcara = [f1, f2, f3, f4]

    #figura
    g1 = [4*X_Figura/5, 3*Y_Figura/4, Z_Figura]
    g2 = [4*X_Figura/5, Y_Figura, Z_Figura]
    g3 = [X_Figura, Y_Figura, Z_Figura]
    g4 = [X_Figura, 3*Y_Figura/4, Z_Figura]
    gcara = [g1, g2, g3, g4]

    #superior en medio de pequenitas
    h1 = [X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    h2 = [X_Figura/5, Y_Figura, 4*Z_Figura/5]
    h3 = [4*X_Figura/5, Y_Figura, 4*Z_Figura/5]
    h4 = [4*X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    hcara = [h1, h2, h3, h4]

    #superior mitad en forma mitad h
    i1 = [0, 0, 2*Z_Figura/5]
    i2 = [0, 3*Y_Figura/4, 2*Z_Figura/5]
    i3 = [X_Figura, 3*Y_Figura/4, 2*Z_Figura/5]
    i4 = [X_Figura, 0, 2*Z_Figura/5]
    i5 = [7*X_Figura/10, 0, 2*Z_Figura/5]
    i6 = [7*X_Figura/10, Y_Figura/2, 2*Z_Figura/5]
    i7 = [3*X_Figura/10, Y_Figura/2, 2*Z_Figura/5]
    i8 = [3*X_Figura/10, 0, 2*Z_Figura/5]
    icara = [i1, i2, i3, i4, i5, i6, i7, i8]

    #----------------POLIGONOS DE LA VISTA CONTRARIO LATERAL

    l1 = [3*X_Figura/10,0,0]
    l2 = [3*X_Figura/10,Y_Figura/2,0]
    l3 = [3*X_Figura/10,Y_Figura/2,2*Z_Figura/5]
    l4 = [3*X_Figura/10,0,2*Z_Figura/5]
    lcara = [l1, l2, l3, l4]

    m1 = [X_Figura/5, 3*Y_Figura/4, 4*Z_Figura/5]
    m2 = [X_Figura/5, Y_Figura, 4*Z_Figura/5]
    m3 = [X_Figura/5, Y_Figura, Z_Figura]
    m4 = [X_Figura/5, 3*Y_Figura/4, Z_Figura]
    mcara = [m1, m2, m3, m4]

    n1 = [X_Figura, 0, 0]
    n2 = [X_Figura, Y_Figura, 0]
    n3 = [X_Figura, Y_Figura, Z_Figura]
    n4 = [X_Figura, 3*Y_Figura/4, Z_Figura]
    n5 = [X_Figura, 3*Y_Figura/4, 2*Z_Figura/5]
    n6 = [X_Figura, 0, 2*Z_Figura/5]
    ncara = [n1, n2, n3, n4, n5, n6]

    #----------------POLIGONOS DE LA VISTA CONTRARIA FRONTAL

    o1 = [0, Y_Figura, 0]
    o2 = [0, Y_Figura, Z_Figura]
    o3 = [X_Figura/5, Y_Figura, Z_Figura]
    o4 = [X_Figura/5, Y_Figura, 4*Z_Figura/5]
    o5 = [4*X_Figura/5, Y_Figura, 4*Z_Figura/5]
    o6 = [4*X_Figura/5, Y_Figura, Z_Figura]
    o7 = [X_Figura, Y_Figura, Z_Figura]
    o8 = [X_Figura, Y_Figura, 0]
    ocara = [o1, o2, o3, o4, o5, o6, o7, o8]

    #====================DIBUJAR FIGURA ISOMETRICA=============================
    #Angulos de perspectiva
    # angulo de perspectiva con respecto a X
    persx = 45
    # angulo de perspectiva con respecto a Y
    persy = 135
    #Ang---> vector ang[0], ang[1]
    #   angulos para la perspectiva, ademas se suma el angulo de rotacion por si
    #   se mueve la figura
    ang = [persx + rotarAng, persy + rotarAng]

    #Depende del angulo, hay ciertas caras visibles para la figura
    # 300 ---> 60
    if (rotarAng <= (90 - persx) or rotarAng >= (270 + 180 - persy)):
        listacolores = [AZUL, VERDE, AMARILLO, AMARILLO, AMARILLO, AMARILLO, AZUL, AZUL, AZUL, VERDE, VERDE]
        listacaras = [dcara, jcara, hcara, fcara, gcara, icara, bcara, ccara, ecara, acara, kcara]
    # 60--->120
    elif (rotarAng > (90 - persx) and rotarAng <= (90 + 180 - persy)):
        listacolores = [VERDE, AMARILLO, AMARILLO, VERDE, AMARILLO, AMARILLO, ROSADO, VERDE]
        listacaras = [jcara, icara, hcara, kcara, fcara, gcara, ocara, acara]
    # 120 ---> 240
    elif (rotarAng > (90 + 180 - persy) and rotarAng <= (270 -persx)):
        listacolores = [ROJO, AMARILLO, AMARILLO, ROJO, AMARILLO, AMARILLO, ROSADO, ROJO]
        listacaras = [lcara, icara, hcara, mcara, fcara, gcara, ocara, ncara]
    # 240 --->300
    elif (rotarAng > (270 -persx) and rotarAng < (270 + 180 - persy)):
        listacolores = [AZUL, AMARILLO, AMARILLO, AMARILLO, AMARILLO, AZUL, AZUL, AZUL, ROJO, ROJO, ROJO]
        listacaras = [dcara, icara, hcara, fcara, gcara, bcara, ccara, ecara, ncara, mcara, lcara]

    #dibujar Plano X
    pygame.draw.line(ventana, Cplano, PolarPantalla(3*X_Figura/2, (180 + persx)), PolarPantalla(3*X_Figura/2, persx))
    #dibujar plano Y
    pygame.draw.line(ventana, Cplano, PolarPantalla(3*Y_Figura/2, persy), PolarPantalla(3*Y_Figura/2, 180 + persy))

    dibujarCaras(ventana, listacaras, listacolores, ang, escalar)

    #dibujar plano Z
    if(rotarAng >= persy and rotarAng <= 270 - persx):
        pygame.draw.line(ventana, Cplano, PuntoPantalla([0, 40]), PuntoPantalla([0, 250]))
    else:
        pygame.draw.line(ventana, Cplano,  PuntoPantalla([0,0]), PuntoPantalla([0, 250]))

    #====================Vistas===========================

    #VISTA SUPERIOR
    #No importa el orden de la lista
    dibujarVistaSuperior([fcara, gcara, icara, hcara], rotarAng)

    #Depende del angulo, hay ciertas caras visibles para cada vista
    if (rotarAng >= 0 and rotarAng <= 90):
        colores = [VERDE, VERDE, ROSADO]
        dibujarVistaLateral([kcara, acara, ocara], rotarAng, colores)
        colores = [VERDE, VERDE, AZUL, AZUL, AZUL, AZUL, VERDE]
        dibujarVistaFrontal([kcara, jcara, dcara, ecara, bcara, ccara, acara], rotarAng, colores)
    elif (rotarAng > 90 and rotarAng <= 180):
        colores = [ROJO, ROJO, ROSADO]
        dibujarVistaLateral([mcara, ncara, ocara], rotarAng, colores)
        colores = [VERDE, VERDE, ROSADO]
        dibujarVistaFrontal([kcara, acara, ocara], rotarAng, colores)
    elif (rotarAng > 180 and rotarAng <= 270):
        colores = [ROJO, ROJO, AZUL, AZUL, AZUL, AZUL, ROJO]
        dibujarVistaLateral([mcara, lcara, dcara, ecara, bcara, ccara, ncara], rotarAng, colores)
        colores = [ROJO, ROJO, ROSADO]
        dibujarVistaFrontal([mcara, ncara, ocara], rotarAng, colores)
    elif (rotarAng > 270 and rotarAng < 360):
        colores = [VERDE, VERDE, AZUL, AZUL, AZUL, AZUL, VERDE]
        dibujarVistaLateral([kcara, jcara, dcara, ecara, bcara, ccara, acara], rotarAng, colores)
        colores = [ROJO, ROJO, AZUL, AZUL, AZUL, AZUL, ROJO]
        dibujarVistaFrontal([mcara, lcara, dcara, ecara, bcara, ccara, ncara], rotarAng, colores)



# =================FUNCIONES PARA LA VISTA SUPERIOR=============================
#listas de caras organizadas con prioridad
#los colores van en paralelo a la lista de caras
#Transforma un poligono superior de coordenadas 3d a 2d
#listaPuntos ---> lista de puntos del poligono o cara
#ang ---> es el angulo de rotacion (Por si se mueve la figura, cambia las vistas)
#return ---> listas de puntos ya en coordenadas 2d pantalla
def aplanarZ(listaPuntos, ang):
    listanueva = []
    for punto in listaPuntos:
        #rotar figura con un punto fijo por que la vista superior nunca cambia
        puntonuevo = RotarAntiHorario(PuntoPantalla([punto[0], punto[1]]), ang)
        puntonuevo = Traslacion(puntonuevo, VistaSuperior)
        listanueva.append(puntonuevo)
    return listanueva


#Dibuja la caras superiores
#caras ---> lista de poligonos o caras superiores
#ang -----> entero, angulo de rotacion
def dibujarVistaSuperior(caras, ang):
    for cara in caras:
        caranueva = aplanarZ(cara, ang)
        pygame.draw.polygon(ventana, AMARILLO, caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)



# =================FUNCIONES PARA LA VISTA LATERAL=============================

#Transforma un poligono lateral o frontal de coordenadas 3d a 2d (en plano lateral)
#listaPuntos ---> lista de puntos del poligono o cara
#ang ---> es el angulo de rotacion (Por si se mueve la figura, cambia las vistas)
#return ---> listas de puntos ya en coordenadas 2d pantalla
def aplanarX(listaPuntos, ang):
    listanueva = []
    #angulos para la transformacion
    a = np.radians(180 + ang)
    b = np.radians(ang)
    for punto in listaPuntos:
        #Transformar la coordenada y, x en una sola, que seria x
        x = int(punto[1]*np.cos(a)) - int(punto[0]*np.sin(b))
        puntonuevo = PuntoPantalla([x, punto[2]])
        puntonuevo = Traslacion(puntonuevo, VistaLateral)
        listanueva.append(puntonuevo)
    return listanueva
#Dibuja la caras que se ven en la vista lateral
#caras ---> lista de poligonos o caras tanto laterales y superiores
#       Estas estan organizadas en un especifico para que quede bien dibujado
#ang -----> entero, angulo de rotacion
#colores ----> una lista lista de colores que van en paralelo a lista de poligonos o caras
def dibujarVistaLateral(caras, ang, colores):
    i=0
    for cara in caras:
        caranueva = aplanarX(cara, ang)
        pygame.draw.polygon(ventana, colores[i], caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)
        i+=1


# =================FUNCIONES PARA LA VISTA FRONTAL=============================

#Transforma un poligono lateral o frontal de coordenadas 3d a 2d (en plano frontal)
#listaPuntos ---> lista de puntos del poligono o cara
#ang ---> es el angulo de rotacion (Por si se mueve la figura, cambia las vistas)
#return ---> listas de puntos ya en coordenadas 2d pantalla
def aplanarY(listaPuntos, ang):
    listanueva = []
    #Angulo necesario para la transformacion
    a = np.radians(ang)
    for punto in listaPuntos:
        x = int(punto[0]*np.cos(a)) - int(punto[1]*np.sin(a))
        puntonuevo = PuntoPantalla([x, punto[2]])
        puntonuevo = Traslacion(puntonuevo, VistaFrontal)
        listanueva.append(puntonuevo)
    return listanueva

#Dibuja la caras que se ven en la vista lateral
#caras ---> lista de poligonos o caras tanto laterales y superiores
#       Estas estan organizadas en un especifico para que quede bien dibujado
#ang -----> entero, angulo de rotacion
#colores ----> una lista lista de colores que van en paralelo a lista de poligonos o caras
def dibujarVistaFrontal(caras, ang, colores):
    i=0
    for cara in caras:
        caranueva = aplanarY(cara, ang)
        pygame.draw.polygon(ventana, colores[i], caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)
        i += 1


# Dibuja toda la figura mediante una listas de poligonos o pequenas caras
# estos poligonos estan conformados por puntos
# ventana ---> en donde se va a dibujar
# caras ----> Lista de poligonos ej: listas de Caras Superior
# color -----> Lista de colores que identifica esa lista de caras
# ang -----> vector ang[0], ang[1] (para dar perpectiva a la figura)
# escalar----> incrementa o decrementa el tamano de la figura
def dibujarCaras(ventana, caras, color, ang, escalar):
    i = 0
    for cara in caras:
        caranueva = listPuntos3dA2d(cara, ang)
        caranueva = escalarLista(caranueva, escalar)
        pygame.draw.polygon(ventana, color[i], caranueva)
        pygame.draw.lines(ventana, NEGRO, True, caranueva)
        i += 1

#Transforma una lista de puntos 3d a 2d
# list3d ---> lista de puntos 3d (Cada uno esta en coordenadas cartesianas)
# ang ----> es un vector ang[0] y ang[1], Es para intentar darle perspectiva
#   ang[0] ----> este suele ser el de 45 + anguloRotacion
#   ang[1] ----> este suele ser el de 135 + anguloRotacion
#   Sin embargo estos angulos se definen justo antes de llamar la funcion dibujarcaras
# return ---> retorna una lista de puntos 2d en coordenadas pantalla
def listPuntos3dA2d(list3d, ang):
    list2d = []
    for punto3d in list3d:
        punto2d = p3dA2d(punto3d, ang)
        list2d.append(punto2d)
    return list2d

# Transforma un punto 3d a 2d
# v ----> v[0] = x,  v[1] = y,  v[2]= z (coordenadas 3d cartesianas)
# ang---> vector de angulos para dar perspectiva
#return retorna coordenadas 2d pantalla
def p3dA2d(v, ang):
    a = np.radians(ang[0])
    b = np.radians(ang[1])
    x = int(v[0]*np.cos(a)) + int(v[1]*np.cos(b))
    y = int(v[0]*np.sin(a)) + int(v[1]*np.sin(b) + v[2])
    return PuntoPantalla([x, y])

#Escala una lista de puntos punto pantalla
#ListaPuntos ----> lista puntos de coordenadas pantalla
#Escalar ----> numero con el que se multiplica cada punto
#return ---> retorna una lista de puntos en coordenadas pantalla ya escalados

def escalarLista(listaPuntos, escalar):
    listanueva = []
    for punto in listaPuntos:
        punto = Escalar(punto, escalar)
        listanueva.append(punto)
    return listanueva

def corregirAnguloRotacion(angulo):
    if(angulo < 0):
        angulo += 360
    elif(angulo >= 360):
        angulo = angulo - 360
    return angulo


if __name__ == '__main__':
    pygame.time.set_timer(Itstime, 1000)
    pygame.init()
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    ventana.fill(Cpantalla)
    pygame.display.set_caption("Pillese esta rikura")
    reloj=pygame.time.Clock()

    ang = 0
    escalar = 1
    # DEATH = False

    fin=False
    while not fin:
        for event in pygame.event.get():
            #Gestion de eventos
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    ang += 10
                if event.button == 4:
                    ang -= 10
                if event.button == 1:
                    escalar += 0.1
                if event.button == 2:
                    escalar = 1
                if event.button == 3:
                    escalar -= 0.1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Cpantalla == BLANCO:
                        Cpantalla = NEGRO
                        Cplano = BLANCO
                    else:
                        Cpantalla = BLANCO
                        Cplano = NEGRO
                if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                    if DEATH == True:
                        DEATH = False
                    else:
                        DEATH = True
            if event.type ==Itstime:
                if DEATH == True:
                    if Cpantalla == BLANCO:
                        Cpantalla = NEGRO
                        Cplano = BLANCO
                    else:
                        Cpantalla = BLANCO
                        Cplano = NEGRO



            #control
            #

            ang = corregirAnguloRotacion(ang)
            #Refresco
            ventana.fill(Cpantalla)
            dibujarfigura(ang, escalar)
            pygame.display.flip()
            reloj.tick(60)
