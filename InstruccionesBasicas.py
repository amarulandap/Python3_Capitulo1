"""Mi primer programa"""

"""Importar el módulo sys para poder gestionar excepciones"""

import sys


"""Instrucción: Es una unica línea de código que se compone de una función y un literal."""

print("Hola Andres")
print("Bienvenido al mundo de Python")


"""Mostrar en pantalla una info ingresada por el usuario"""

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
print("Su nombre es: ", nombre, apellido)


"""Utilizar valores booleanos, que son el resultado de una operación de comparación.
   <, <=, >, >=, ==, !=
   Para almacenar datos númericos ingresados desde el teclado se debe hacer un casteo"""

try:
    numero1 = int(input("Ingrese un número entero: "))
except ValueError as e:
    print("Valor erroneo", file=sys.stderr)
    sys.exit()

try:
    numero2 = int(input("Ingrese un segundo número entero: "))
except ValueError as e:
    print("Valor erroneo", file=sys.stderr)
    sys.exit()


comparacion = numero1 < numero2
suma = numero1 + numero2
print(numero1, 'es menor que', numero2, ':', comparacion)
print(numero1, '+', numero2, '=', suma)





