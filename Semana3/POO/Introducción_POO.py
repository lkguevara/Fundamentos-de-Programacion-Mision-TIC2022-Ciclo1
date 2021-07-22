#PROGRAMACIÓN ORIENTADA A 0BJETOS (POO)

"""Para entender en qué se basa este paradigma (modelo de solución de problemas), en lugar de empezar con teoría os propongo jugar un poco con dos códigos distintos. Ambos implementan una estructura de clientes y funciones para trabajar con ellos, pero uno está creado con programación estructurada (la clásica cuyas bases hemos estudiado hasta ahora) y la otra con programación orientada a objetos.
Lo único que tenéis que hacer es probar ambos códigos (sin necesidad de analizarlos), luego sacad vuestras propias conclusiones sobre cuál os parece más útil e intuitivo de aplicar y extender en el mundo real."""

#Atributos:
"""marca : 'String', color : 'String', cilindraje : 'Int',  modelo : 'Int' """

#Métodos o funciones:
"""acelarar, frenar, pinchar, apagar, encerder"""

#Instancias: self

class Moto: #indica que la clase no tiene atributos ni métodos y ya se puede utilizar
    pass    

class Moto:
    def __init__(self): #Función constructora Es la primera que se ejecuta cuando se crea un onjero de dicha clase
        self.marca = 'Auteco'
        self.color = 'Gris'
        self.cilindraje = 180
        self.modelo = 2021

#objeto: Instancia de una clase
moto1 = Moto()                      
print(moto1.marca)
print(moto1.color)
print(moto1.cilindraje)
print(moto1.modelo)

#***************************************************************************************************************

class Libro:  #Identificador de la clase
    def __init__(self, titulo, autor, costo) -> None:
        self.titulo = titulo #Constructor
        self.autor = autor
        self.costo = costo

    def mostrar(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Precio: {self.costo}'
"""
libro1 = Libro('Juegos del hambre','Suzanne Collins', 60000 )  ###Son los objetos
libro2 = Libro('cien años de soledad','Gabriel García Marquez', 35000 )
print(libro1.mostrar())
print(libro2.mostrar())"""


class Sala():
    def __init__(self, nombre, capacidad) -> None:
        self.nombre= nombre
        self.capacidad= capacidad
        self.books= []

#Creando un libro a la lista
    def add_book(self, titulo, autor, costo):
        libro = Libro(titulo,autor,costo)
        self.books.append(libro)

    def mostrar(self):
        return f'Nombre: {self.nombre}, capacidad: {self.capacidad}'

"""sala_novelas = Sala('Novelas', 10)
sala_novelas.add_book('La Paloma', 'Patrick', 45000)
sala_novelas.add_book('La maquina del tiempo', 'HG wells', 35000)"""

class Biblioteca():
    def __init__(self, nombre) -> None:
        self.nombre=nombre
        self.rooms = []

    def add_room(self, nombre, capacidad):
        sala=Sala(nombre, capacidad)
        self.rooms.append(sala)

objeto_biblioteca= Biblioteca('Soledad Rengifo')

objeto_biblioteca.add_room('Bellas Artes', 50)
objeto_biblioteca.add_room('Novelas', 50)

objeto_biblioteca.rooms[0].add_book('La Paloma', 'Patrick', 45000)
objeto_biblioteca.rooms[1].add_book('La maquina del tiempo', 'HG wells', 35000)

print(objeto_biblioteca.rooms[0].mostrar())
print(objeto_biblioteca.rooms[1].mostrar())
print(objeto_biblioteca.rooms[1].books[0].mostrar())


    
#*******************************************************************************EJEMPLOS****************************************
"""#1. El usuario va a crear su inventario de motos:

class Moto:
    def __init__(self,marca, color, cilindraje, modelo):
        self.marca = marca
        self.color = color
        self.cilindraje = cilindraje
        self.modelo = modelo

marca = input("Digite la marca de la moto: ")
color = input("Digite el color de la moto: ")
cilindraje = int(input("Digite el cilindraje de la moto: "))
modelo = int(input("Digite el modelo de la moto: "))
moto1 = Moto(marca, color, cilindraje, modelo)
print(f'La moto es de una marca {moto1.marca} color {moto1.color}, modelo {moto1.modelo} y cilindraje {moto1.cilindraje}')"""

#2. Realizar un programa que almacene los contactos telefonicos: nombre, fecha_nac, telefono e email:
"""class Agendamiento:
    def __init__(self,nombre, fechaNac, telefono, email):
        self.nombre = nombre            #atributos, características, propiedades
        self.fechaNac = fechaNac
        self.telefono = telefono
        self.email = email

    def mostrar_datos(self):            #funciones ó métodos
        print(f'nombre: {self.nombre}, fecha Nacimiento: {self.fechaNac}, telefono: {self.telefono}, email: {self.email}')

agenda = []
while(True):
    nombre = input("Digite el nombre del contacto")
    fechaNac = input("Digite la fechad de nacimiento")
    telefono = input("Digite el telefono")
    email = input("Digite el correo electrónico")
    contacto = Agendamiento(nombre, fechaNac, telefono, email)
    contacto.mostrar_datos()
    agenda.append(contacto)
    opcion = input("Desea adicionar otro contacto? s / n")
    if opcion == 'n':
        print("Hasta la vista")
        break
    for item in agenda:
        print(item.mostrar_datos())"""















