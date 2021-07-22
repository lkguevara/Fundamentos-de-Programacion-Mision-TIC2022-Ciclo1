# from _typeshed import Self


class Libro:  #Identificador de la clase
    def __init__(self, titulo, autor, costo) -> None:
        self.titulo = titulo #Constructor
        self.autor = autor
        self.costo = costo

    def show(self):
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

    def show(self):
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

    def show_rooms(self):
        format_rooms = [room.show() for room in self.rooms]
        return format_rooms 

"""objeto_biblioteca= Biblioteca('Soledad Rengifo')

objeto_biblioteca.add_room('Bellas Artes', 50)
objeto_biblioteca.add_room('Novelas', 50)

objeto_biblioteca.rooms[0].add_book('La Paloma', 'Patrick', 45000)
objeto_biblioteca.rooms[1].add_book('La maquina del tiempo', 'HG wells', 35000)

print(objeto_biblioteca.rooms[0].mostrar())
print(objeto_biblioteca.rooms[1].mostrar())
print(objeto_biblioteca.rooms[1].books[0].mostrar())"""