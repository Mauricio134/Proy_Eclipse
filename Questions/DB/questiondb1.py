import pygame
import random
from pygame.locals import *

pygame.init()

# Configuración de la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")

# Carga de imágenes de las opciones
imagen_ancho = 200
imagen_alto = 100
opcion_1_imagen = pygame.image.load("respuesta_1.jpg")
opcion_1_imagen = pygame.transform.scale(opcion_1_imagen, (imagen_ancho, imagen_alto))
opcion_2_imagen = pygame.image.load("carta.jpg")
opcion_2_imagen = pygame.transform.scale(opcion_2_imagen, (imagen_ancho, imagen_alto))

preguntas_respuestas = [
    {
        "pregunta": "Relaciona el dato correspondiente",
        "opciones": [
            opcion_1_imagen,
            opcion_2_imagen
        ],
        "respuesta_correcta": opcion_2_imagen  # Respuesta correcta es la imagen de opción 2
    },
    # Agrega más preguntas con opciones y respuestas comunes aquí
]

contexto = "Contexto1"  # Puedes cambiar esto si deseas usar contexto

font = pygame.font.Font(None, 36)

running = True
respuesta_seleccionada = None  # Almacena la respuesta seleccionada por el usuario

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si el usuario hizo clic en una opción
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 100 < mouse_x < 300 and 400 < mouse_y < 500:
                respuesta_seleccionada = preguntas_respuestas[0]["opciones"][0]  # El usuario seleccionó la opción 1
            elif 400 < mouse_x < 600 and 400 < mouse_y < 500:
                respuesta_seleccionada = preguntas_respuestas[0]["opciones"][1]  # El usuario seleccionó la opción 2

    screen.fill((255, 255, 255))

    # Dibuja la pregunta en la parte superior de la pantalla
    pregunta_surface = font.render(f"{contexto}: {preguntas_respuestas[0]['pregunta']}", True, (0, 0, 0))
    pregunta_rect = pregunta_surface.get_rect()
    pregunta_rect.centerx = window_size[0] // 2
    pregunta_rect.y = 100
    screen.blit(pregunta_surface, pregunta_rect)

    # Dibuja las imágenes de las opciones en la pantalla
    for i, opcion_imagen in enumerate(preguntas_respuestas[0]["opciones"]):
        x = 100 + i * 300
        y = 400
        screen.blit(opcion_imagen, (x, y))

    # Verifica si se ha seleccionado una respuesta y muestra el resultado
    if respuesta_seleccionada is not None:
        if respuesta_seleccionada == preguntas_respuestas[0]["respuesta_correcta"]:
            resultado = "Eres o te haces?"
        else:
            resultado = "Bien tamare"
        resultado_surface = font.render(f"Respuesta: {resultado}", True, (0, 0, 0))
        resultado_rect = resultado_surface.get_rect()
        resultado_rect.centerx = window_size[0] // 2
        resultado_rect.y = 550
        screen.blit(resultado_surface, resultado_rect)

    pygame.display.flip()

pygame.quit()
