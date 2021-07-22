#JSON

"""Notación de objeto de JavaScript (JavaScript Object Notation), es una sintaxis para almacenar e intercambiar datos"""

"""json.dump------> guardar un nuevo archivo de diccionario a json"""
"""json.dumps------> convierte un string"""
"""json.load------> pasar de json a diccionario"""
"""json.loads------> lee un string"""


import json

#Escritura de datos en JSON

#Ejemplo 1: Leer un diccionario y guardar en .json

Mi_dicionario= {
    "Programador":"Gabriel", 
    "Lenguaje":"Python",
    "Idioma":"Español",
    "Numeros_favoritos":[1,3,5]} #Diccionario, ---los nombres son como están en el json y esta información la brinda el backend--///

###Guardando el archivo Mi_dicionario en .json

with open("Mi_primer_JSON.json","w") as jsonFile:  #("nombre_archivo",tipo(write "w",read "r")) as "nombre_nuevo_archivo"
    json.dump(Mi_dicionario,jsonFile) #Con el dump almacena en el archivo f el diccionario a.
    jsonFile.close


#Ejemplo 2: Leer un diccionario y guardar en .json

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre":nombre, "empleo":empleo, "email":email})

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)


#Lectura de datos en JSON

with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])


#Ejemplo 3: Leer un archivo .json y pasarlo a diccionario
import json

with open("E:\Cursos\LIAN\Cursos\Progress\Programación\MINTIC\Fundamentos_programación\Semana7\Json\mi_SegundoJSON.json") as jsonFile:
    diccionarioProductos = json.load(jsonFile)
    jsonFile.close()

print(diccionarioProductos)