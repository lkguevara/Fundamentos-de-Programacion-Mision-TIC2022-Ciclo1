class animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def sonido(self):
        return "error - las suclases son las que tienen sonido"

    
    def imprimirSonido(self):
        self.sonido()

class Gato(animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "miau miua"


class perro(animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "guau guau"

gato1= Gato("jocker")
perro1= perro("Bambu")


print(gato1.sonido())
print(perro1.sonido())