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

print A1, A2, A3, A4, A5, A6, A7, A8

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

#Figura 3

traslado = PuntoCartesiano(PolarCartesiano([50, 150]))

C1 = Traslacion(A2, traslado)
C2 = Traslacion(A5, traslado) # Conecta
C3 = Traslacion(B7, traslado) # Conecta
C4 = Traslacion(B8, traslado)

#Figura 4

traslado = PuntoCartesiano(PolarCartesiano([50, 150]))

D1 = Traslacion(C1, traslado)
D2 = Traslacion(C4, traslado)
D3 = Traslacion(D1, [0, 80]) # Trasero izquierdo
D4 = Traslacion(D2, [0, 80]) # Trasero Derecho
D5 = Traslacion(C2, [0, 40]) # Angulo 30
D6 = Traslacion(C3, [0, 40]) # Angulo 210

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
        Punto(ventana, A1, NOSE)
        Punto(ventana, A2, NOSE)
        Punto(ventana, A3, NOSE)
        #superiores
        Punto(ventana, A4, NOSE)
        Punto(ventana, A5, NOSE)
        Punto(ventana, A6, NOSE)
        #traseros
        Punto(ventana, A7, NOSE)
        Punto(ventana, A8, NOSE)

        #Frigura 2
        Punto(ventana, B1, NOSE)
        Punto(ventana, B2, NOSE)
        Punto(ventana, B3, NOSE)
        #superiores
        Punto(ventana, B4, NOSE)
        Punto(ventana, B5, NOSE)
        Punto(ventana, B6, NOSE)
        #traseros
        Punto(ventana, B7, NOSE)
        Punto(ventana, B8, NOSE)

        #Figura 3
        Punto(ventana, C1, AZUL)
        Punto(ventana, C2, AZUL)
        Punto(ventana, C3, AZUL)
        Punto(ventana, C4, AZUL)

        #Figura 4
        Punto(ventana, D1, VERDE)
        Punto(ventana, D2, VERDE)
        Punto(ventana, D3, VERDE)
        Punto(ventana, D4, VERDE)
        Punto(ventana, D5, VERDE)
        Punto(ventana, D6, VERDE)

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
