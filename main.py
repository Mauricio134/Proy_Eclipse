import pygame
import sys


# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()