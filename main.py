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

def escena_menu():
    # Limpiar el escenario
    screen.fill((0, 0, 0))
    imagenLogo = pygame.image.load('src/logoSpaceApp.png')
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
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón "Jugar"
                if 300 <= x <= 500 and 250 <= y <= 300:
                    return 'JUGAR'
                # Verificar si se hizo clic en el botón "Salir"
                elif 300 <= x <= 500 and 450 <= y <= 500:
                    return 'QUIT'

        # Dibujar el frame actual
        posLuna = (190, (alto/2)-100-100)
        screen.blit(animationArray[current_frame],posLuna )
        # Actualizar el frame actual
        current_frame += 1
        if current_frame >= numFrames:
            current_frame = 0
        # Dibujar el Logo
        posLogo = (175, 50)
        screen.blit(imagenLogo,posLogo)
        # Crear un botón "Jugar"
        pygame.draw.rect(screen, RED, (300, 250, 200, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Jugar", True, WHITE)
        screen.blit(texto_jugar, (350, 260))
         # Crear un botón "Opciones"
        pygame.draw.rect(screen, RED, (300, 350, 200, 50))
        texto_salir = font.render("Opciones", True, WHITE)
        screen.blit(texto_salir, (340, 360))
        # Crear un botón "Salir"
        pygame.draw.rect(screen, RED, (300, 450, 200, 50))
        texto_salir = font.render("Salir", True, WHITE)
        screen.blit(texto_salir, (350, 460))

        pygame.display.flip()
        clock.tick(FPS) 

def escena_juego():
    # Lógica del juego
    # Dibujar los elementos del juego en la pantalla
    # Limpiar el escenario
    # Cargar las imágenes
    imagenLogo = pygame.image.load('src/luna.png')
    # Ajustar el tamaño de la imagen
    imagenLogo = pygame.transform.scale(imagenLogo, (50, 50))  # Nuevo tamaño: (50, 50)
    spsheet = pygame.image.load('src/sol.png')

    clock = pygame.time.Clock()
    FPS = 15  # Frames por segundo
    running = True
    scroll_pos = 0  # Posición inicial de la barra de desplazamiento
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón "Regresar"
                if 50 <= x <= 150 and alto-200 <= y <= alto-150:
                    return 'REGRESAR'
                # Verificar si se hizo clic en la barra de desplazamiento
                elif 50 <= x <= 150 and alto-100 <= y <= alto-50:
                    scroll_pos = x  # Actualizar la posición de la barra de desplazamiento

        # Limpiar el escenario antes de dibujar el nuevo frame
        screen.fill((0, 0, 0))

        # Dibujar el Logo en una posición que depende de la barra de desplazamiento
        screen.blit(imagenLogo,(scroll_pos,50))
        screen.blit(spsheet,(200,200))
        # Crear un botón "Regreso"
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, RED, (50, alto-200, 100, 50))
        texto_regresar = font.render("Regresar", True, WHITE)
        screen.blit(texto_regresar, (50, alto-200))
        # Crear una barra de desplazamiento
        pygame.draw.rect(screen, RED, (50, alto-100, 100, 10))
        pygame.display.flip()

escena_actual = escena_menu

while True:
    resultado = escena_actual()
    if resultado == 'QUIT':
        break
    elif resultado == 'JUGAR':
        escena_actual = escena_juego
    elif resultado == 'REGRESAR':
        escena_actual = escena_menu

pygame.quit()