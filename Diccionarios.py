"""Como crear un diccionario"""
diccionario = { "clave1" : "valor1",
                "clave2" : "valor2",
                "clave3" : "valor3"}

agenda = { "andres" : "3006183625",
           "carolina" : "3012547896",
           "cristina" : "3205897468",
           "maria" : "3215487962"}
print("Diccionario original: ",agenda)

print("El número celular de andres es: ",agenda["andres"])

agenda["sebastian"] = "3175862410"
print(agenda)

agenda["carolina"] = "3025874216"
print(agenda)


"""Como recorrer un diccionario"""
for clave, valor in diccionario.items():
    print("la combinación {}, {} del registro, nos indica que este contendor es un diccionario".format(clave, valor))

print("\n")
for nombre, telefono in agenda.items():
    print("Nombre: {} ; Telefono {}".format(nombre, telefono))

print("\n")
for nombre in sorted(agenda.keys()):
    print("Nombre: {} ; Telefono: {}".format(nombre, agenda[nombre]))

print("\n")
print("Nombres:", agenda.keys())
print("Telefonos:", agenda.values())


"""Comprobar la existencia de una clave"""
existe_clave = "juan" in agenda
print("La clave Juan existe en la agenda?", existe_clave)

print(agenda.get("andres", "la clave andres no existe"))
print(agenda.get("juan", "la clave juan no existe"))


"""Utilizar un generador para crear un diccionario"""
diccionario1 = {a:a ** 2 for a in range(10)}
print('el diccionario 1 es: ',diccionario1)


