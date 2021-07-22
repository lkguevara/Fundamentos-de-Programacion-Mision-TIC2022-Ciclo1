"""Elaborar un programa que permita: 
a. Guardar los datos de la lista
b. Mostrar los datos de la lista
c. Realizar modificaciones a través de un menú"""

from os import remove, system


devs = [] #1. Se crea la lista vacia

def create_dev():  #5. Funcion para agregar el desarrollador a la lista y luego verlos
    dev={"cedula":"","nombre":"","salario":""}
    dev["nombre"]=input("Digite el nombre del desarrollador : ")
    dev["cedula"]=validate_input("Digite la cedula del desarrollador")
    dev["salario"]=validate_input("Digite el salario del desarrollador")
    devs.append(dev)
    print(devs)

def list_devs(): #8. Funcion para listar los devs
    for dev in devs:
        print(f'nombre: {dev["nombre"]}, cedula: {dev["cedula"]}, salario: {dev["salario"]}')


def search_devs(): # Funcion para buscar por cédula
    idBuscar= int(input("digita el número de cédula a buscar: "))
    for dev in devs:
        if idBuscar == dev["cedula"]:
            print(f'nombre: {dev["nombre"]}, cedula: {dev["cedula"]}, salario: {dev["salario"]}')      

def search_devs_hight_salary():
    for dev in devs:
        if dev["salario"]>3000000:
            print(f'nombre: {dev["nombre"]}, cedula: {dev["cedula"]}, salario: {dev["salario"]}')

def validate_input(text_validate):
    while True:
        dicty = input("Digite " + text_validate + ":")
        try:
            dicty = int(dicty)
            return dicty
        except ValueError:
            print("Error: Debe digitar un número")

def delete_Dev():
    idBuscar= int(input("digita el número de cédula a buscar: "))
    for dev in devs:
        if idBuscar == dev["cedula"]:
            devs.remove(dev)



def menu(option):   #4. Menu de selección
    if option == "1":
        create_dev()
        run() #6. Vuelve al menú principal y el ciclo no va a finalizar a menos que el usuario lo quiera
    elif option == "2": 
        list_devs()
        run()
    elif option == "3": 
        search_devs()
        run()
    elif option == "4": 
        search_devs_hight_salary()
        run()
    elif option == "5": 
        delete_Dev()
        run()
    elif option == "8": 
        system("cls")
        run()
    else:
        exit()


def run(): #3. Correr el entry point
    print("""
    Escoge una opción:
    1. Agregar desarrollador.
    2. Listar desarrolladores
    3. Buscar un desarrollador con cédula
    4. Desarrolladores con salario alto
    5. Eliminar un desarrollador con su número de cédula
    8. Limpiar pantalla
    9. Salir
    """)
    menu(input("Digita la opción: "))


if __name__ == '__main__':  #2. Entry point
    run()

