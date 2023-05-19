"""Simular un juego de blackjack"""

"""Del paquete random importamos las funciones choice y sample"""
from random import choice, sample

jugar = True
dinero_jugador = 20000
while jugar == True:
    """Crear un diccionario para obtener el valor de cada carta"""
    cartas = {
        chr(0x1f0a1) : 11,
        chr(0x1f0a2) : 2,
        chr(0x1f0a3) : 3,
        chr(0x1f0a4) : 4,
        chr(0x1f0a5) : 5,
        chr(0x1f0a6) : 6,
        chr(0x1f0a7) : 7,
        chr(0x1f0a8) : 8,
        chr(0x1f0a9) : 9,
        chr(0x1f0aa) : 10,
        chr(0x1f0ab) : 10,
        chr(0x1f0ad) : 10,
        chr(0x1f0ae) : 10,
    }

    """Crearemos una lista de cartas de donde podremos elegir una carta"""
    lista_cartas = list(cartas)

    """Haremos que el jugador pueda elegir dos cartas, una a continuación de la otra"""
    carta = choice(lista_cartas)

    """Sumamos el valor de la carta"""
    puntaje = cartas[carta]

    carta = choice(lista_cartas)
    puntaje += cartas[carta]

    """La casa elige dos cartas al azar"""
    casa = sample(lista_cartas, 2)
    puntaje_casa = sum(cartas[carta] for carta in casa)

    if puntaje > puntaje_casa:
        print("El puntaje del jugador es:", puntaje, " y el puntaje de la casa es:", puntaje_casa, "EL JUGADOR GANA")
        dinero_jugador += 2000
    else:
        print("El puntaje del jugador es:", puntaje, " y el puntaje de la casa es:", puntaje_casa, "LA CASA GANA")
        dinero_jugador -= 2000

    print("Dinero:", dinero_jugador)
    opcion = int(input("Desea seguir jugando? 1. Si; 2. No:"))
    if opcion == 1 and dinero_jugador > 0:
        jugar = True
    else:
        print("El dinero ganado son:", dinero_jugador, "pesos")
        jugar = False



