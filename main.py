import pygame
from plano import *

pygame.init()
ventana = pygame.display.set_mode([ANCHO, ALTO])
ventana.fill(Cpantalla)
Origen = [ANCHO/2,ALTO/2]
fin=False
L = 250
Angulo = 0
lf = Estrella_7_puntas(L, Origen)
i = 0
reloj=pygame.time.Clock()
pygame.time.set_timer(Itstime, 600)
pygame.draw.polygon(ventana, Cplano, lf,1)
if __name__ == '__main__':
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    i = +2
                if event.button == 4:
                    i = -2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    i = +2
                if event.key == pygame.K_LEFT:
                    i = -2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if Cpantalla == BLANCO:
                            Cpantalla = NEGRO
                        else:
                            Cpantalla = BLANCO
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

        ln = []
        Angulo+= i
        if Cestrella == AMARILLO:
            Cestrella = ROJO
        else:
            Cestrella = AMARILLO
        for punto in lf:
            aux = RotarHorario(punto, Angulo)
            ln.append(aux)
        ventana.fill(Cpantalla)
        pygame.draw.circle(ventana, Cplano, ORIGEN, L, 1)
        pygame.draw.polygon(ventana, Cestrella, ln,TLine)
        pygame.display.flip()
        reloj.tick(30)
