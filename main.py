import pygame
import sys


# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho = 800
alto = 600
window_size = (ancho, alto)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")
running = True

clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# fondo_menu = pygame.image.load('src/moonAnimation.gif') 


# def escena_menu():
#     spsheet = pygame.image.load('src/moonSpriteS.png')
#     animationArray = []
#     numFrames = 100
#     frameWidth = 50
#     frameHeight = 100

#     for i in range(numFrames):
#         f1 = spsheet.subsurface(i*frameWidth, 0, frameWidth, frameHeight)
#         animationArray.append(f1)

#     for img in animationArray:
#         image = img
#         pygame.display.flip()

#     pygame.draw.rect(screen, RED, (300, 250, 200, 50))
#     font = pygame.font.Font(None, 36)
#     texto_jugar = font.render("Jugar", True, WHITE)
#     screen.blit(texto_jugar, (350, 260))

#     # Crear un botón "Salir"
#     pygame.draw.rect(screen, RED, (300, 350, 200, 50))
#     texto_salir = font.render("Salir", True, WHITE)
#     screen.blit(texto_salir, (360, 360))
###################################################################
# def escena_menu():
#     spsheet = pygame.image.load('src/moonSpriteS.png')
#     animationArray = []
#     numFrames = 100
#     frameWidth = 50
#     frameHeight = 100

#     for i in range(numFrames):
#         f1 = spsheet.subsurface(i*frameWidth, 0, frameWidth, frameHeight)
#         animationArray.append(f1)

#     running = True
#     current_frame = 0
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Dibujar el frame actual
#         screen.blit(animationArray[current_frame], (100, 100))

#         # Actualizar el frame actual
#         current_frame += 1
#         if current_frame >= numFrames:
#             current_frame = 0

#         # Crear un botón "Jugar"
#         pygame.draw.rect(screen, RED, (300, 250, 200, 50))
#         font = pygame.font.Font(None, 36)
#         texto_jugar = font.render("Jugar", True, WHITE)
#         screen.blit(texto_jugar, (350, 260))

#         # Crear un botón "Salir"
#         pygame.draw.rect(screen, RED, (300, 350, 200, 50))
#         texto_salir = font.render("Salir", True, WHITE)
#         screen.blit(texto_salir, (360, 360))
#         pygame.display.flip()
#     pygame.quit()
#######################################################################
def escena_menu():
    spsheet = pygame.image.load('src/moonSpriteS.png')
    animationArray = []
    numFrames = 50
    frameWidth = 100
    frameHeight = 100
    posx = 0
    for i in range(numFrames):
        f1 = spsheet.subsurface(posx, 0, frameWidth, frameHeight)
        animationArray.append(f1)
        posx+= 100

    clock = pygame.time.Clock()
    FPS = 15  # Frames por segundo
    running = True
    current_frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar el frame actual
        posLuna = ((ancho/2)-100+100, (alto/2)-100-100)
        screen.blit(animationArray[current_frame],posLuna )
        # Actualizar el frame actual
        current_frame += 1
        if current_frame >= numFrames:
            current_frame = 0

        # Crear un botón "Jugar"
        pygame.draw.rect(screen, RED, (300, 250, 200, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Jugar", True, WHITE)
        screen.blit(texto_jugar, (350, 260))

        # Crear un botón "Salir"
        pygame.draw.rect(screen, RED, (300, 350, 200, 50))
        texto_salir = font.render("Salir", True, WHITE)
        screen.blit(texto_salir, (360, 360))

        pygame.display.flip()
        clock.tick(FPS)  # Limita el número de iteraciones del bucle por segundo
    pygame.quit()


def escena_juego():
    # Lógica del juego
    # Dibuja los elementos del juego en la pantalla
    pass

escena_actual = escena_menu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Verificar si se hizo clic en el botón "Jugar"
            if 300 <= x <= 500 and 250 <= y <= 300:
                # Cambiar a la escena del juego
                escena_actual = escena_juego
            # Verificar si se hizo clic en el botón "Salir"
            elif 300 <= x <= 500 and 350 <= y <= 400:
                pygame.quit()
                sys.exit()
    # Limpia la pantalla
    screen.fill((0, 0, 0))

    # Actualiza y dibuja la escena actual
    escena_actual()

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de fotogramas
    clock.tick(60)