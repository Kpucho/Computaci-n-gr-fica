import pygame

pygame.init()
ventana = pygame.display.set_mode([600, 450])
fin = False


if __name__ == '__main__':
    while not fin:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
