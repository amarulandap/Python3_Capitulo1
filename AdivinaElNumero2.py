"""Desarrollar una segunda versión del juego Adivina el número"""
import sys
import random

"""Esta función valida que se haya introducido un número"""
def validarNumero (invitacion):
    while True:

        try:
            entrada = int(input(invitacion))
        except:
            print("Error, solo números entre 0 - 99", file=sys.stderr)
        else:
            return entrada


"""Pedirle al usuario que ingrese un número dentro del rango definido para jugar"""
def pedirNumeroLimite (invitacion, minimo, maximo):
    while True:

        invitacion = "{} entre {} y {} incluidos: ".format(invitacion, minimo, maximo)

        """Donde se almacenará el número ingresado por el usuario"""
        entrada = validarNumero(invitacion)
        if (minimo <= entrada and entrada <= maximo):
            return entrada


"""A través de esta función se ejecutará el juego"""
def jugarUnaVez (numero, minimo, maximo):

    """Almacenará el número ingreasdo por el usuario"""
    intento = pedirNumeroLimite("Adivine el numero", minimo, maximo)

    if intento < numero:
        print("Menor que")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Mayor que")
        maximo = intento - 1
        victoria = False
    else:
        print("Advinaste el número")
        victoria = True
        minimo = maximo = intento

    return victoria, minimo, maximo


"""Definir los números límites del juego"""
def definirLimites ():
    minimo = validarNumero("Ingrese el limite inferior: ")
    maximo = validarNumero("Ingrese el limite superior: ")

    return minimo, maximo

minimo, maximo = definirLimites()

"""Número a adivinar"""
numero = random.randint (minimo, maximo)

while True:
    victoria, minimo, maximo = jugarUnaVez(numero, minimo, maximo)

    if victoria == True:
        break











