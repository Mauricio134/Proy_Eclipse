import pygame
import random
import os
import pandas as pd
import time

dir_actual = os.getcwd()
ruta_al_csv = os.path.join(dir_actual, 'countrydb','test.csv')

# Lee el archivo CSV
df = pd.read_csv(ruta_al_csv)
lista_de_paises=df['Nombre'].values
nombres_por_pais = {}

for i, row in df.iterrows():
    pais = row['Nombre']
    hombre=row[' hombre']
    mujer=row[' mujer']
    nombres_por_pais[pais] = [hombre,mujer]


weather_conditions = [
    "Sunny",
    "Cloudy",  
    "Partly Cloudy",  
    "Overcast",  
    "Raining",  
    "Snowing",  
    "Foggy",  
    "Thunder and Lightning",  
    "Windy", 
    "Hailing", 
    "Drizzling",  
    "Freezing", 
    "Blizzard",  
    "Hurricane", 
    "Tornado",  
]

pais_aleatorio = random.choice(lista_de_paises)
nombre_aleatorio = random.choice(nombres_por_pais[pais_aleatorio])
condicion_meteorologica_aleatoria = random.choice(weather_conditions)

if (condicion_meteorologica_aleatoria=="Sunny"or condicion_meteorologica_aleatoria=="Partly Cloudy"):
    answer =1
else:
    answer=0


def generar_pregunta():
    contexto=""
    pregunta = "Hi I'm " + nombre_aleatorio + " from " + pais_aleatorio + ", in my country the weather is " + condicion_meteorologica_aleatoria + ". I can see the Eclipse"
    opciones = ["Yes,you can see the eclipse","Sorry, you will not be able to see the eclipse"]
    respuesta_correcta = answer
    mensa_i = "Correct"
    mensa_c = "Incorrect"
    return contexto,pregunta, opciones, respuesta_correcta, mensa_i, mensa_c

def wrap_text(text, font, max_width):
    """Envuelve el texto para que se ajuste dentro de un ancho máximo."""
    lines = []
    words = text.split(' ')
    while len(words) > 0:
        line_words = []
        while len(words) > 0 and font.size(' '.join(line_words + [words[0]]))[0] <= max_width:
            line_words.append(words.pop(0))
        lines.append(' '.join(line_words))
    return lines




pygame.init()

window = pygame.display.set_mode((800, 600))

ruta_imagen = os.path.join(dir_actual, 'images', 'desktop-wallpaper-dark-night-sky-black-dark-night .jpg')

background = pygame.image.load(ruta_imagen)
font = pygame.font.Font(None, 36)

start_text = """In the sky, a spectacle to see,
But the weather must be your key.
If clouds do cover, you must wait,
Until the clear sky can illuminate."""

start_lines = start_text.split('\n')

start_surfaces = []
for i, line in enumerate(start_lines):
    text_surface = font.render(line, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(400, 300 + i * font.get_linesize()))  
    start_surfaces.append((text_surface, text_rect))

window.blit(background, (0, 0))
for text_surface, text_rect in start_surfaces:
    window.blit(text_surface, text_rect)
pygame.display.flip()
time.sleep(3)  



pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Ventana de Pygame')

black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green= (0,255,0)

font = pygame.font.Font(None, 36)

contexto, pregunta, opciones, respuesta_correcta, mensa_i, mensa_c = generar_pregunta()

lineas_pregunta = wrap_text(pregunta, font, 700)  

textos_pregunta = []
for linea in lineas_pregunta:
    text_surface = font.render(linea, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    textos_pregunta.append((text_surface, text_rect))

pregunta_rect = pygame.Rect(20, 20, 760, len(textos_pregunta) * font.get_linesize()+30)

for i, (text_surface, text_rect) in enumerate(textos_pregunta):
    text_rect.center = (pregunta_rect.centerx, pregunta_rect.y + 10 + i * font.get_linesize())

buttons = []
colores = [green, red] # Define los colores en el orden que deseas
for i, opcion in enumerate(opciones):
    wrapped_text = wrap_text(opcion, font, 360)
    text_opcion = [font.render(line, True, (0, 0, 0)) for line in wrapped_text]

    button_y = 300 + len(lineas_pregunta) * font.get_linesize() + 100  

    button_rect = pygame.Rect(20 + i * 400, button_y, 360, max(100,len(wrapped_text) * font.get_linesize() + 20))
    buttons.append((button_rect,text_opcion ,opcion,colores[i])) # Almacena la opción y el color en el botón

# Load the background image
dir_actual = os.getcwd()
ruta_imagen = os.path.join(dir_actual, 'images', 'desktop-wallpaper-dark-night-sky-black-dark-night .jpg')
background = pygame.image.load(ruta_imagen)

running = True
while running:
    # Draw the background
    window.blit(background,(0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button_rect,text_opcion ,opcion,color in buttons: # Obtiene la opción y el color del botón
                if button_rect.collidepoint(pos):
                    selected_index=buttons.index((button_rect,text_opcion ,opcion,color))
                    if selected_index == respuesta_correcta: # Compara el índice seleccionado con la respuesta correcta
                        print(mensa_c)
                        window.fill(black)
                        correct_text_surface = font.render('Incorrect! :c', True, red)
                        correct_text_rect = correct_text_surface.get_rect(center=(400,300))
                        window.blit(correct_text_surface ,correct_text_rect)
                        pygame.display.flip()
                        time.sleep(2)
                        running=False
                    else:
                        print(mensa_i)
                        window.fill(black)
                        incorrect_text_surface=font.render('Correct! :D',True ,green)
                        incorrect_text_rect=incorrect_text_surface.get_rect(center=(400 ,300))
                        window.blit(incorrect_text_surface ,incorrect_text_rect)
                        pygame.display.flip()
                        time.sleep(2)
                        running=False

    

    pygame.draw.rect(window,(200 ,200 ,200),pregunta_rect)

    for text_surface,text_rect in textos_pregunta:
        window.blit(text_surface,text_rect)

    for button_rect,text_opcion,_ ,color in buttons: # Usa el color almacenado en el botón
        pygame.draw.rect(window,color ,button_rect)

        total_height=len(text_opcion)*font.get_linesize()

        for i,line in enumerate(text_opcion):
            text_opcion_rect=line.get_rect()
            text_opcion_rect.center=(button_rect.centerx ,button_rect.y+button_rect.height/2-total_height/2+i*font.get_linesize())
            window.blit(line,text_opcion_rect)

    pygame.display.flip()

pygame.quit()
