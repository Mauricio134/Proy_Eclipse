import random
import pygame

#Puzzle 2
# Listas de opciones
opciones_totales_i = ["5 lunares 2 solares", "4 lunares 3 solares", "3 lunares 4 solares", "2 lunares 5 solares", "1 lunar y 6 solares"]
mensajes_error = ["Se nos chispoteo...","Tal vez debamos buscar por otros mares...", "Houston tenemos un problema...", "Es buena la intencion, la respuesta no, pero la intencion está...", "Sabemos que sabes que sabemos ¿verdad?"]
opciones_totales_c = ["7 solares y 3 lunares", "5 lunares y 1 solar", "1 solar y 6 lunares", "8 lunares y 0 solares"]
# Aleatoriedad
primeros_elementos = [opcion[0] for opcion in opciones_totales_i]
segundos_elementos = [opcion[1] for opcion in opciones_totales_i]

opciones_incorrectas = random.sample(opciones_totales_i, 3)
mensajes_e = random.sample(mensajes_error, 3)
opciones_correctas = random.sample(opciones_totales_c, 1)

# Concatenar respuesta correcta con las opciones incorrectas.
opciones_aleatorias = opciones_correctas + opciones_incorrectas

preguntas_respuestas = {
    "contexto": "Menos de 2 eclipses no existen por año,\ny tener más de 7 es demasiado raro.\nMínimo 2 eclipses solares encontraremos\ny los demás variarán dependiendo de ello.",
    "datos": {
        "pregunta": "¿Que enunciado es INCORRECTO según la cantidad\nde eclipses que pueden haber por año?",
        "opciones": opciones_aleatorias,
        "respuesta_correcta": opciones_correctas[0],
        "mensaje_i" : mensajes_e,
        "mensaje_c": "Correcto"
    }
}
def obtener_pregunta_aleatoria():
    #random.shuffle(opciones)
    ancho = 800
    alto = 600 
    window_size = (ancho, alto)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Juego de Eclipse")
    running = True

    pygame.init()

    color_fondo = (0, 0, 0)
    fuente = pygame.font.Font(None, 40)
    texto_con_saltos = preguntas_respuestas["contexto"]
    pregSaltos = preguntas_respuestas["datos"]["pregunta"]
    y = (alto - (3 * fuente.get_height())) // 2

    lineas = texto_con_saltos.split('\n')
    lineaPre = pregSaltos.split('\n')

    duracion_pantalla = 3000  # 3 segundos

    # Variables para controlar el cambio de pantalla
    tiempo_inicio_pantalla = pygame.time.get_ticks()
    pantalla_actual = 1

    color_rectangulo = (0, 173, 239)  # Celeste

    ancho_rectangulo = ancho//2 - 10
    alto_rectangulo = alto//8 - 2
    valor = 0
    ubi_click = []
    def punto_en_boton(x,y):
        return

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    valor = punto_en_boton(x,y)
        tiempo_actual = pygame.time.get_ticks()
        if pantalla_actual == 1 and tiempo_actual - tiempo_inicio_pantalla >= duracion_pantalla:
            pantalla_actual = 2
            tiempo_inicio_pantalla = tiempo_actual


        screen.fill(color_fondo)
        if pantalla_actual == 1:
            for i, linea in enumerate(lineas):
                texto_surface = fuente.render(linea, True, (255, 255, 255))
                texto_rect = texto_surface.get_rect()
                texto_rect.centerx = window_size[0] // 2
                texto_rect.centery = window_size[1] // 2 - len(lineas) * 20 + i * 40
                screen.blit(texto_surface, texto_rect)
        else:
            for i, linea in enumerate(lineaPre):
                texto_surface = fuente.render(linea, True, (255, 255, 255))
                texto_rect = texto_surface.get_rect()
                texto_rect.centerx = window_size[0] // 2
                texto_rect.centery = window_size[1] // 2 - len(lineas) * 20 + i * 40
                screen.blit(texto_surface, texto_rect)
            for _ in range(4):
                ubi_ancho = 0
                ubi_alto = 0
                if(_ < 2):
                    ubi_ancho = 8+(ancho_rectangulo+6) * _
                    ubi_alto = alto-alto_rectangulo - 8
                    pygame.draw.rect(screen, color_rectangulo, (ubi_ancho, ubi_alto, ancho_rectangulo, alto_rectangulo))
                else:
                    ubi_ancho = 8+(ancho_rectangulo+6)*(_-2)
                    ubi_alto = alto-alto_rectangulo - (16+alto_rectangulo)
                    pygame.draw.rect(screen, color_rectangulo, (ubi_ancho, ubi_alto, ancho_rectangulo, alto_rectangulo))
                texto_superficie = fuente.render(preguntas_respuestas["datos"]["opciones"][_], True, (255,255,255))

                # Obtener el rectángulo que rodea el texto
                rectangulo_texto = texto_superficie.get_rect()

                # Centrar el rectángulo del texto dentro del rectángulo del botón
                rectangulo_texto.center = ((ubi_ancho + ancho_rectangulo // 2), (ubi_alto + alto_rectangulo // 2))
                screen.blit(texto_superficie, rectangulo_texto)
                ubicacion = [ubi_ancho, ubi_alto]
                ubi_click.append(ubicacion)
        pygame.display.flip()
    pygame.quit()
    return