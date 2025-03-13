import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título de la ventana e icono
pygame.display.set_caption(" Invasión Espacial ")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

# Función para mostrar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Bucle principal
se_ejecuta = True
while se_ejecuta:

    # Color de fondo RGB
    pantalla.fill((205, 144, 228))
    
    # Eventos
    for evento in pygame.event.get():

        # Salir del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Movimiento del jugador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.1

        # Detener el movimiento del jugador
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio
    jugador(jugador_x, jugador_y)

    # Actualizar la pantalla
    pygame.display.update()

    