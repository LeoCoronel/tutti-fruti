from configuracion1 import *
from principal1 import *
from extras1 import *
import math
import random

listaDeTodo= obtenerListas()
def unaAlAzar(lista):
    return random.choice(lista)

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo,i,eleccionCompu):
    if palabraUsuario[0] == letra and palabraUsuario in listaDeTodo[i]:
        if palabraUsuario in eleccionCompu:
            return 15
        else:
            return 10
    else:

        return -5



def juegaCompu(letraAzar, listaDeTodo):
    salida=[]
    posibles = []
    cont = 0
    cant = len(listaDeTodo)
    while cont < cant:
        for x in range(cant):
            for i in listaDeTodo[x]:
                if letraAzar == i[0]:
                    posibles.append(i)
            if len(posibles) < 1:
                salida.append("-")
                posibles = []
            else:
                salida.append(random.choice(posibles))
                posibles = []
            cont += 1
    return salida

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

    archivo = open('colores.txt', 'r')
    for linea in archivo:
        colores.append(linea[:-1])
    archivo.close()

    archivo = open('paises.txt', 'r')
    for linea in archivo:
        paises.append(linea[:-1])
    archivo.close()

    archivo = open('capitales.txt', 'r')
    for linea in archivo:
        capitales.append(linea[:-1])
    archivo.close()

    archivo = open('nombres.txt', 'r')
    for linea in archivo:
        nombres.append(linea[:-1])
    archivo.close()

    listaDeTodo = [
        colores,
        paises,
        capitales,
        animales,
        nombres
    ]

    return listaDeTodo

