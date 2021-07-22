#1. MAP()

"""Map es una función que trabaja con datos de una lista, EL MAP regresará una nueva lista.
Esta función trabaja de una forma muy similar a filter(), con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map"""

#Ejemplo:

def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

map(doblar, numeros)

#----<map at 0x212eb6e0748>----- #Retorna una dirección en memoria
print(numeros)
print(list(map(doblar, numeros))) #Transformando el map en una lista:

#Y se puede simplificar con una función **lambda** para substituir la llamada de una función definida:

print(list( map(lambda x: x*2, numeros)))

"""La función map() se utiliza mucho junto a expresiones lambda ya que permite ahorrarnos el esfuerzo de crear bucles for. Además se puede utilizar sobre más de un iterable con la condición que tengan la misma longitud."""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(list( map(lambda x,y : x*y, a,b) ))

"""[6, 14, 24, 36, 50]"""


# *****************************************************************MINTIC*********************************************************************
#Generar los números del 1 al 50

numeros=[numeros for numeros in range(1,51)]
print(numeros)

"""[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]"""

dobles= list(map(lambda numero:numero*2, numeros )) #Aqui me guardará el map, el map regresa un map object
print(dobles)

"""[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]"""

#Sumar un año más de experiencia al desarrollador

devs=[
    {"cc":123, "Nombre":"Juan", "salario":25, "years":5},
    {"cc":456, "Nombre":"armando", "salario":26, "years":7},
    {"cc":789, "Nombre":"Ricardo", "salario":27, "years":1},
    {"cc":101, "Nombre":"Roberto", "salario":28, "years":9},
    {"cc":1213, "Nombre":"Lian", "salario":29, "years":2},
    {"cc":1415, "Nombre":"Esmeralda", "salario":30, "years":15}]
#Solución 1

names= list(map(lambda dev: {"cc":dev["cc"], "Nombre":dev["Nombre"],"salario":dev["salario"],"years":dev["years"]+1}, devs )) 
print(names)

"""[{'cc': 123, 'Nombre': 'Juan', 'salario': 25, 'years': 6}, {'cc': 456, 'Nombre': 'armando', 'salario': 26, 'years': 8}, {'cc': 789, 'Nombre': 'Ricardo', 'salario': 27, 'years': 2}, {'cc': 101, 'Nombre': 'Roberto', 'salario': 28, 'years': 10}, {'cc': 1213, 'Nombre': 'Lian', 'salario': 29, 'years': 3}, {'cc': 1415, 'Nombre': 'Esmeralda', 'salario': 30, 'years': 16}]"""

#Solución 2

def add_year(dev):
    dev["years"]+=1
    return dev

nombres= list(map(lambda dev: dev["Nombre"],devs ))
all_devs = list(map(add_year, devs))
print(all_devs)

"""[{'cc': 123, 'Nombre': 'Juan', 'salario': 25, 'years': 6}, {'cc': 456, 'Nombre': 'armando', 'salario': 26, 'years': 8}, {'cc': 789, 'Nombre': 'Ricardo', 'salario': 27, 'years': 2}, {'cc': 101, 'Nombre': 'Roberto', 'salario': 28, 'years': 10}, {'cc': 1213, 'Nombre': 'Lian', 'salario': 29, 'years': 3}, {'cc': 1415, 'Nombre': 'Esmeralda', 'salario': 30, 'years': 16}]"""

#*********************************************************************************************

#2. FILTER()

"""Tal como su nombre indica filter significa filtrar, ya que a partir de una lista o iterador y una función condicional, es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición."""

#Ejemplo: Encontrar los números impares de la siguiente lista:

numeros=[numeros for numeros in range(1,101)]

impares=list(filter(lambda numero: numero %2 == 1, numeros))
print(impares)

"""[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]"""

#2. Se tiene una lista con varios números. Se desea filtrar y seleccionar únicamente con los múltiples de 5.

numeros=[numeros for numeros in range(1,101)]

multiplos=list(filter(lambda numero: numero %5==0, numeros))
print(multiplos)

#FILTRANDO OBJETOS

"""Sin embargo, más allá de filtrar listas con valores simples, el verdadero potencial de filter() sale a relucir cuando necesitamos filtrar varios objetos de una lista."""

#3. e tiene una lista con varias personas, Se desea filtrar y seleccionar únicamente las que son menores de edad:

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)


"""Marta de 16 años
Eduardo de 12 años"""