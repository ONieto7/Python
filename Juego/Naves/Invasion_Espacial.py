import pygame
import random
import math
from pygame import mixer
import io

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título de la ventana e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")
colision_img = pygame.image.load("colision.png")

# Agregar música de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

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
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(30)

# Variables de la Bala
img_bala = pygame.image.load("explosion.png")
bala_x = 0
bala_y = 480
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Variable para colisión
tiempo_colision = 0
pos_colision = (0, 0)
mostrar_colision = False

# Variable para el puntaje
puntaje = 0
enemigo_colisionados = 0
nivel = 1
fuente_como_bytes = None

# Función para cargar la fuente como bytes
def fuente_bytes(fuente):
    with open(fuente, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

# Cargar fuentes
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font("Fastest.ttf", 32)
fuente_final = pygame.font.Font(fuente_como_bytes, 40)
fuente_nivel = pygame.font.Font("freesansbold.ttf", 24)

# Texto de información
texto_x = 10
texto_y = 10

# Función para mostrar el texto de Game Over
def texto_final():
    mixer.music.stop()
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

# Función para mostrar el puntaje
def mostrar_puntaje(x, y):
    puntaje_texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(puntaje_texto, (x, y))

# Función para mostrar el nivel
def mostrar_nivel(x, y):
    nivel_texto = fuente_nivel.render(f"Nivel: {nivel}", True, (255, 255, 255))
    pantalla.blit(nivel_texto, (x, y))

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

# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((math.pow(x_1 - x_2, 2)) + (math.pow(y_1 - y_2, 2)))
    if distancia < 27:
        return True
    else:
        return False

# Función subir Nivel
def incrementar_nivel():
    global cantidad_enemigos, bala_y_cambio
    for i in range(cantidad_enemigos):
        if enemigo_x_cambio[i] > 0:
            enemigo_x_cambio[i] += 0.05
        else:
            enemigo_x_cambio[i] -= 0.05
    bala_y_cambio += 0.05  # Incrementar la velocidad de la bala

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
                jugador_x_cambio -= 0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.5
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    mixer.Sound("disparo.mp3").play()
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

        # Game Over
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            se_ejecuta = False
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Límites del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = abs(enemigo_x_cambio[e])  # Asegurarse de que sea positivo
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -abs(enemigo_x_cambio[e])  # Asegurarse de que sea negativo
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        if hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y):
            mixer.Sound("Golpe.mp3").play()
            bala_y = 480
            bala_visible = False
            puntaje += 1
            enemigo_colisionados += 1
            tiempo_colision = pygame.time.get_ticks()
            pos_colision = (enemigo_x[e], enemigo_y[e])
            mostrar_colision = True
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 150)

            # Incrementar nivel cada 10 enemigos colisionados
            if enemigo_colisionados % 10 == 0:           
                incrementar_nivel()
                nivel += 1

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

    mostrar_puntaje(texto_x, texto_y)
    mostrar_nivel(texto_x + 650 , texto_y + 10)

    # Actualizar la pantalla
    pygame.display.update()

