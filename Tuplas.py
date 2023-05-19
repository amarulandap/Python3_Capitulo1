"""Introducción al manejo de las tuplas"""

"""Crear una tupla"""
tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("tupla1:", tupla1)

tupla2 = 9, 8, 7, 6, 5, 4, 3, 2, 1
print("tupla2:", tupla2)

tupla3 = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 0))
print("tupla3:", tupla3)

"""Convertir una lista en tupla"""
lista1 = list("Esta es una lista que se convertira en tupla")
print("\nlista1:", lista1)
tupla4 = tuple(lista1)
print("tupla4:", tupla4)


"""Recorrer una tupla"""
for tp in tupla3:
    print(tp)

print("\n")
for tp in tupla3:
    for tp1 in tp:
        print(tp1)

"""Las tuplas son inmutables, por lo tanto no se pueden agregar, eliminar o modificar datos"""

"""Asignarle los datos de una tupla a un conjunto de variables"""
a, b, c, d, e, f, g, h, i = tupla1
print(a, '', b, '', c, '', d, '', e, '', f, '', g, '', h, '', i)


"""Métodos de la clase tuple"""
print("la a aparece:", tupla4.count('a'), "veces")

print("la letra s aparece por primera vez en la", tupla4.index('s'), "posición")

print("La segunda letra s aparece en la", tupla4.index('s', 2), "posición")


"""Conocer el tamaño de una tupla"""
tamaño1 = len(tupla1)
print("El tamaño de la tupla 1 es:", tamaño1)


"""Acceder a un dato de la tupla"""
print("dato de la posición 2:", tupla2[2])
print("Datos de las posiciones 0 a 3", tupla2[:4])


"""Concatenar dos tuplas"""
tupla5 = tupla1 + tupla2
print(tupla5)