import pygame


pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))


se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    pantalla.fill((0, 0, 0))

    pygame.display.flip()
    