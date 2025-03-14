import pygame
import random
import math
import os

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título de la ventana e icono
pygame.display.set_caption(" Invasión Espacial ")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")
colision_img = pygame.image.load("colision.png")

# Variables del Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 368
jugador_y = 520
jugador_x_cambio = 0

# Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 150))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(30)

# Variables de la Bala
img_bala = pygame.image.load("explosion.png")
bala_x = 0
bala_y = 480
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

# Variable para colision
tiempo_colision = 0
pos_colision = (0, 0)
mostrar_colision = False

# Variable para el puntaje
puntaje = 0

# Función para mostrar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Función para mostrar al enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((math.pow(x_1 - x_2, 2)) + (math.pow(y_1 - y_2, 2)))
    if distancia < 27:
        return True
    else:
        return False

# Bucle principal
se_ejecuta = True
while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))
    
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
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Detener el movimiento del jugador
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio

    # Límites del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Actualizar la posición del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

        # Límites del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        if hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y):
            bala_y = 480
            bala_visible = False
            puntaje += 1
            print(puntaje)
            tiempo_colision = pygame.time.get_ticks()
            pos_colision = (enemigo_x[e], enemigo_y[e])
            mostrar_colision = True
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 150)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 480
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Mostrar imagen de colisión 
    if mostrar_colision and pygame.time.get_ticks() - tiempo_colision < 1000:
        pantalla.blit(colision_img, pos_colision)
    else:
        mostrar_colision = False

    jugador(jugador_x, jugador_y)

    # Actualizar la pantalla
    pygame.display.update()

