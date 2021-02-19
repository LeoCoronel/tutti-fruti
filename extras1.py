import pygame
from pygame.locals import *
from configuracion1 import *

def obtenerListas():
    colores = []
    paises = []
    animales = []
    nombres = []
    capitales = []
    archivo = open('animales.txt', 'r')
    for linea in archivo:
        animales.append(linea[:-1])
    archivo.close()
    archivo = open('nombres.txt', 'r')
    for linea in archivo:
        nombres.append(linea[:-1])
    archivo.close()

    archivo = open('colores.txt', 'r')
    for linea in archivo:
        colores.append(linea[:-1])
    archivo.close()

    archivo = open('paises.txt', 'r')
    for linea in archivo:
        paises.append(linea[:-1])
    archivo.close()

    archivo = open('nombres.txt', 'r')
    for linea in archivo:
        nombres.append(linea[:-1])
    archivo.close()

    archivo = open('capitales.txt', 'r')
    for linea in archivo:
        capitales.append(linea[:-1])
    archivo.close()

    listaDeTodo = [colores, paises, capitales, animales,nombres]

    return listaDeTodo
listaDeTodo= obtenerListas()#
lista_delistas=[]
for i in listaDeTodo:# formar una unica lista para poder cambiar de color si la palabra es correcta
    lista_delistas+=i


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, letra, item, palabraUsuario, puntos, temporizador):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #Linea Horizontal
    # pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, NEGRO), ((ANCHO / 2) - 50, 500))

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Tiempo: " + str(round(temporizador)), 1, COLOR_TIEMPO_FINAL if temporizador >60 else COLOR_TEXTO)
    ren3 = defaultFontMUYGRANDE.render(item, 1, NEGRO)
    ren4 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_LETRA)
    ren5 = defaultFont.render("Presiona 0 para pausar", 1, NEGRO)

    screen.blit(ren1, (670, 35))
    screen.blit(ren2, (10, 35))
    screen.blit(ren3, ((ANCHO//2-((len(item)//2) - (-1))*TAMANO_LETRA_GRANDE), ALTO//2))
    screen.blit(ren4, (ANCHO//2-TAMANO_LETRA_GRANDE, 50))
    screen.blit(ren5, ((ANCHO-525, ALTO-350)))

def dibujarSalida(screen, letra, items, eleccionUsuario, eleccioncompu, puntos, temporizador,lista_delistas, puntaje):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #Linea Horizontal
    #pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Tiempo: " + str(round(temporizador)), 1, COLOR_TIEMPO_FINAL if temporizador > 60 else COLOR_TEXTO)
    ren3 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_LETRA)
    ren4 = defaultFontGRANDE.render("Puntos: ", 1, COLOR_TIEMPO_FINAL if puntos <= 0 else COLOR_LETRAS)
    ren5 = defaultFontGRANDE.render("Categoria" +" "+" "+" "+ " "+" " +"Usuario"+" "+" " +" "+" "+" "+" "+" "+" "+" "+" "+ "Puntos"+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "  +"Compu" ,1,COLOR_TEXTO)
    ren6 = defaultFont.render("Presiona 9 para jugar otra vez", 1, NEGRO)

    screen.blit(ren1, (ANCHO - 260, 30))
    screen.blit(ren2, (115, 30))
    screen.blit(ren3, (ANCHO//2-TAMANO_LETRA_GRANDE, 40))
    screen.blit(ren4, (45, 525))
    screen.blit(ren5, (30, 120))
    screen.blit(ren6, (ANCHO - 320, 85))
    p=[str(puntos)]

    y=525
    for palabra in p:
        screen.blit(defaultFontGRANDE.render(palabra,1,COLOR_TIEMPO_FINAL if puntos <= 0 else COLOR_LETRAS),(430, y))

    y=200
    for palabra in items:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_TEXTO), (50, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=200
    for palabra in eleccionUsuario:
        if palabra in lista_delistas:
            screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRAS), (225, y))
            y=y+TAMANO_LETRA_GRANDE*2
        else:
            screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRA), (225, y))
            y=y+TAMANO_LETRA_GRANDE*2

    y=200
    for palabra in puntaje:
        if palabra == "10":
            screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRAS), (430, y))
            y=y+TAMANO_LETRA_GRANDE*2
        if palabra == "15":
            screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRAS), (430, y))
            y=y+TAMANO_LETRA_GRANDE*2
        if palabra != "10" and palabra != "15":
            screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRA), (430, y))
            y=y+TAMANO_LETRA_GRANDE*2

    y=200
    for palabra in eleccioncompu:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRAS), (580, y))
        y=y+TAMANO_LETRA_GRANDE*2



