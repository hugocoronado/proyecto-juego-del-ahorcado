import pygame
import random

# Configuración de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 128, 0)
NARANJA = (255, 127, 80)
# Lista de palabras para adivinar
PALABRAS = ["PYTHON", "PROGRAMAR", "CORRER", "COMPUTADORA", "COMER", "INTELIGENCIA", "ESTUDIAR", "MUNDO", "HOLA"]

# Función para seleccionar una palabra aleatoria de la lista
def seleccionar_palabra():
    return random.choice(PALABRAS)

# Función principal
def main():
    # Inicializar Pygame
    pygame.init()

    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ahorcado")

    # Cargar imágenes del ahorcado
    imagenes_ahorcado = [pygame.image.load("ahorcado0.png"), pygame.image.load("ahorcado1.png"),
                         pygame.image.load("ahorcado2.png"), pygame.image.load("ahorcado3.png"),
                         pygame.image.load("ahorcado4.png"), pygame.image.load("ahorcado5.png"),
                         pygame.image.load("ahorcado6.png")]

    # Variables para el juego
    palabra_secreta = seleccionar_palabra()
    letras_acertadas = ['_' for _ in palabra_secreta]
    letras_intentadas = []
    intentos_restantes = 6

    # Cargar música
    pygame.mixer.music.load("win_sound.mp3")
    perder_sound = pygame.mixer.Sound("lose_sound.mp3")
    letra_sound = pygame.mixer.Sound("letra_sound.mp3")  # Cargar el sonido para cada letra ingresada

    # Bucle principal del juego
    jugando = True
    while jugando:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.KEYDOWN:
                if pygame.key.name(evento.key).isalpha() and len(pygame.key.name(evento.key)) == 1:
                    letra = pygame.key.name(evento.key).upper()
                    if letra not in letras_intentadas:
                        letra_sound.play()  # Reproducir el sonido al ingresar una letra
                        letras_intentadas.append(letra)
                        if letra in palabra_secreta:
                            for i, l in enumerate(palabra_secreta):
                                if l == letra:
                                    letras_acertadas[i] = letra
                        else:
                            intentos_restantes -= 1

        # Limpiar pantalla
        pantalla.fill(BLANCO)

        # Dibujar imagen del ahorcado
        pantalla.blit(imagenes_ahorcado[6 - intentos_restantes], (0, 0))

        # Dibujar palabra secreta
        font = pygame.font.SysFont(None, 30)
        palabra_render = font.render(' '.join(letras_acertadas), True, NEGRO)
        pantalla.blit(palabra_render, (400, 250))

        # Dibujar letras intentadas
        letras_intentadas_render = font.render('Letras intentadas: ' + ', '.join(letras_intentadas), True, NARANJA)
        pantalla.blit(letras_intentadas_render, (360, 100))

        # Dibujar intentos restantes
        intentos_render = font.render('Intentos restantes: ' + str(intentos_restantes), True, ROJO)
        pantalla.blit(intentos_render, (400, 300))

        # Actualizar pantalla
        pygame.display.flip()

        # Verificar si se ganó o se perdió
        if '_' not in letras_acertadas:
            pygame.mixer.music.play()
            font_ganar = pygame.font.SysFont(None, 50)
            ganar_render = font_ganar.render('¡Ganaste!', True, VERDE)
            pantalla.blit(ganar_render, (400, 360))
            pygame.display.flip()
            pygame.time.delay(3000)
            jugando = False
        elif intentos_restantes == 0:
            perder_sound.play()
            font_perder = pygame.font.SysFont(None, 30)
            perder_render = font_perder.render('¡Perdiste! La palabra era: ' + palabra_secreta, True, NARANJA)
            pantalla.blit(perder_render, (300, 330))
            pygame.display.flip()
            pygame.time.delay(3000)
            jugando = False

    # Esperar hasta que el usuario cierre la ventana
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

# Llamar a la función main
main()
