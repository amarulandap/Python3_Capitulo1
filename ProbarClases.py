"""Probaremos las clases creadas en la introducción"""

"""Tenemos que importar la clase o clases que vamos a utilizar"""
from IntroduccionClases import Punto
from IntroduccionALaHerencia import Punto2D


"""Instanciamos un objeto de la clase Punto"""
coordenada = Punto(10, 20, 30)
coordenada2D = Punto2D(2, 4)


"""Invocar el método mostrar usando la notación punto"""
coordenada.mostrarEnPantalla()
coordenada2D.mostrarEnPantalla()


"""Calcular la distancia al origen"""
modulo = coordenada.distanciaRespectoAlOrigen()
modulo1 = coordenada2D.distanciaRespectoAlOrigen()
print("\nLa distancia respecto al origen es:", modulo)
print("La distancia al origen del punto 2D es: ", modulo1)


"""Calcular la distancia entre dos puntos"""
coordenada1 = Punto(5, 10, 15)
coordenada1_2D = Punto2D(6, 8)
distanciaPuntos = coordenada.distanciaEntrePuntos(coordenada1)
distanciaPuntos2D = coordenada1_2D.distanciaEntrePuntos(coordenada2D)
print("\nLa distancia entre los dos puntos es:", distanciaPuntos)
print("La distancia entre puntos 2D es: ", distanciaPuntos2D)


"""Operador add"""
print("\nOperador add:")
coordenada2 = coordenada.__add__(coordenada1)
coordenada2.mostrarEnPantalla()
coordenada2_2D = coordenada2D.__add__(coordenada1_2D)
coordenada2_2D.mostrarEnPantalla()


"""Operador sub"""
print("\nOperador sub:")
coordenada3 = coordenada.__sub__(coordenada1)
coordenada3.mostrarEnPantalla()
coordenada3_2D = coordenada2D.__sub__(coordenada1_2D)
coordenada3_2D.mostrarEnPantalla()


"""Operador mul"""
print("\nOperador mul:")
coordenada4 = coordenada3.__mul__(5)
coordenada4.mostrarEnPantalla()
coordenada4_2D = coordenada3_2D.__mul__(-5)
coordenada4_2D.mostrarEnPantalla()


"""Operador iaddd"""
print("\nOperador iadd:")
coordenada.__iadd__(coordenada1).mostrarEnPantalla()


"""Operador isub"""
print("\nOperador isub:")
coordenada4.__isub__(coordenada3).mostrarEnPantalla()








