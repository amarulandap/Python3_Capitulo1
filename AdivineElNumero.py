"""Juego de adivine un número entero entre 0 y 100"""
import sys

"""Importar el paquete para generar un número aleatorio que es el que debe adivinar el jugador"""
import random

"""Generar el número que debe ser adivinado"""
numero = random.randint (0, 100)

"""Ingresar al ciclo para poder permitir un numero indefinido de intentos"""
nroIntentos = 0
cont = True

while cont == True:
    try:
        intento = int(input("Ingrese un número entre 0 y 100: "))
    except ValueError as e:
        print("Valor erroneo", file=sys.stderr)
        sys.exit()

    nroIntentos += 1
    """print(numero)"""

    if intento >= 0 and intento <= 100:

        if numero == intento:
            print ("Ha ganado", numero, "=", intento)
            print ("Intentos: ", nroIntentos)
            cont = False
        elif intento <= numero - 20:
            print ("Demasiado pequeño")
        elif intento <= numero - 10 and intento > numero - 20:
            print ("Pequeño")
        elif intento < numero and intento > numero - 10:
            print ("Muy cerca")
        elif intento >= numero + 20:
            print ("Demasiado grande")
        elif intento >= numero + 10 and intento < numero + 20:
            print ("Grande")
        elif intento > numero and intento < numero + 10:
            print("Muy cerca")
    else:
        print("Error, recuerde que debe ser un número entre 0 y 100")
        nroIntentos -= 1

print("Fin del juego")