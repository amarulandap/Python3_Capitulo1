"""Importar los modulos necesarios"""

import sys

"""Solicitar al usuario que ingrese dos números, gestionando la posible excepción"""

try:
    numero1 = int(input("Ingrese el primer número: "))
except ValueError as e:
    print("Valor erroneo", file=sys.stderr)
    sys.exit()

try:
    numero2 = int(input("Ingrese el segundo número: "))
except ValueError as e:
    print("Valor erroneo", file=sys.stderr)
    sys.exit()

"""Condicional simple"""

if numero1 == numero2:
    print(numero1, " es igual a ", numero2)

"""Condicional Doble"""

if numero1 <= numero2:
    print(numero1, " es menor que ", numero2)
else:
    print(numero2, " es menor que ", numero1)

"""Condicional multiple"""

try:
    numero3 = int(input("Ingrese un tercer número: "))
except ValueError as e:
    print("Valor erroneo", file=sys.stderr)
    sys.exit()

if numero1 == numero3:
    print(numero1, " es igual a ", numero3)
elif numero2 == numero3:
    print(numero2, " es igual a ", numero3)
elif numero1 < numero3 and numero2 < numero3:
    print(numero3, " es el número mayor")
elif numero2 < numero1 and numero3 < numero1:
    print(numero1, " es el número mayor")
else:
    print(numero2, " es el número mayor")


"""Ciclo for"""

for a in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19):
    print("Número impar:", a)

for b in range(0, 10, 2):
    print("Número menor que 10:", b)


"""Ciclo while"""

while True:
    try:
        numero4 = int(input("Ingrese un cuarto número: "))
    except:
        pass
    else:
        if 1 <= numero4 <= 10:
            break

print(numero4, "esta entre 1 y 10")







