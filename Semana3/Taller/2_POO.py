#Ejercicio 7 Taller POO

class Peluchito:
    def __init__(self, nombre, cantidad, valor):
        self.nombre = nombre
        self.cantidad = cantidad
        self.valor = valor

    def mostrar_peluchito(self):
        print(f'Peluche: {self.nombre}, Cantidad: {self.cantidad}, Valor: {self.valor}')

def imprimirMenu():
    opcion = int(input("1.Agregar Peluche\n2.Buscar Peluche\n3.Eliminar Peluche\n4. Mostrar Inventario\n5. Realizar Venta\n6.Mostar Ganancia\n7.Salir"))
    return opcion

inventario = []
while(True):
    opcion = imprimirMenu()
    if opcion == 1:
        nombre = input("Digite el nombre del peluche: ")
        cantidad = int(input("Digite la cantidad de ese peluche: "))
        valor = int(input("Digite el valor de ese peluche: "))
        peluche = Peluchito(nombre=nombre, cantidad=cantidad, valor=valor)
        inventario.append(peluche)
    elif opcion == 2:
        nombreABuscar = input("Digite el nombre del peluche a buscar: ")
        existeElPeluche = False
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                peluche.mostrar_peluchito()
                existeElPeluche = True
        if existeElPeluche == False:
            print("El peluche no existe")
    elif opcion == 3:
        nombreABuscar = input("Digite el nombre del peluche a eliminar: ")
        existeElPeluche = False
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                confirmacion = input(F'Confirma que desea eliminar el peluche {peluche.nombre} s / n')
                if confirmacion == 's':
                    inventario.remove(peluche)
                existeElPeluche = True
        if existeElPeluche == False:
            print("El peluche no existe")
    elif opcion == 4:
        for peluche in inventario:
            peluche.mostrar_peluchito()
    elif opcion == 7:
        print("Hasta la vista Baby")
        break
    else:
        print("Opción Invalida")