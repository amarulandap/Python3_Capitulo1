"""Como definir una variable tipo String o cadena"""
import string

cadena = 'Primera cadena de caracteres'
cadena1 = "segunda cadena de caracteres"
cadena2 = "TERCERA CADENA DE CARACTERES"
entero = 1
entero1 = 2

"""Como darle formato a una cadena"""

print(cadena, cadena1)
print("la suma de " + str(entero) + " + " + str(entero1) + " es igual a " + str(entero + entero1))

print("¿Tú te inspiras en %s?" % "C")
print("Tú cumples años el día %s %s y lo celebras siempre con %s y %s" % ("7", "de Mayo", "familia", "amigos"))

print("Tú cumples años el %(dia)s de %(mes)s y los festejas con %(persona1)s y con %(persona2)s" % {"dia" : "7",
                                                                                                    "mes" : "Mayo",
                                                                                                    "persona1" : "familia",
                                                                                                    "persona2" : "amigos"})

mes1 = "Enero"
mes2 = "Diciembre"
print("Las personas mas importantes para ti son: {} y {}".format("madre", "padre"))
print("el primer mes del año es {1}, y el último mes del año es {0}".format(mes2, mes1))


"""Noción de tamaño de letra"""

cadena2_minuscula = cadena2.lower()
print(cadena2_minuscula)
cadena_mayuscula = cadena.upper()
print(cadena_mayuscula)
"""El método capitalize me convierte a mayúscula la letra inicial de la cadena de caracteres"""
cadena1_capitalize = cadena1.capitalize()
print(cadena1_capitalize)
"""El método title me convierte a mayúscula la letra inicial de cada palabra de la cadena"""
cadena1_title = cadena1.title()
print(cadena1_title)
"""El método swapcase hace lo mismo que upper, convierte todo el string a letras mayusculas"""
cadena1_swapcase = cadena1.swapcase()
print(cadena1_swapcase)


"""Noción de longitud"""

longitud_cadena = len(cadena)
print("La primera cadena de caracteres tiene una longitud de: ", longitud_cadena, "caracteres")


"""Noción de pertenencia"""

cadena3 = "Los días de la semana son 7: Lunes, Martes, Miercoles, Jueves, Viernes, Sabado y Domingo"
fragmento = "lunes" in cadena3
print("Fragmento es:", fragmento)


"""Noción de ocurrencia"""

"""El método count se usa para determinar cuantas veces se repite un caracter o combinación de caracteres en una cadena"""
a = cadena1.count('a')
print('a: ', a)

es = cadena3.count('es')
print("es: ", es)

lunes = cadena3.count('Lunes')
print("Lunes: ", lunes)

"""También es posible determinar la primera posición de ocurrencia de el caracter o combinación de caracteres"""
posicion = cadena.index("d")
posicion2 = cadena.index("d", posicion + 1)
print("la letra {} se encuentra en las posiciones".format("d"), posicion, "y", posicion2)

fragmento1 = cadena3.find("Martes")
print("Fragmento1 es:", fragmento1)


"""Método para reemplazar caracteres"""
reemplazo = cadena1.replace("segunda", "SEGUNDA")
print("\nEsta es la cadena de reemplazo:", reemplazo)
reemplazo1 = cadena1.replace("segunda", "2da")
print("\tEste es el segundo reemplazo:", reemplazo1)


"""Noción de carácter"""
print([chr(x) for x in range(191, 564)])

"""Saber que carácter tiene una cadena en una determinada posición"""
print("La cadena2 tiene en la posición 2 el carácter:", cadena2[2])


"""Módulo String me permite conocer los tipos de caracteres que maneja python. \n es para generar un salto de linea,
    \t es para tabular a la derecha"""
print("\n", string.ascii_letters)
print("\t", string.ascii_lowercase)
print("\r", string.ascii_uppercase)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)

print(string.punctuation)
print(string.whitespace)

"""Secuenciar o dividir cadenas de caracteres"""
cadena4 = "Esta es la cadena para prácticar la división de cadenas"

lista_cadena4 = list(cadena4)
print(lista_cadena4)

secuencia = cadena4.split()
print(secuencia)

print(" ".join(secuencia))
























