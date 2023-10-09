import pygame
import sys
import random
import os
import pandas as pd
import time

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

def escena_MiniGames():
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
                if 50 <= x <= 150 and alto-100 <= y <= alto-50:
                    return 'REGRESAR'
                elif 50 <= x <= 300 and 250 <= y <= 300:
                    return 'MOON-POS'
                elif 350 <= x <= 550 and 250 <= y <= 300:
                    return 'QUIZ-CH'
                elif 50 <= x <= 250 and 350 <= y <= 400:
                    return 'QUIZ-GA'

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
        # Crear un botón "JuegoMaycol"
        pygame.draw.rect(screen, RED, (50, 250, 250, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Posicion del Eclipse", True, WHITE)
        screen.blit(texto_jugar, (50, 260))
        # Crear un botón "JuegoChega"
        pygame.draw.rect(screen, RED, (350, 250, 200, 50))
        texto_Quiz = font.render("Quiz", True, WHITE)
        screen.blit(texto_Quiz, (350, 260))
        # Crear un botón "JuegoGabo"
        pygame.draw.rect(screen, RED, (50, 350, 200, 50))
        texto_Quiz = font.render("QuizDate", True, WHITE)
        screen.blit(texto_Quiz, (50, 360))
         # Crear un botón "Regreso"
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, RED, (50, alto-100, 150, 50))
        texto_regresar = font.render("Regresar", True, WHITE)
        screen.blit(texto_regresar, (50, alto-75))

        pygame.display.flip()
        clock.tick(FPS) 

def escena_QuizCh():
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
        pregunta = "Hi I'm " + nombre_aleatorio + " from " + pais_aleatorio + ", in my country the weather is   " + condicion_meteorologica_aleatoria + ". I can see the Eclipse"
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
    #SE HIZO UN CAMBIO
    window = pygame.display.set_mode((800, 600))
    # Limpiar el escenario
    screen.fill((0, 0, 0))
    #################################################################### TRANSICION
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
    #########################################################################################
    # Limpiar el escenario
    screen.fill((0, 0, 0))
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

        button_rect = pygame.Rect(20 + i * 400, button_y, 360, max(100,len(wrapped_text) * font.get_linesize()  + 20))
        buttons.append((button_rect,text_opcion ,opcion,colores[i])) # Almacena la opción y el color en el  botón

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
                        if selected_index == respuesta_correcta: # Compara el índice seleccionado con la    respuesta correcta
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
                text_opcion_rect.center=(button_rect.centerx ,button_rect.y+button_rect.height/2-total_height/2 +i*font.get_linesize())
                window.blit(line,text_opcion_rect)
        pygame.display.flip()
    return 'REGRESAR'

def escena_QuizGa():
    # Limpiar el escenario
    pygame.font.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    screen.fill((0, 0, 0))
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
    line1_text = font.render("In {} sunrise is at {} and sunset is at {},".format(country["name"], country  ["sunrise"], country["sunset"]), True, (255, 255, 255))
    line2_text = font.render("if the time is {}, what type of eclipse would it be possible to see?".format  (random_time), True, (255, 255, 255))

    correct_answer_text = font.render("Well done! You've selected the correct option.", True, (0, 255, 0))
    incorrect_answer_text = font.render("Sorry, you've selected the incorrect option.", True, (255, 0, 0))
    show_answer = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if posicion_opcion_1.collidepoint(pos):
                    if not es_de_dia:
                        respuesta_texto = correct_answer_text
                        running = False
                    else:
                        respuesta_texto = incorrect_answer_text
                    show_answer = True
                elif posicion_opcion_2.collidepoint(pos):
                    if es_de_dia:
                        respuesta_texto = correct_answer_text
                        running = False
                    else:
                        respuesta_texto = incorrect_answer_text
                    show_answer = True
                    
        screen.fill((0, 0, 0))
        screen.blit(opcion_1_imagen, posicion_opcion_1)
        screen.blit(opcion_2_imagen, posicion_opcion_2)
        # Muestra texto en la pantalla
        screen.blit(line1_text, (window_size[0] / 2 - line1_text.get_width() / 2, window_size[1] / 5 -  line1_text.get_height() / 2 - line2_text.get_height()))
        screen.blit(line2_text, (window_size[0] / 2 - line2_text.get_width() / 2, window_size[1] / 5 -  line2_text.get_height() / 2))
        if show_answer:
            screen.blit(respuesta_texto, (window_size[0] / 2 - respuesta_texto.get_width() / 2, window_size[1]  - respuesta_texto.get_height() - 20))
        pygame.display.flip()
        if running == False:
            time.sleep(2)
    return 'REGRESAR'

def escena_juego():
    # Cargar las imágenes
    imGLuna = pygame.image.load('src/luna.png')
    imGLuna = pygame.transform.scale(imGLuna, (50, 50))  # Nuevo tamaño: (50, 50)
    imGSol = pygame.image.load('src/sol.png')
    imGSol = pygame.transform.scale(imGSol, (200, 200))  # Nuevo tamaño: (50, 50)

    spsheet = pygame.image.load('src/Tierra.png')
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
    FPS = 10  # Frames por segundo
    running = True
    scroll_pos = 75  # Posición inicial de la barra de desplazamiento
    current_frame = 0
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
        # Dibujar una elipse
        color = (255, 255, 255)  # Color de la elipse en formato RGB
        rectOne = pygame.Rect(75, (alto/2)-10, 250, 50+25) 
        rectTwo = pygame.Rect(200, (alto/2)-50, 600, 100+50) 
        thickness = 2  # Grosor del borde en píxeles
        pygame.draw.ellipse(screen, color, rectOne, thickness)
        pygame.draw.ellipse(screen, color, rectTwo, thickness)
        # Definir los puntos inicial y final de la línea
        # Dibujar la línea
        start_pos = (75, (alto/2)+25)
        end_pos = (800, (alto/2)+25)
        pygame.draw.line(screen, color, start_pos, end_pos, thickness)
        # Dibujar el frame actual
        tierraPos = (200-50, (alto/2)-50)
        screen.blit(animationArray[current_frame],tierraPos)
        # Actualizar el frame actual
        current_frame += 1
        if current_frame >= numFrames:
            current_frame = 0
        # Dibujar el Logo en una posición que depende de la barra de desplazamiento
        screen.blit(imGLuna,(scroll_pos,(alto/2)))
        screen.blit(imGSol,(200+200,(alto/2)-100))
        # Crear un botón "Regreso"
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, RED, (50, alto-200, 100, 50))
        texto_regresar = font.render("Regresar", True, WHITE)
        screen.blit(texto_regresar, (50, alto-200))
        # Crear una barra de desplazamiento
        pygame.draw.rect(screen, RED, (50, alto-100, 100, 10))
        
        pygame.display.flip()
        clock.tick(FPS) 

escena_actual = escena_menu

while True:
    resultado = escena_actual()
    if resultado == 'QUIT':
        break
    elif resultado == 'JUGAR':
        escena_actual = escena_MiniGames
    elif resultado == 'REGRESAR':
        escena_actual = escena_menu
    elif resultado == 'MOON-POS':
        escena_actual = escena_juego
    elif resultado == 'QUIZ-CH':
        escena_actual = escena_QuizCh
    elif resultado == 'QUIZ-GA':
        escena_actual = escena_QuizGa

pygame.quit()