import pygame
from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
Origen = [ANCHO/2,ALTO/2]
fin=False
L = 250
lf = Estrella_7_puntas(L, Origen)
pygame.draw.polygon(ventana, AMARILLO, lf,1)
N_rotacionR = 0;
N_rotacionL = 0;
if __name__ == '__main__':
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:

                if event.key == pygame.K_RIGHT:
                    ln = []
                    i=0

                    if N_rotacionL>0:
                        N_rotacionL-=1
                        i=N_rotacionL
                    else:
                        N_rotacionR+=1
                        i=N_rotacionR

                    for punto in lf:
                        aux = RotarHorario(punto, 2*i)
                        ln.append(aux)
                    ventana.fill(NEGRO)
                    pygame.draw.polygon(ventana, AMARILLO, ln,1)

                if event.key == pygame.K_LEFT:
                    ln = []
                    if N_rotacionR>0:
                        N_rotacionR-=1
                        i=N_rotacionR
                    else:
                        N_rotacionL+=1
                        i=N_rotacionL
                    for punto in lf:
                        aux = RotarAntiHorario(punto, 2*i)
                        ln.append(aux)

                    ventana.fill(NEGRO)
                    pygame.draw.polygon(ventana, AMARILLO, ln,1)

            pygame.draw.circle(ventana,AMARILLO, ORIGEN, L, 1)
            pygame.display.flip()
