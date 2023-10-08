import pygame
import random
import os

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find Wallo's Glasses")

# Cargar la imagen de fondo
background = pygame.image.load(os.path.join("images", "background.jpg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Definir fuente de texto (Times New Roman)
font = pygame.font.Font(os.path.join("fonts", "times.ttf"), 36)  # Ruta a la fuente
bold_font = pygame.font.Font(os.path.join("fonts", "times.ttf"), 36)  # Ruta a la fuente
bold_font.set_bold(True)

# Cargar sonido de felicitaciones
congratulations_sound = pygame.mixer.Sound(os.path.join("sounds", "congratulations.mp3"))  # Ruta al sonido

# Clase para representar objetos clickeables
class ClickableObject:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        screen.blit(self.image, self.rect)

    def check_collision(self, pos):
        return self.rect.collidepoint(pos)

# Función para mostrar mensajes emergentes con fondo blanco ajustado al texto
def show_message(message):
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))  # Mensaje en la parte inferior
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)

    pygame.draw.rect(screen, (255, 255, 255), background_rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(1500)  # Muestra el mensaje durante 1.5 segundos

# Cargar la imagen correcta y crear objetos clickeables incorrectos
correct_image = pygame.image.load(os.path.join("images", "glasses.png"))
correct_image = pygame.transform.scale(correct_image, (100, 100))
correct_object = ClickableObject(correct_image, random.randint(50, WIDTH - 150), random.randint(HEIGHT // 2, HEIGHT - 150))

incorrect_images = [
    pygame.image.load(os.path.join("images", "object1.png")),
    pygame.image.load(os.path.join("images", "object2.png")),
    pygame.image.load(os.path.join("images", "object3.png")),
    pygame.image.load(os.path.join("images", "object4.png")),
    pygame.image.load(os.path.join("images", "object5.png"))
]

incorrect_images = [pygame.transform.scale(img, (100, 100)) for img in incorrect_images]

# Asegurar que los objetos no se sobrepongan en la parte inferior
positions = []
while len(positions) < len(incorrect_images) + 1:
    x, y = random.randint(50, WIDTH - 150), random.randint(HEIGHT // 2, HEIGHT - 150)
    valid_position = all(
        pygame.Rect(x, y, 100, 100).colliderect(pygame.Rect(px, py, 100, 100)) == False
        for px, py in positions
    )
    if valid_position:
        positions.append((x, y))

correct_object.rect.topleft = positions[0]
incorrect_objects = [ClickableObject(img, x, y) for img, (x, y) in zip(incorrect_images, positions[1:])]

# Texto superior izquierda (contexto y pregunta)
context_text = "Help Wallo find his glasses to see the eclipse."
question_text = "Where are the glasses?"

# Variable para rastrear el estado del juego
game_over = False

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Verifica el clic izquierdo del ratón
            if not game_over:
                pos = pygame.mouse.get_pos()
                for obj in incorrect_objects:
                    if obj.check_collision(pos):
                        show_message("Keep trying to find the glasses.")
                if correct_object.check_collision(pos):
                    show_message("Congratulations! You found Wallo's glasses.")
                    congratulations_sound.play()  # Reproduce el sonido de felicitaciones
                    game_over = True

    # Dibujar fondo
    screen.blit(background, (0, 0))

    # Dibujar objetos clickeables
    for obj in incorrect_objects:
        obj.draw()
    correct_object.draw()

    # Dibujar texto en la parte superior de la pantalla (contexto y pregunta en azul)
    context_surface = bold_font.render(context_text, True, (0, 0, 255))  # Color azul
    context_rect = context_surface.get_rect(center=(WIDTH // 2, 30))  # Texto en la parte superior
    screen.blit(context_surface, context_rect)

    question_surface = bold_font.render(question_text, True, (0, 0, 255))  # Color azul
    question_rect = question_surface.get_rect(center=(WIDTH // 2, 80))  # Texto en la parte superior
    screen.blit(question_surface, question_rect)

    pygame.display.flip()

# Salir del juego
pygame.quit()
