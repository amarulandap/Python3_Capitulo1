"""Aserciones"""

for a in range(2):
    assert a % 2 == 1, 'Número impar'

"""Para capturar una exepción"""
def test(num):
    if num < 0:
        raise ValueError('El número es negativo')

    return num

try:
    num = test(-3)
except:
    num = 0

print(num)


"""
ok = False
>>> try:
... # instrucción de la que se quiere capturar las excepciones
... ok = True
... except:
... pass
...
>>> if ok:
... # segunda parte: otras instrucciones
...
"""

"""
Ejemplo para gestionar uan base de datos

try:
# establecimiento de conexión con una base de datos
except:
# se muestra un mensaje que pide verificar la conexión
else:
    try:
    # se envía una consulta
    except:
    # se muestra un mensaje con la consulta
    else:
    # se recupera el resultado en una variable
finally:
# se cierra la conexión a la base de datos
"""




