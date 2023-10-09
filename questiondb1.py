import pygame
import random
import sys

pygame.init()
# Configuración de la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")
pathSrc = "./src/img-Osc/"
# Carga de imágenes de las opciones
imagen_ancho = 200
imagen_alto = 100
opcion_1_imagen = pygame.image.load(f"{pathSrc}respuesta_1.jpg")
opcion_1_imagen = pygame.transform.scale(opcion_1_imagen, (imagen_ancho, imagen_alto))
opcion_2_imagen = pygame.image.load(f"{pathSrc}respuesta_2.jpg")
opcion_2_imagen = pygame.transform.scale(opcion_2_imagen, (imagen_ancho, imagen_alto))
opcion_3_imagen = pygame.image.load(f"{pathSrc}respuesta_3.jpg")
opcion_3_imagen = pygame.transform.scale(opcion_3_imagen, (imagen_ancho, imagen_alto))
opcion_4_imagen = pygame.image.load(f"{pathSrc}respuesta_4.jpg")
opcion_4_imagen = pygame.transform.scale(opcion_4_imagen, (imagen_ancho, imagen_alto))
opcion_5_imagen = pygame.image.load(f"{pathSrc}respuesta_5.jpg")
opcion_5_imagen = pygame.transform.scale(opcion_5_imagen, (imagen_ancho, imagen_alto))
opcion_6_imagen = pygame.image.load(f"{pathSrc}respuesta_6.jpg")
opcion_6_imagen = pygame.transform.scale(opcion_6_imagen, (imagen_ancho, imagen_alto))
cartas_1_image = pygame.image.load(f"{pathSrc}carta_1.png")
cartas_1_image = pygame.transform.scale(cartas_1_image, (imagen_ancho + 30, imagen_alto + 30))
cartas_2_image = pygame.image.load(f"{pathSrc}carta_2.png")
cartas_2_image = pygame.transform.scale(cartas_2_image, (imagen_ancho + 30, imagen_alto + 30))
cartas_3_image = pygame.image.load(f"{pathSrc}carta_3.png")
cartas_3_image = pygame.transform.scale(cartas_3_image, (imagen_ancho + 30, imagen_alto + 30))
cartas_4_image = pygame.image.load(f"{pathSrc}carta_4.png")
cartas_4_image = pygame.transform.scale(cartas_4_image, (imagen_ancho + 30, imagen_alto + 30))
cartas_5_image = pygame.image.load(f"{pathSrc}carta_5.png")
cartas_5_image = pygame.transform.scale(cartas_5_image, (imagen_ancho + 30, imagen_alto + 30))
cartas_6_image = pygame.image.load(f"{pathSrc}carta_6.png")
cartas_6_image = pygame.transform.scale(cartas_6_image, (imagen_ancho + 30, imagen_alto + 30))

eclipses = [opcion_1_imagen, opcion_2_imagen, opcion_3_imagen, opcion_4_imagen, opcion_5_imagen, opcion_6_imagen]

# Diccionario que asocia las opciones de la izquierda con las cartas de la derecha
asociacion_cartas = {
    opcion_1_imagen: cartas_1_image,
    opcion_2_imagen: cartas_2_image,
    opcion_3_imagen: cartas_3_image,
    opcion_4_imagen: cartas_4_image,
    opcion_5_imagen: cartas_5_image,
    opcion_6_imagen: cartas_6_image,
}

# Posiciones de las imágenes en la pantalla
posiciones_izquierda = [(100, 100), (100, 250), (100, 400)]
posiciones_derecha = [(500, 100), (500, 250), (500, 400)]

# Lista de tuplas que almacena la posición actual de las imágenes en la izquierda
coordenadas_izquierda = []

# Lista de tuplas que almacena la posición actual de las cartas en la derecha
coordenadas_derecha = []

# Crear una copia de la lista de eclipses para mantener las imágenes disponibles
eclipses_disponibles = eclipses.copy()

# Estructura de preguntas_respuestas
preguntas_respuestas = [
    {
        "pregunta": "Relates the corresponding eclipse",
        "opciones": [],
        "respuesta_correcta": opcion_2_imagen  # Respuesta correcta es la imagen de opción 2
    },
    # Agrega más preguntas con opciones y respuestas comunes aquí
]

# Selección aleatoria de las imágenes de la izquierda sin repetir
for _ in range(3):
    opcion_elegida = random.choice(eclipses_disponibles)
    preguntas_respuestas[0]["opciones"].append(opcion_elegida)
    eclipses_disponibles.remove(opcion_elegida)

imagenes_originales = preguntas_respuestas[0]["opciones"][:]
random.shuffle(imagenes_originales)

contexto = "Seek the embrace of the sky,\n the secrets of the eclipse, you must face,\n Prepare your knowledge, the grace of this puzzle,\nAnd you will see, the truth I trace"
lineas = contexto.split('\n')
font = pygame.font.Font(None, 36)

# Variables para controlar el tiempo de espera
tiempo_espera = 2000
inicio_espera = pygame.time.get_ticks()
espera_completa = False

# Variables para el arrastre de imágenes
arrastrando = False
imagen_arrastrada = None

# Variables para el botón "Comprobar"
color_boton = (0, 255, 0)  # Verde
boton_comprobar = pygame.Rect(550, 530, 200, 50)
font_boton = pygame.font.Font(None, 36)
texto_boton = "Comprobar"

# Variables para el mensaje de resultado
mensaje_resultado = ""
tiempo_mensaje = 0
tiempo_mensaje_correcto = 0  # Nuevo tiempo de mensaje para "Correcto"

# Función para mostrar el mensaje de resultado durante un tiempo específico
def mostrar_mensaje_resultado(mensaje, tiempo):
    global mensaje_resultado, tiempo_mensaje, tiempo_mensaje_correcto
    mensaje_resultado = mensaje
    tiempo_mensaje = tiempo * 60  # Convertir segundos a fotogramas


# Fase de introducción
while not espera_completa:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fondo negro

    # Dibuja el texto de introducción en la pantalla
    for i, linea in enumerate(lineas):
        texto_surface = font.render(linea, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect()
        texto_rect.centerx = window_size[0] // 2
        texto_rect.centery = window_size[1] // 2 - len(lineas) * 20 + i * 40
        screen.blit(texto_surface, texto_rect)

    pygame.display.flip()

    # Controla el tiempo de espera
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - inicio_espera >= tiempo_espera:
        espera_completa = True

# Fase principal del juego
running = True
respuesta_seleccionada = None  # Almacena la respuesta seleccionada por el usuario

# Obtener las coordenadas iniciales de las imágenes en la izquierda y las cartas en la derecha
coordenadas_izquierda = posiciones_izquierda[:]
coordenadas_derecha = posiciones_derecha[:]
cartas_en_pantalla = {}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si el usuario hizo clic en una opción
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, imagen in enumerate(imagenes_originales):
                x, y = coordenadas_izquierda[i]
                rect_imagen = pygame.Rect(x, y, imagen_ancho, imagen_alto)
                if rect_imagen.collidepoint(mouse_x, mouse_y):
                    arrastrando = True
                    imagen_arrastrada = i  # Rastrea la imagen que se está arrastrando

        elif event.type == pygame.MOUSEMOTION and arrastrando:
            # Actualiza la posición de la imagen arrastrada
            x, y = pygame.mouse.get_pos()
            coordenadas_izquierda[imagen_arrastrada] = (x - imagen_ancho / 2, y - imagen_alto / 2)

        elif event.type == pygame.MOUSEBUTTONUP:
            # Detiene el arrastre cuando se suelta el botón del mouse
            arrastrando = False

            # Verificar si el usuario hizo clic en el botón "Comprobar"
            if boton_comprobar.collidepoint(event.pos):
                correcto = True

                for opcion_imagen, carta_imagen in zip(imagenes_originales, preguntas_respuestas[0]["opciones"]):
                    x_opcion, y_opcion = coordenadas_izquierda[imagenes_originales.index(opcion_imagen)]
                    rect_opcion = pygame.Rect(x_opcion, y_opcion, imagen_ancho, imagen_alto)
                    
                    x_carta, y_carta = cartas_en_pantalla[carta_imagen]
                    
                    rect_carta = pygame.Rect(x_carta, y_carta, imagen_ancho + 30, imagen_alto + 30)

                    if not rect_opcion.colliderect(rect_carta):
                        correcto = False
                        break
                if correcto:
                    mostrar_mensaje_resultado("Correcto", 360)  # Mostrar mensaje "Correcto" durante 4 segundos
                    running = False
                else:
                    mostrar_mensaje_resultado("Incorrecto", 3)  # Mostrar mensaje "Incorrecto" durante 3 segundos
                    # Restaurar las imágenes a sus posiciones originales
                    coordenadas_izquierda = posiciones_izquierda[:]

    screen.fill((255, 255, 255))

    # Dibuja la pregunta en la parte superior de la pantalla
    pregunta_surface = font.render(f"{preguntas_respuestas[0]['pregunta']}", True, (0, 0, 0))
    pregunta_rect = pregunta_surface.get_rect()
    pregunta_rect.centerx = window_size[0] // 2
    pregunta_rect.y = 50
    screen.blit(pregunta_surface, pregunta_rect)

    # Dibuja las imágenes de las opciones en la pantalla según sus posiciones
    for i, imagen in enumerate(imagenes_originales):
        x, y = coordenadas_izquierda[i]
        screen.blit(imagen, (x, y))

    # Dibuja las cartas en la derecha basadas en la asociación de imágenes
    for i, opcion_imagen in enumerate(preguntas_respuestas[0]["opciones"]):
        x, y = coordenadas_derecha[i]
        cartas_en_pantalla[opcion_imagen] = (x, y)
        carta_asociada = asociacion_cartas[opcion_imagen]
        screen.blit(carta_asociada, (x, y))

    # Dibuja el botón "Comprobar"
    pygame.draw.rect(screen, color_boton, boton_comprobar)
    texto_boton_surface = font_boton.render(texto_boton, True, (0, 0, 0))
    texto_boton_rect = texto_boton_surface.get_rect()
    texto_boton_rect.center = boton_comprobar.center
    screen.blit(texto_boton_surface, texto_boton_rect)

    # Dibuja el mensaje de resultado si es necesario
    if tiempo_mensaje > 0:
        resultado_surface = font.render(mensaje_resultado, True, (255, 0, 0))
        resultado_rect = resultado_surface.get_rect()
        resultado_rect.centerx = window_size[0] // 2
        resultado_rect.centery = window_size[1] // 2
        screen.blit(resultado_surface, resultado_rect)
        tiempo_mensaje -= 1

    pygame.display.flip()

pygame.quit()
sys.exit()
