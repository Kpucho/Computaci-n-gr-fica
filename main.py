import pygame
from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
fin = False

##################################        PUNTOS    #################################################

#Figura 1

A1 = PuntoPantalla([0, 0])  #Centro
PolarA2 = PolarCartesiano([80, Alfa]) #Inferior izquierdo
PolarA3 = PolarCartesiano([40, Theta]) #Inferior  derecho
A2 = Traslacion(PolarA2, PuntoCartesiano(A1))
A3 = Traslacion(PolarA3, PuntoCartesiano(A1))
A4 = Traslacion(A1, [0,30]) #Superior Centro
A5 = Traslacion(A2, [0,30]) #Superior izquierdo
A6 = Traslacion(A3, [0,30]) #Superior Derecho
A7 = Traslacion(PolarA2, PuntoCartesiano(A6)) #Superior trasero
A8 = Traslacion(PolarA2, PuntoCartesiano(A3)) #Inferior trasero

poligono1 = [A1, A2, A8, A7, A5, A4, A6, A3, A6, A7, A5, A2, A1, A3, A1, A4, A1]

traslado = PuntoCartesiano(PolarCartesiano([100, Theta]))

#Figura 1.1
B1 = Traslacion(A1, traslado) #Centro
B2 = Traslacion(A2, traslado) #Inferior izquierdo
B3 = Traslacion(A3, traslado) #Inferior  derecho
B4 = Traslacion(A4, traslado) #Superior Centro
B5 = Traslacion(A5, traslado) #Superior izquierdo
B6 = Traslacion(A6, traslado) #Superior Derecho
B7 = Traslacion(A7, traslado) #Superior trasero
B8 = Traslacion(A8, traslado) #Inferior trasero

poligono2 = [B1, B2, B8, B7, B5, B4, B6, B3, B6, B7, B5, B2, B1, B3, B1, B4, B1]

#Figura 3

traslado = PuntoCartesiano(PolarCartesiano([50, Alfa]))

C1 = Traslacion(A2, traslado) #inferior izquierdo
C2 = Traslacion(A5, traslado) # Superior izquierdo
C3 = Traslacion(B7, traslado) # Superior Derecho
C4 = Traslacion(B8, traslado) # Inferior derecho

poligono3 = [C1, A2, B8, C4, C1, C2, A5, B7, C3, C2, C1]

#Figura 4

traslado = PuntoCartesiano(PolarCartesiano([50, Alfa]))

D1 = Traslacion(C1, traslado) #inferior izquierdo
D2 = Traslacion(C4, traslado) #inferior derecho
D3 = Traslacion(D1, [0, 80]) # Trasero izquierdo
D4 = Traslacion(D2, [0, 80]) # Trasero Derecho
D5 = Traslacion(C2, [0, 50]) # Frente izquierdo
D6 = Traslacion(C3, [0, 50]) # Frente derecho


poligono4 = [C1, D1, D3, D4, D6, C3, D6, D5, D3, D5, C1]

# Figura 2.1

traslado = PuntoCartesiano(PolarCartesiano([30, Theta]))

PolarF5 = PolarCartesiano([50, 150])

F1 = Traslacion(D5, traslado) #frente Derecho
F2 = Traslacion(F1, [0, 30]) #Frente superior derecho
F3 = Traslacion(D3, [0, 30]) #Trasero superior izquierdo
F4 = Traslacion(D5, [0, 30]) #Frente superior izquierdo
F5 = Traslacion(PolarF5, PuntoCartesiano(F2)) #Trasero derecho superior
F6 = Traslacion(F5, [0,-30])
poligono5 = [D5, F1, F2, F5, F3, D3, F3, F4, F2, F1, D5, F4, D5]

#figura 2.2

traslado = PuntoCartesiano(PolarCartesiano([110, Theta]))

G1 = Traslacion(F1, traslado)
G2 = Traslacion(F2, traslado)
G3 = Traslacion(F3, traslado)
G4 = Traslacion(F4, traslado)
G5 = Traslacion(F5, traslado)
G6 = Traslacion(D5, traslado)
G7 = Traslacion(D3, traslado)

poligono6 = [G6, G1, G2, G5, G3, G7, G3, G4, G2, G1, G6, G4, G6, G7, G6]


##################################        CARAS    #################################################

#Caras superiores
carasuperior123 = [C2, C3, B6, B4, B5, A7, A6, A4]
carasuperior4 = [F2, F5, F3, F4]
carasuperior5 = [G2, G5, G3, G4]
carasuperior6 = [F6, G7, G6, F1]

#Cara lateral izquierda
                                #Esto pa que?  NO Se
#figura1
caralateral1 = [A1, A2, A5, A4]
#figura 1.1
caralateral2 = [B1, B2, B5, B4]
#figura 3
caralateral3 = [A2, C1, C2, A5]
#figura 4
caralateral4 = [C1, D1, D3, D5]
#figura 2.1
caralateral5 = [D5, D3, F3, F4]

#con este coge toda la cara de una
caralateraltotal = [A1, D1, F3, F4, C2, A4]

#Caras Frontales
carafrontal1 = [F4,F2,F1,G6,G4,G2,C3,C2]
carafrontal2 = [A4,A6,A3,A1]
carafrontal3 = [B4,B6,B3,B1]
carafrontal4 = [A7,B5,B2,A8]

def Vistas():
    #ventana.fill(NEGRO)

    #Frontales
    pygame.draw.polygon(ventana, AMARILLO, carafrontal2)
    caraux = []
    for i in carafrontal2:
        caraux.append(Traslacion(i,Tfrontal))
    pygame.draw.polygon(ventana, AMARILLO, caraux)

    pygame.draw.polygon(ventana, AMARILLO, carafrontal3)
    caraux = []
    for i in carafrontal3:
        caraux.append(Traslacion(i,Tfrontal))
    pygame.draw.polygon(ventana, AMARILLO, caraux)

    pygame.draw.polygon(ventana, AMARILLO, carafrontal4)
    caraux = []
    for i in carafrontal4:
        caraux.append(Traslacion(i,Tfrontal))
    pygame.draw.polygon(ventana, AMARILLO, caraux)

    #Superiores
    pygame.draw.polygon(ventana, AZUL, carasuperior6)
    caraux = []
    for i in carasuperior6:
        caraux.append(Traslacion(i,Tsuperior))
    pygame.draw.polygon(ventana, AZUL, caraux)

    pygame.draw.polygon(ventana, AMARILLO, carafrontal1)
    caraux = []
    for i in carafrontal1:
        caraux.append(Traslacion(i,Tfrontal))
    pygame.draw.polygon(ventana, AMARILLO, caraux)

    pygame.draw.polygon(ventana, AZUL, carasuperior123)
    caraux = []
    for i in carasuperior123:
        caraux.append(Traslacion(i,Tsuperior))
    pygame.draw.polygon(ventana, AZUL, caraux)

    pygame.draw.polygon(ventana, AZUL, carasuperior4)
    caraux = []
    for i in carasuperior4:
        caraux.append(Traslacion(i,Tsuperior))
    pygame.draw.polygon(ventana, AZUL, caraux)

    pygame.draw.polygon(ventana, AZUL, carasuperior5)
    caraux = []
    for i in carasuperior5:
        caraux.append(Traslacion(i,Tsuperior))
    pygame.draw.polygon(ventana, AZUL, caraux)

    #Laterales
    pygame.draw.polygon(ventana, VERDE, caralateraltotal)
    caraux = []
    for i in caralateraltotal:
        caraux.append(Traslacion(i,Tlateral))
    pygame.draw.polygon(ventana, VERDE, caraux)

    pygame.display.flip()


def Figura():
    ventana.fill(NEGRO)
    #figura 1
    pygame.draw.polygon(ventana, NOSE, poligono1, 2)

    #Frigura 2
    pygame.draw.polygon(ventana, NOSE, poligono2, 2)

    #Figura 3
    pygame.draw.polygon(ventana, NOSE, poligono3, 2)

    #Figura 4
    pygame.draw.polygon(ventana, NOSE, poligono4, 2)#

    #figura 2.1
    pygame.draw.polygon(ventana, NOSE, poligono5, 2)

    #figura 2.2
    pygame.draw.polygon(ventana, NOSE, poligono6, 2)

    pygame.display.flip()

if __name__ == '__main__':
    Figura()
    while not fin:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Vistas()
            if event.type == pygame.KEYUP:
                Figura()
