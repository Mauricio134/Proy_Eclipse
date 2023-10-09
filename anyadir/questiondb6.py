import pygame
import random
from pygame.locals import *
#CHECK
pygame.init()
pygame.font.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Answer please")

opcion_1_imagen = pygame.image.load("respuesta_1.jpg")
opcion_1_imagen = pygame.transform.scale(opcion_1_imagen, (200, 200))
opcion_2_imagen = pygame.image.load("respuesta_2.jpg")
opcion_2_imagen = pygame.transform.scale(opcion_2_imagen, (300, 200))

# Posiciones de las imágenes
posicion_opcion_1 = opcion_1_imagen.get_rect()
posicion_opcion_2 = opcion_2_imagen.get_rect()
posicion_opcion_1.topleft = (100, 300)
posicion_opcion_2.topleft = (450, 300)

countries = [
    {"name": "Peru", "sunrise": "06:00", "sunset": "18:00"},
    {"name": "Spain", "sunrise": "07:30", "sunset": "20:30"},
    {"name": "Japan", "sunrise": "04:30", "sunset": "18:30"},
    {"name": "United States", "sunrise": "06:00", "sunset": "20:00"},
    {"name": "Canada", "sunrise": "05:00", "sunset": "21:00"},
    {"name": "Brazil", "sunrise": "05:30", "sunset": "18:00"},
    {"name": "Argentina", "sunrise": "07:30", "sunset": "20:30"},
    {"name": "Australia", "sunrise": "06:00", "sunset": "18:00"},
    {"name": "New Zealand", 	"sunrise":"06:00","sunset":"20:00"},
    {"name":"China","sunrise":"05:00","sunset":"19:00"},
    {"name":"India","sunrise":"06:00","sunset":"18:30"},
    {"name":"Russia","sunrise":"04:30","sunset":"21:00"},
    {"name":"South Africa","sunrise":"06:30","sunset":"18:00"},
    {"name":"Mexico","sunrise":"07:00","sunset":"20:00"},
    {"name":"Colombia","sunrise":"06:00","sunset":"18:00"},
    {"name":"France","sunrise":"08:30","sunset":"17:30"},
    {"name":"Italy","sunrise":"07:30","sunset":"16:30"},
    {"name":"Germany","sunrise":"08:00","sunset":"16:00"},
    {"name":"Indonesia","sunrise":"05:30","sunset":"18:00"},
    {"name":"Chile","sunrise":"07:15","sunset":"20:45"},
    {"name":	"Egypt", 	"sunrise":"05:45","sunset":"17:45"},
    {"name":	"United Kingdom",	"sunrise":"08:15","sunset":"16:15"},
    {"name":	"Greece",	"sunrise":"07:15","sunset":"17:15"},
    {"name":	"Turkey",	"sunrise":"07:45","sunset":"17:45"},
    {"name":	"Norway",	"sunrise":"09:15","sunset":"15.15"},
    {"name":	"Sweden",	"sunrise":"08.45","sunset":"14.45"},
    {"name":	"Finland",	"sunrise":"09.15","sunset":"15.15"},
    {"name":	"Denmark",	"sunrise":"08.45","sunset":"15.45"},
    {"name":	"Ireland",	"sunrise":"08.45","sunset":"16.15"}
]



country = random.choice(countries)
random_time = "{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59))

es_de_dia = country["sunrise"] < random_time < country["sunset"]

font = pygame.font.Font(None, 32)
line1_text = font.render("In {} sunrise is at {} and sunset is at {},".format(country["name"], country["sunrise"], country["sunset"]), True, (255, 255, 255))
line2_text = font.render("if the time is {}, what type of eclipse would it be possible to see?".format(random_time), True, (255, 255, 255))

correct_answer_text = font.render("Well done! You've selected the correct option.", True, (0, 255, 0))
incorrect_answer_text = font.render("Sorry, you've selected the incorrect option.", True, (255, 0, 0))
show_answer = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if posicion_opcion_1.collidepoint(pos):
                if not es_de_dia:
                    respuesta_texto = correct_answer_text
                else:
                    respuesta_texto = incorrect_answer_text
                show_answer = True
            elif posicion_opcion_2.collidepoint(pos):
                if es_de_dia:
                    respuesta_texto = correct_answer_text
                else:
                    respuesta_texto = incorrect_answer_text
                show_answer = True


    screen.fill((0, 0, 0))

    screen.blit(opcion_1_imagen, posicion_opcion_1)
    screen.blit(opcion_2_imagen, posicion_opcion_2)

    # Muestra texto en la pantalla
    screen.blit(line1_text, (window_size[0] / 2 - line1_text.get_width() / 2, window_size[1] / 5 - line1_text.get_height() / 2 - line2_text.get_height()))
    screen.blit(line2_text, (window_size[0] / 2 - line2_text.get_width() / 2, window_size[1] / 5 - line2_text.get_height() / 2))
    
    if show_answer:
        screen.blit(respuesta_texto, (window_size[0] / 2 - respuesta_texto.get_width() / 2, window_size[1] - respuesta_texto.get_height() - 20))



    pygame.display.flip()

pygame.quit()
