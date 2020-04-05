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

traslado = PuntoCartesiano(PolarCartesiano([90, 30]))

#Figura 1.1
B1 = Traslacion(A1, traslado) #Centro
B2 = Traslacion(A2, traslado) #Inferior izquierdo
B3 = Traslacion(A3, traslado) #Inferior  derecho
B4 = Traslacion(A4, traslado) #Superior Centro
B5 = Traslacion(A5, traslado) #Superior izquierdo
B6 = Traslacion(A6, traslado) #Superior Derecho
B7 = Traslacion(A7, traslado) #Superior trasero
B8 = Traslacion(A8, traslado) #Inferior trasero



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

        Dibujar(ventana, ORIGEN)
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
        Punto(ventana, B1, VERDE)
        Punto(ventana, B2, VERDE)
        Punto(ventana, B3, VERDE)
        #superiores
        Punto(ventana, B4, VERDE)
        Punto(ventana, B5, VERDE)
        Punto(ventana, B6, VERDE)
        #traseros
        Punto(ventana, B7, VERDE)
        Punto(ventana, B8, VERDE)






"""
def RotarAntiHorario(Pto, t, Origen):
    Pto1 = from_Pantalla_to_Carte(Origen,Pto)

    angulo=math.radians(t)
    X = int(Pto1[0]*math.cos(angulo) - Pto1[1]*math.sin(angulo))
    Y = int(Pto1[0]*math.sin(angulo) + Pto1[1]*math.cos(angulo))

    return  from_Carte_to_pantalla(Origen, [X,Y])
"""
