from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
fin = False

##################################        PUNTOS    #################################################

#Figura 1

A1 = PuntoPantalla([0, 0])  #Centro
PolarA2 = PolarCartesiano([2*TamanoCudrito, Alfa]) #Inferior izquierdo
PolarA3 = PolarCartesiano([TamanoCudrito, Theta]) #Inferior  derecho
A2 = Traslacion(PolarA2, PuntoCartesiano(A1))
A3 = Traslacion(PolarA3, PuntoCartesiano(A1))
A4 = Traslacion(A1, [0,TamanoCudrito]) #Superior Centro
A5 = Traslacion(A2, [0,TamanoCudrito]) #Superior izquierdo
A6 = Traslacion(A3, [0,TamanoCudrito]) #Superior Derecho
A7 = Traslacion(PolarA2, PuntoCartesiano(A6)) #Superior trasero
A8 = Traslacion(PolarA2, PuntoCartesiano(A3)) #Inferior trasero


traslado = PuntoCartesiano(PolarCartesiano([2*TamanoCudrito, Theta]))

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

traslado = PuntoCartesiano(PolarCartesiano([TamanoCudrito, Alfa]))

C1 = Traslacion(A2, traslado) #inferior izquierdo
C2 = Traslacion(A5, traslado) # Superior izquierdo
C3 = Traslacion(B7, traslado) # Superior Derecho
C4 = Traslacion(B8, traslado) # Inferior derecho

#Figura 4

D1 = Traslacion(C1, traslado) #inferior izquierdo
D2 = Traslacion(C4, traslado) #inferior derecho
D3 = Traslacion(D1, [0, 5*TamanoCudrito/2]) # Trasero izquierdo
D4 = Traslacion(D2, [0, 5*TamanoCudrito/2]) # Trasero Derecho
D5 = Traslacion(C2, [0, 3*TamanoCudrito/2]) # Frente izquierdo
D6 = Traslacion(C3, [0, 3*TamanoCudrito/2]) # Frente derecho

# Figura 2.1

traslado = PuntoCartesiano(PolarCartesiano([TamanoCudrito/2, Theta]))

PolarF5 = PolarCartesiano([TamanoCudrito, Alfa])

F1 = Traslacion(D5, traslado) #frente Derecho
F2 = Traslacion(F1, [0, TamanoCudrito/2]) #Frente superior derecho
F3 = Traslacion(D3, [0, TamanoCudrito/2]) #Trasero superior izquierdo
F4 = Traslacion(D5, [0, TamanoCudrito/2]) #Frente superior izquierdo
F5 = Traslacion(PolarF5, PuntoCartesiano(F2)) #Trasero derecho superior
F6 = Traslacion(F5, [0,-TamanoCudrito/2])

#figura 2.2

traslado = PuntoCartesiano(PolarCartesiano([5*TamanoCudrito/2, Theta]))

G1 = Traslacion(F1, traslado)
G2 = Traslacion(F2, traslado)
G3 = Traslacion(F3, traslado)
G4 = Traslacion(F4, traslado)
G5 = Traslacion(F5, traslado)
G6 = Traslacion(D5, traslado)
G7 = Traslacion(D3, traslado)

###############################      Figuras ######################################
poligono1 = [A1,D1,D2,B3,B1,B2,A8,A3,A1,A4,C2,C3,B6,B3,B6,B4,B1,B4,B5,B2,B5,A7,A8,A7,A6,A3,A6,A4]
poligono2 = [G5,D2,G5,G2,C3,G2,G4,G6,F1,F2,F4,C2,F4,F3,D1,F3,F5,F2,F5,F6,F1,F6,G7,G6,G7,G3,G4,G3]
##################################        Vistas    #################################################

#Caras superiores
carasuperior123 = [C2, C3, B6, B4, B5, A7, A6, A4]
carasuperior4 = [F2, F5, F3, F4]
carasuperior5 = [G2, G5, G3, G4]
carasuperior6 = [F6, G7, G6, F1]

#Cara lateral izquierda

caralateraltotal = [A1, D1, F3, F4, C2, A4]

#Caras Frontales
carafrontal1 = [F4,F2,F1,G6,G4,G2,C3,C2]
carafrontal2 = [A4,A6,A3,A1]
carafrontal3 = [B4,B6,B3,B1]
carafrontal4 = [A7,B5,B2,A8]

#Caras inaxcesibles
caraimposible1 = [G3,G4,G6,G7]
caraimposible2 = [F5,F2,F1,F6]
caraimposible3 = [B5,B4,B1,B2]
caraimposible4 = [A7,A6,A3,A8]
def Vistas():
    #ventana.fill(NEGRO)
    #Imposible (meramente estetico)
    pygame.draw.polygon(ventana, NEGRO, caraimposible1)
    pygame.draw.polygon(ventana, NEGRO, caraimposible2)
    pygame.draw.polygon(ventana, NEGRO, caraimposible3)
    pygame.draw.polygon(ventana, NEGRO, caraimposible4)

    #Frontales
    pygame.draw.polygon(ventana, AMARILLO, carafrontal2)
    Vistar(Tfrontal,carafrontal2,ventana, AMARILLO)
    pygame.display.flip()

    pygame.draw.polygon(ventana, AMARILLO, carafrontal3)
    Vistar(Tfrontal,carafrontal3,ventana, AMARILLO)

    pygame.draw.polygon(ventana, AMARILLO, carafrontal4)
    Vistar(Tfrontal,carafrontal4,ventana, AMARILLO)

    #Superiores
    pygame.draw.polygon(ventana, AZUL, carasuperior6)
    Vistar(Tsuperior,carasuperior6,ventana, AZUL)

    pygame.draw.polygon(ventana, AMARILLO, carafrontal1)
    Vistar(Tfrontal,carafrontal1,ventana, AMARILLO)

    pygame.draw.polygon(ventana, AZUL, carasuperior123)
    Vistar(Tsuperior,carasuperior123,ventana, AZUL)

    pygame.draw.polygon(ventana, AZUL, carasuperior4)
    Vistar(Tsuperior,carasuperior4,ventana, AZUL)

    pygame.draw.polygon(ventana, AZUL, carasuperior5)
    Vistar(Tsuperior,carasuperior5,ventana, AZUL)

    #Laterales
    pygame.draw.polygon(ventana, VERDE, caralateraltotal)
    Vistar(Tlateral,caralateraltotal,ventana, VERDE)


def Figura():
    ventana.fill(NEGRO)
    #figura 1
    pygame.draw.polygon(ventana, NOSE, poligono1, 3)

    #Frigura 2
    pygame.draw.polygon(ventana, NOSE, poligono2, 3)

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
