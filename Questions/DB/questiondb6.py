import pygame
import random
from pygame.locals import *

pygame.init()
pygame.font.init()  # Inicializa la biblioteca de fuentes

# Configuración de la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")

# Carga de imágenes de las opciones
imagen_ancho = 200
imagen_alto = 200
opcion_1_imagen = pygame.image.load("respuesta_1.jpg")
opcion_1_imagen = pygame.transform.scale(opcion_1_imagen, (200, 200))
opcion_2_imagen = pygame.image.load("respuesta_2.jpg")
opcion_2_imagen = pygame.transform.scale(opcion_2_imagen, (300, 200))

# Posiciones de las imágenes
posicion_opcion_1 = opcion_1_imagen.get_rect()
posicion_opcion_2 = opcion_2_imagen.get_rect()
posicion_opcion_1.topleft = (100, 300)
posicion_opcion_2.topleft = (450, 300)

# Lista de países y sus coordenadas y horas de amanecer y atardecer
paises = [
    {"nombre": "Perú", "amanecer": "06:00", "atardecer": "18:00"},
    {"nombre": "España", "amanecer": "07:30", "atardecer": "20:30"},
    {"nombre": "Japón", "amanecer": "04:30", "atardecer": "18:30"},
    {"nombre": "Estados Unidos", "amanecer": "06:00", "atardecer": "20:00"},
    {"nombre": "Canadá", "amanecer": "05:00", "atardecer": "21:00"},
    {"nombre": "Brasil", "amanecer": "05:30", "atardecer": "18:00"},
    {"nombre": "Argentina", "amanecer": "07:30", "atardecer": "20:30"},
    {"nombre": "Australia", "amanecer": "06:00", "atardecer": "18:00"},
    {"nombre": "Nueva Zelanda", 	"amanecer":"06:00","atardecer":"20:00"},
    {"nombre":"China","amanecer":"05:00","atardecer":"19:00"},
    {"nombre":"India","amanecer":"06:00","atardecer":"18:30"},
    {"nombre":"Rusia","amanecer":"04:30","atardecer":"21:00"},
    {"nombre":"Sudáfrica","amanecer":"06:30","atardecer":"18:00"},
    {"nombre":"México","amanecer":"07:00","atardecer":"20:00"},
    {"nombre":"Colombia","amanecer":"06:00","atardecer":"18:00"},
    {"nombre":"Francia","amanecer":"08:30","atardecer":"17:30"},
    {"nombre":"Italia","amanecer":"07:30","atardecer":"16:30"},
    {"nombre":"Alemania","amanecer":"08:00","atardecer":"16:00"},
    {"nombre":"Indonesia","amanecer":"05:30","atardecer":"18:00"},
    {"nombre":"Chile","amanecer":"07:15","atardecer":"20:45"},
    {"nombre": "Egipto", 	"amanecer":"05:45","atardecer":"17:45"},
    {"nombre":	"Reino Unido",	"amanecer":"08:15","atardecer":"16:15"},
    {"nombre":	"Grecia",	"amanecer":"07:15","atardecer":"17:15"},
    {"nombre":	"Turquía",	"amanecer":"07:45","atardecer":"17:45"},
    {"nombre":	"Noruega",	"amanecer":"09:15","atardecer":"15.15"},
    {"nombre":	"Suecia",	"amanecer":"08.45","atardecer":"14.45"},
    {"nombre":	"Finlandia",	"amanecer":"09.15","atardecer":"15.15"},
    {"nombre":	"Dinamarca",	"amanecer":"08.45","atardecer":"15.45"},
    {"nombre":	"Irlanda",	"amanecer":"08.45","atardecer":"16.15"}
]


# Seleccionar un país al azar
pais = random.choice(paises)

# Generar una hora aleatoria del día en formato HH:MM
hora_aleatoria = "{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59))

es_de_dia = pais["amanecer"] < hora_aleatoria < pais["atardecer"]

# Crear una fuente para mostrar el texto
font = pygame.font.Font(None, 36)

# Crear textos con la información del país y las horas de amanecer y atardecer
linea1_texto = font.render("En {} amanece a las {} y atardece a las {},".format(
    pais["nombre"], pais["amanecer"], pais["atardecer"]), True, (255, 255, 255))
linea2_texto = font.render("si la hora es {} ¿qué tipo de eclipse sería posible ver?".format(hora_aleatoria), True, (255, 255, 255))

respuesta_correcta_texto = font.render("¡Bien hecho! Has seleccionado la opción correcta.", True, (0, 255, 0))
respuesta_incorrecta_texto = font.render("Lo siento, has seleccionado la opción incorrecta.", True, (255, 0, 0))
mostrar_respuesta = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if posicion_opcion_1.collidepoint(pos):
                if not es_de_dia:
                    respuesta_texto = respuesta_correcta_texto
                else:
                    respuesta_texto = respuesta_incorrecta_texto
                mostrar_respuesta = True
            elif posicion_opcion_2.collidepoint(pos):
                if es_de_dia:
                    respuesta_texto = respuesta_correcta_texto
                else:
                    respuesta_texto = respuesta_incorrecta_texto
                mostrar_respuesta = True


    screen.fill((0, 0, 0))

    # Muestra ambas imágenes sin importar si es de día o de noche
    screen.blit(opcion_1_imagen, posicion_opcion_1)
    screen.blit(opcion_2_imagen, posicion_opcion_2)

    # Muestra los textos en la pantalla
    screen.blit(linea1_texto, (window_size[0] / 2 - linea1_texto.get_width() / 2,
                            window_size[1] / 4 - linea1_texto.get_height() / 2 - linea2_texto.get_height()))
    screen.blit(linea2_texto, (window_size[0] / 2 - linea2_texto.get_width() / 2,
                            window_size[1] / 4 - linea2_texto.get_height() / 2))
    
    if mostrar_respuesta:
        screen.blit(respuesta_texto, (window_size[0] / 2 - respuesta_texto.get_width() / 2,
                                    window_size[1] - respuesta_texto.get_height() - 20))



    pygame.display.flip()

pygame.quit()
