"""Para crear una lista"""
lista = list("Esta es la primera lista que creo en Python")
lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
print(lista)
print("Lista 1: ", lista1)
print("La longitud de la lista es:", len(lista))


"""Puedo buscar los elementos de izquierda a derecha o viceversa"""
print(lista[3], lista[-3])


"""Puedo obtener copias parciales de la lista"""
print("Los primeros seis elementos de la lista:", lista[:5])
print("Los últimos cuatro elementos de la lista:", lista[39:])
print("Una sublista intermedia:", lista[7:25])
print("Una copia con paso:", lista1[1::2])
print("Uno copia con paso, iniciando en el final:", lista1[-2::-2])


"""Reemplazar elementos dentro de una lista"""
lista1[3] = 8
print("Lista1 modificada:", lista1)
print("La longitud de la lista1 es:", len(lista1))
lista[11:17] = "segunda"
print("Lista modificada:", lista)


"""Eliminar elementos de la lista"""
existe = 5 in lista1
print(existe)

del lista1[4]
print("Lista1 con un elemento eliminado:", lista1)
print("La nueva longitud de la lista1 es:", len(lista1))

del lista[:4]
print("Lista con los primeros cuatro elementos eliminados:", lista)
print("la nueva longitud de lista es:", len(lista))


"""Valores"""
a = lista.index("a")
print("La primera posición de la letra a:", a)

cuenta = lista.count("a")
print("La letra a se repite:", cuenta, "veces")

lista1.remove(11)
print("Lista1 sin el número 11:", lista1)

print(lista1.pop())
print("Lista1 sin el último elemento:", lista1)

lista.append("3.11")
print("Lista con un elemento agregado:", lista)

lista1.insert(3, 6)
print("Lista1 con el número 6 insertado:", lista1)

lista.extend(["del", "curso", "Python3"])
print("Lista con una nueva lista agregada al final", lista)

print(lista + lista1)


"""Técnicas de iteración"""
lista2 = [2, 4, 6, 8, 10]
for numero in lista2:
    print(numero)

print("\n")
for indice, numero in enumerate(lista2):
    print("El elemento {1} esta en la posición {0}".format(indice, numero))

lista2_1 = [a ** 2 for a in range(10)]
print('La lista 2_1 es: ',lista2_1)


lista3 = [1, 3, 5, 7, 9]
lista4 = [11, 13, 15, 17, 19]

matriz = [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [11, 13, 15, 17, 19]]
print(matriz)

for fila in matriz:
    for columna in fila:
        print(columna)

for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        print("El elemento {2} esta en la posición [{0}],[{1}]".format(i, j, columna))

matriz_transpuesta = zip(matriz)
print(matriz_transpuesta)

for j, columna in enumerate(matriz_transpuesta):
    for i, fila in enumerate(columna):
        print("El elemento {2} está en la posición [{1}],[{0}]".format(i, j, fila))


"""Como ordenar listas"""
cadena = "Esta es la cadena de caracteres para ordenar, camino al éxito"
lista5 = cadena.split()
print(lista5)
lista5.sort(key=str.lower)

traduccion = str.maketrans("àäâéèëêïîöôùüûÿŷç_-",
                            "aaaeeeeiioouuuyyc_-",
                            "#~.?,;:!")

def transformacion(x):
    return x.lower().translate(traduccion)

lista5.sort(key=transformacion)
print("Lista5 ordenada:", lista5)

lista6 = [1, 4, 2, 6, 4, 8, 6, 9, 3, 6, 4, 8, 6, 0, 13, 5]
lista6.sort()
print("lista6 ordenada:", lista6)






