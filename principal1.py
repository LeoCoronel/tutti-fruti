#!/usr/bin/env python3

import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion1 import *
from funcionesVACIAS1 import *
from extras1 import *




def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Obtener imagenes
    background = pygame.image.load(os.path.join("img", "fondoGame.png"))
    backgroundFinal = pygame.image.load(os.path.join("img", "fondoPuntaje.png"))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    puntos = 0
    candidata = ""
    puntaje=[]
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    items=["Colores","Paises","Capitales","Animales", "Nombres"]


    listaDeTodo = obtenerListas()
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]
    eleccionCompu=juegaCompu(letraAzar, listaDeTodo)#la pase aca para poder verificar si la palabra elegida por el usuario esta en la lista de juegacompu
    i=0

    #Elementos para la pausa
    clock = pygame.time.Clock()
    temporizador = 0
    temporizador2 = 0
    pausa = False

    menu = True
    backgroundMenu = pygame.image.load('img/menu.png')

    jugarDeNuevo = False

    # MUSICA

    pygame.mixer.music.load("music/menu_mus.mp3")
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.3)

    correctSound = pygame.mixer.Sound("music/correct.wav")
    correctSound.set_volume(0.2)
    incorrectSound = pygame.mixer.Sound("music/incorrect.wav")
    incorrectSound.set_volume(0.2)
    tecla = pygame.mixer.Sound("music/switch.wav")
    tecla.set_volume(0.2)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False

        screen.fill((0,0,0))

        clock.tick()
        screen.blit(backgroundMenu, (0,0))

        pygame.display.update()



    while i < len(items):
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        fps = 3

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
                return
            if e.type == KEYDOWN:
                 if e.key == K_0:
                    pausa = not pausa
                    clock.tick()
                 if pausa != True:
                    letra = dameLetraApretada(e.key)
                    tecla.play()
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        if palabraUsuario == "" and e.key == K_RETURN:
                            palabraUsuario="-"
                            sumar=-5
                        # lista para poner el puntaje en la pantalla final
                        puntaje.append(str(esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo,i,eleccionCompu)))
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo,i,eleccionCompu)
                        if sumar == 10 or sumar == 15:
                            correctSound.play()
                        else:
                            incorrectSound.play()
                        puntos += sumar
                        palabraUsuario=""
                        i=i+1


        if pausa == False:
            temporizador += temporizador2
            pygame.display.update()
            temporizador2 = clock.tick() / 1000
##        segundos = pygame.time.get_ticks() / 1000

        # limpiar pantalla anterior
        screen.fill(COLOR_FONDO)
        # Agrego background
        screen.blit(background, (0,0))

        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, temporizador)
        else:
            screen.blit(backgroundFinal, (0,0))
##            eleccionCompu=juegaCompu(letraAzar, listaDeTodo)# se paso a la linea 46
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, temporizador,lista_delistas,puntaje)


        pygame.display.flip()


        pygame.display.update()

    while i >= len(items):
        jugarDeNuevo = True
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
                return
            if e.type == KEYDOWN:
                if jugarDeNuevo == True and e.key == K_9:
                    main()
                    pygame.init()




    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
