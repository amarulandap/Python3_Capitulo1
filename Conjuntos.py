"""Introducción al manejo de los Set"""

"""Declaración de un set"""
lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
conjunto1 = set(lista1)
print("set1:", conjunto1)

conjunto2 = set([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])
print("set2:", conjunto2)

conjunto3= {2, 4, 6, 8, 10, 8, 6, 5, 7, 9, 3, 2}
print("set2:", conjunto3)


"""No es posible modificar un elemento del set usando su indice"""


"""Iterar un set"""
for st in conjunto1:
    print(st)


"""Tamaño de un set"""
print("La longitud del conjunto 3 es:", len(conjunto3))


"""Determinar si un elemento pertenece a un set"""
existe = 11 in conjunto2
print(existe)


"""Unir dos sets"""
conjunto4 = {1, 2, 3}
conjunto5 = {4, 5, 6}
conjunto6 = conjunto4 | conjunto5
print("conjunto6:", conjunto6)

print("conjunto5 unido a conjunto4:", conjunto4.union(conjunto5))


"""Métodos"""
conjunto4.add(7)
print("conjunto4:", conjunto4)

conjunto5.remove(6)
print("Conjunto5:", conjunto5)

conjunto5.discard(6)
print("Conjunto5:", conjunto5)

conjunto4.pop()
print("conjunto4:", conjunto4)
conjunto4.pop()
print("conjunto4:", conjunto4)
"""El método pop elimina el primer elemento del set, y el método claer() elimina todos los elementos del set"""

print("Intersección de los conjuntos 4 y 5:", conjunto4.intersection(conjunto5))

print("la diferencia entre los conjuntos 1 y 3 es:", conjunto1.difference(conjunto3))


"""conjunto a partir de un generador"""
conjunto6 = {a*3 for a in range(10)}
print('el conjunto 6 es:', conjunto6)


