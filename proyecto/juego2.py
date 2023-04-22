import pygame
import random
import time
pygame.init()

# Configuración de la ventana
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ultima Carrera del Rayo")
#Fondo de pantalla
fondo_image=pygame.image.load('pista2.png')
fondo_image=pygame.transform.scale(fondo_image,(800,600))



# Configuración del reloj
clock = pygame.time.Clock()

# Carga de imágenes
player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()
player_rect.y = size[1] - player_rect.height -50

obstacle_image = pygame.image.load('obstacle1.png')
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.x = 600
obstacle_rect.y = size[1] - obstacle_rect.height - 50

# Configuración de variables del juego
score = 0

# Configuración de la variable de juego que indica si se está ejecutando o no
running = True
tiempo_inicial=time.time()
# Loop principal del juego
while running:
    tiempo_actual=time.time()
    tiempo_transcurrido=tiempo_actual-tiempo_inicial
    # Manejo de eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= 5 +tiempo_transcurrido*0.5
    if keys[pygame.K_RIGHT] and player_rect.x < size[0] - player_rect.width:
        player_rect.x += 5+tiempo_transcurrido*0.5
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -=5 +tiempo_transcurrido*0.5
    if keys[pygame.K_DOWN] and player_rect.y < size[1] - player_rect.height:
        player_rect.y +=5 +tiempo_transcurrido*0.5



    # Movimiento del obstáculo

    obstacle_rect.x -= 3 #Velocidad de juego

    obstacle_rect.x -= 3+tiempo_transcurrido*0.5



    if obstacle_rect.x < -obstacle_rect.width:
    obstacle_rect.x = size[0]
    obstacle_rect.y = random.randint(0, size[1] - obstacle_rect.height)
    score += 1

    # Detección de colisión
    if player_rect.colliderect(obstacle_rect):
    print('Perdiste! Puntuación:', score)
    running = False

    # Pintado de la pantalla
    screen.fill((255, 255, 255))
    screen.blit(fondo_image, (0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(obstacle_image, obstacle_rect)
    font = pygame.font.Font(None, 36)
    score_text = font.render('Puntuación: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    pygame.display.flip()

# Limitación de FPS
clock.tick(60)

pygame.quit()

