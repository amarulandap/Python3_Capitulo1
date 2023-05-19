"""Introducción a los generadores"""

def generador(numero):

    for i in range(numero):
        yield i
        print('Generador %d' % i)


"""Invocamos la función para que el generador pueda ser usado"""
gen = generador(10)

"""next(gen) me permite invocar el valor siguiente de un generador"""


"""Visualizamos los números generador en la función"""
for num in gen:
    print(num)


"""Sintaxis Yield From para no tener que usar ciclos anidados"""
def cadena(*iters):

    for it in iters:
        for item in it:
            yield item


def cadena1(*iters):

    for it in iters:
        yield from it


"""Construcción condicional"""
pelicula = 1

if pelicula == 1:
    print("\nEl señor de los anillos")
else:
    print("El Hobbit")

film = 1 if (pelicula == 1) else 0
print(pelicula)