import pygame
from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
Origen = [ANCHO/2,ALTO/2]
fin=False
L = 250
Angulo = 0
lf = Estrella_7_puntas(L, Origen)
i = 0
reloj=pygame.time.Clock()
pygame.draw.polygon(ventana, NEGRO, lf,1)
if __name__ == '__main__':
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:

                if event.key == pygame.K_RIGHT:
                    i = +2

                if event.key == pygame.K_LEFT:
                    i = -2

            ln = []
            Angulo+= i
            for punto in lf:
                aux = RotarHorario(punto, Angulo)
                ln.append(aux)
            ventana.fill(NEGRO)
            pygame.draw.circle(ventana,BLANCO, ORIGEN, L, 1)
            pygame.draw.polygon(ventana, ROJO, ln,1)
            pygame.display.flip()
            reloj.tick(60)
