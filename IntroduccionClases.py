"""Introducción a las clases en Python"""
import math

class Punto:
    """Representar un punto en el espacio"""

    """En Python no es obligatorio declarar desde un principio todos los atributos de la clase"""
    """A través de la notación punto puedo darle valores a los atributos"""

    def __init__(self, x, y, z):
        """Método para la inicialización del punto en el espacio, método constructor"""

        self.x = x
        self.y = y
        self.z = z

    def mostrarEnPantalla(self):
        """Muestra el punto en pantalla"""

        print("Punto ({}, {}, {})".format(self.x, self.y, self.z))


    def distanciaRespectoAlOrigen(self):
        """La distancia respecto al origen es igual a la raíz cuadrada de la suma de los cuadrados de las coordenadas"""

        modulo = math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

        return modulo


    def distanciaEntrePuntos(self, other):
        """la distancia entre dos puntos"""

        distancia = math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2))

        return distancia


    def __add__(self, other):
        """Operador suma para los atributos de los objetos de la clase"""

        return Punto(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        """Operador diferencia para los atributos de los objetos"""

        return Punto(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, escalar):
        """Operador producto por un escalar"""

        return Punto(self.x * escalar, self.y * escalar, self.z * escalar)


    def __iadd__(self, other):
        """Modificar la instancia en curso sin crear una nueva"""

        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self


    def __isub__(self, other):

        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

        return self
