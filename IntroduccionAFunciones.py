"""Crear una programa que nos permita realizar diferentes operaciones con dos o tres números enteros usando funciones"""
import sys

def PedirNumero ():

    try:
        numero = int(input("Ingrese un número entero: "))
    except ValueError as e:
        print("Valor erroneo, recuerde que debe ser un número entero", file=sys.stderr)
        """sys.exit()"""
        numero = 0

    return numero

"""los parámetros por defecto me permiten asignarle un valor a uno de ellos, 
en caso de que no sea incluido en la llamada a la función"""
def SumarNumeros (sumandoUno=0, sumandoDos=0, sumandoTres=0):

    suma = sumandoUno + sumandoDos + sumandoTres

    print("Resultado : " + str(sumandoUno) + " + " + str(sumandoDos) + " + " + str(sumandoTres) + "=", suma)

def RestarNumeros (operandoUno=0, operandoDos=0, operandoTres=0):

    resta = operandoUno - operandoDos - operandoTres

    print("Resultado :" + str(operandoUno) + " - " + str(operandoDos) + " - " + str(operandoTres) + " = ", resta)

def MultiplicarNumeros (operandoUno=0, operandoDos=0):

    producto = operandoUno * operandoDos

    print("Resultado : " + str(operandoUno) + " * " + str(operandoDos) + " = ", producto)

def DividirNumeros (dividendo, divisor):

    if divisor == 0:
        print("Error, división por cero")
        division = 0
    else:
        division = dividendo / divisor

    return division


"""Los llamados a las funciones se deben hacer luego de crearlas"""
numero1 = PedirNumero()
numero2 = PedirNumero()
numero3 = PedirNumero()
SumarNumeros(numero1, numero2, numero3)
RestarNumeros(numero1, numero2)
MultiplicarNumeros(numero3, numero1)
division = DividirNumeros(numero1, numero2)
print("Resultado : " + str(numero1) + " / " + str(numero2) + " = ",division)




