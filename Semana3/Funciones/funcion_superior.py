"""Son funciones que reciben como parametro otras funciones"""

def saludar(function):
    print(function())

def hola():
    return "hola"

def mundo():
    return "mundo"

saludar(hola)
saludar(mundo)


# ************************

def saludar(function, function2):
    print(function(), function2())

def hola():
    return "hola"

def mundo():
    return "mundo"

saludar(hola, mundo)
