import pygame
from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
fin = False

#Figura 1
A1 = PuntoPantalla([0, 0])  #Centro
PolarA2 = PolarCartesiano([80, 150]) #Inferior izquierdo
PolarA3 = PolarCartesiano([40, 30]) #Inferior  derecho
A2 = Traslacion(PolarA2, PuntoCartesiano(A1))
A3 = Traslacion(PolarA3, PuntoCartesiano(A1))
A4 = Traslacion(A1, [0,30]) #Superior Centro
A5 = Traslacion(A2, [0,30]) #Superior izquierdo
A6 = Traslacion(A3, [0,30]) #Superior Derecho
A7 = Traslacion(A2, PuntoCartesiano(A6)) #Superior trasero
A8 = Traslacion(A2, PuntoCartesiano(A3)) #Inferior trasero

poligono1 = [A1, A2, A8, A7, A5, A4, A6, A3, A6, A7, A5, A2, A1, A3, A1, A4, A1]


traslado = PuntoCartesiano(PolarCartesiano([100, 30]))

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

traslado = PuntoCartesiano(PolarCartesiano([50, 150]))

C1 = Traslacion(A2, traslado) #inferior izquierdo
C2 = Traslacion(A5, traslado) # Superior izquierdo
C3 = Traslacion(B7, traslado) # Superior Derecho
C4 = Traslacion(B8, traslado) # Inferior derecho

poligono3 = [C1, A2, B8, C4, C1, C2, A5, B7, C3, C2, C1]

#Figura 4

traslado = PuntoCartesiano(PolarCartesiano([50, 150]))

D1 = Traslacion(C1, traslado) #inferior izquierdo
D2 = Traslacion(C4, traslado) #inferior derecho
D3 = Traslacion(D1, [0, 80]) # Trasero izquierdo
D4 = Traslacion(D2, [0, 80]) # Trasero Derecho
D5 = Traslacion(C2, [0, 50]) # Angulo 30
D6 = Traslacion(C3, [0, 50]) # Angulo 210

poligono4 = [C1, D1, D3, D4, D6, C3, D6, D5, D3, D5, C1]

# Figura 2.1

traslado = PuntoCartesiano(PolarCartesiano([30, 30]))

F1 = Traslacion(D5, traslado)
F2 = Traslacion(F1, [0, 30])
F3 = Traslacion(D3, [0, 30])
F4 = Traslacion(D5, [0, 30])
F5 = Traslacion(D3, PuntoCartesiano(F2))


#          x    y   z     Medidas
figura1 = [30, 80, 40]
figura2 = [20, 40, 20]
figura3 = [100, 40, 40]
figura4 = [100, 40, 80]


if __name__ == '__main__':
    while not fin:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        #Dibujar(ventana, ORIGEN)
        #figura 1
        pygame.draw.polygon(ventana, NOSE, poligono1, 2)

        #Frigura 2
        pygame.draw.polygon(ventana, NOSE, poligono2, 2)

        #Figura 3
        pygame.draw.polygon(ventana, NOSE, poligono3, 2)

        #Figura 4
        pygame.draw.polygon(ventana, NOSE, poligono4, 2)


        #figura 2.1
        Punto(ventana, F1, ROJO)
        Punto(ventana, F2, ROJO)
        Punto(ventana, F3, ROJO)
        Punto(ventana, F4, ROJO)
        #Punto(ventana, F5, ROJO)





"""
def RotarAntiHorario(Pto, t, Origen):
    Pto1 = from_Pantalla_to_Carte(Origen,Pto)

    angulo=math.radians(t)
    X = int(Pto1[0]*math.cos(angulo) - Pto1[1]*math.sin(angulo))
    Y = int(Pto1[0]*math.sin(angulo) + Pto1[1]*math.cos(angulo))

    return  from_Carte_to_pantalla(Origen, [X,Y])
"""
