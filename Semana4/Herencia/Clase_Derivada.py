class persona:
    def __init__(self, nombre, edad, telefono): #padre
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

class Empleado: 
    def __init__(self,nombre, edad, telefono, salario, empresa): #Hijo
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.salario = salario
        self.empresa = empresa



#Convirtiendo a herencia, La clase hija deberá llamar al constructor de la clase padre, lo anterior con super().

class Empleado (persona): 
    def __init__(self, nombre, edad, telefono, salario, empresa): #Hijo
        super().__init__(nombre, edad, telefono)
        self.salario = salario
        self.empresa = empresa
    
    def imprimirdatos(self):
        print(f'salario: {self.salario}, compañia: {self.empresa}')

empleado1 = Empleado ("james", 58, 311412, 5000000, "prigma")
empleado1.imprimirdatos()

# Ejemplos

# 1. Definir una clase padre llamado vehiculo y dos clases llamadas carro y bicicleta

class vehiculo:
    def __init__(self, color, ruedas):
        self.color=color 
        self.ruedas=ruedas

class coche(vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas) 
        self.velocidad=velocidad

    def imprimircoche(self):
        print(f'color: {self.color}, ruedas: {self.ruedas}, velocidad: {self.velocidad}, ')

class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas) 
        self.tipo=tipo

    def imprimirbici(self):
        print(f'color: {self.color}, ruedas: {self.ruedas}, tipo: {self.tipo}, ')

coche1 =coche("rojo", 4, 1200)
coche1.imprimircoche()

bicicleta1 =bicicleta("verde", 2, "scooter")
bicicleta1.imprimirbici()


# 2. Inventario supermercado

class producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre= nombre
        self.precio= precio
        self.cantidad= cantidad
        

    def __str__(self):
        return "Nombre: " + self.nombre + ", Precio: " + str(self.precio) + ", Cantidad: " + str(self.cantidad)


class Lacteos(producto):
    def __init__(self, nombre, precio, cantidad, volumen, tipo,presentacion):
        super().__init__(nombre, precio, cantidad)
        self.volumen= volumen
        self.tipo= tipo
        self.presentacion= presentacion

    def __str__(self):
        return super().__str__() + ", Volumen: " + str(self.volumen) + ", tipo: " + self.tipo + ", presentacion: " + self.presentacion

def imprimirMenu():
    option = int(input("1. Agregar Producto\n2. Buscar Producto\n3. Eliminar Producto\n4. Actualizar Producto\n5. Mostrar inventario\n6. Salir"))
    return option


lacteosList = []
detergentesList = []
licoresList = []

while (True):
    option = imprimirMenu()
    if option == 1:
        tipo = int(input("Seleccione el tipo de producto:\n1. Lacteo\n2. Detergente\n3. Licores"))
        if tipo == 1:  #Lacteo
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))
            volumen = int(input("Digite el volumen"))
            tipo = input("Digite el tipo")
            presentacion = input("Digite la presentación")
            lacteo = Lacteos(nombre, precio, cantidad, volumen, tipo, presentacion)
            lacteosList.append(lacteo)

        elif tipo ==2:
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))

        elif tipo ==3: 
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))

    elif option == 5:
        print("-------------Lacteos--------")
        for lacteo in lacteosList:
            print(lacteo.__str__())
        print("-------------Detergentes--------")

        print("-------------Licores-------------")
    elif option == 6:
        print("Gracias totales")
        break
    else:
        print("Opción invalida")

       

class detergente(producto):
    def __init__(self, nombre, precio, cantidad, fechaVencimiento, tipoUso, presentacion):
        super().__init__(nombre, precio, cantidad, fechaVencimiento)
        self.tipoUso= tipoUso
        self.presentacion= presentacion

    def imprimirdetergente(self):
        print(f'nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}, fechaVencimiento: {self.fechaVencimiento}, tipoUso: {self.tipoUso}, presentacion: {self.presentacion},')

class licores(producto):
    def __init__(self, nombre, precio, cantidad, fechaVencimiento, tipo, origen, porcentajeAlcohol):
        super().__init__(nombre, precio, cantidad, fechaVencimiento)
        self.tipo= tipo
        self.origen= origen
        self.porcentajeAlcohol= porcentajeAlcohol

    def imprimirdetergente(self):
        print(f'nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}, fechaVencimiento: {self.fechaVencimiento}, tipo: {self.tipo}, origen: {self.origen},porcentajeAlcohol: {self.porcentajeAlcohol},')

