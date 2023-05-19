"""Crearemos una subclase que herede de la clase madre Punto"""
from IntroduccionClases import Punto

class Punto2D(Punto):
    """Representar un punto en el plano cartesiano"""

    def __init__(self, x, y):
        """Método para inicializar un punto en el plano, invocando el método constructor de la clase madre"""

        super().__init__(x, y, 0)



    def mostrarEnPantalla(self):
        """Método para imprimir el punto en pantalla"""

        print("Punto ({}, {})".format(self.x, self.y))





