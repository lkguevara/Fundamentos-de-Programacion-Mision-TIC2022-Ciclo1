# PILAS
"""Son colecciones de elementos ordenados que únicamente permiten dos acciones:

1. Añadir un elemento a la pila.
2. Sacar un elemento de la pila.
3. La peculiaridad es que el último elemento en entrar es el primero en salir. 

En inglés se conocen como estructuras LIFO (Last In First Out). Las podemos crear como listas normales y añadir elementos al final con el append():
"""
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

"""[3, 4, 5, 6, 7]"""

#Método pop()
"""Para sacar los elementos utilizaremos el método pop(). Al utilizareste método devolveremos el último elemento, pero también lo borraremos:"""

print(pila.pop())
print(pila)

# *********************************************************************************

def funcion1():
    print("ingreso por el método 1")
    x=5+funcion2()  #L2
    return x

def funcion2():
    print("ingreso por el método 2")
    x=3+funcion3() #L3
    return x


def funcion3():
    print("ingreso por el método 3")
    x=7
    return x

x=funcion1() #L1
print(x)

"""Los datos procesados aplican en orden inverso, 7+3+10=15"""

"""MÉTODOS"""


#6. ESLLENA: retorna verdadero si la pila está llena, falso de lo contrario.

stack=[] #1. Init: crea una pila vacía.

stack.append("a") 
stack.append("e")  #2. APILAR: agrega un elemento a pila.
stack.append("i")
print(stack)

stack.pop()#3. DESAPILAR: elimina el último elemento de la pila y deja una nueva pila la cual queda con un elemento menos.
print(stack)

###Clase Pila ---> POO

class Pila:
    def __init__(self):
        self.arreglo=[] #Init

    def apilar(self,x):
        self.arreglo.append(x) #Apliar

    def desapilar(self):
        self.arreglo.pop() #Desapilar (Se realiza únicamente al último, no se puede colocar posición)

    def imprimirPila(self):
        for i in self.arreglo: 
            print(i,end=",")
        print()

    def estaVacia(self):
        return len(self.arreglo) == 0 #EsVacia

    def esLlena(self):
        return len(self.arreglo) != 0 #Esllena
        

p=Pila()
print(p.estaVacia())
print(p.esLlena())
p.apilar(4)
p.imprimirPila()
p.apilar(5)
p.imprimirPila()
p.desapilar()
p.imprimirPila()
print(p.estaVacia())
print(p.esLlena())

"""PILAS USANDO LA CLASE DE LISTAS ENLAZADAS"""
 
class nodoSimple:
    def __init__(self, d = None):
        self.dato = d
        self.liga = None        #puntero o conector al siguiente nodo
    def asignarDato(self, d):           #setters y getters
        self.dato = d
    def asignarLiga(self, x):
        self.liga = x
    def retornarDato(self):
        return self.dato
    def retornarLiga(self):
        return self.liga

#Clase LSL
class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None

    def insertar (self, d, y=None): #cambio
        x = nodoSimple(d) #cambio
        self.conectar(x, y)

    def conectar (self, x, y):
        if y == None:
            if self.primero == None:
                self.ultimo = x
            else:
                x.asignarLiga(self.primero)
            self.primero = x
            return
        x.asignarLiga(y.retornarLiga())
        y.asignarLiga(x)
        if y == self.ultimo:
            self.ultimo = x

    def primerNodo (self):
        return self.primero

    def finDeRecorrido (self, p):
        return p == None

    def esVacia (self):
        return self.primero == None

    def recorrerLista (self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end = ", ")
            p = p.retornarLiga()

    def borrar (self, x, y = None):
        if x == None:
            print("Dato no está en la lista")
            return
        if y == None:
            if x != self.primero:
                print("Falta el anterior del dato a borrar")
                return
        else:
            y = y.retornarDato()
        self.desconectar(x,y)

    def desconectar(self, x, y):
        if y == None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y

#init: Inicializar una pila nueva y vacia
#apilar: Agrega un elemento a la pila
#desapilar: Elimina el tope de la pila y lo devuelve (El elemento que se devuelve siempre es el último que se agrego)
#imprimirPila: Recorre la pila y muestra los datos
#estaVacia: Devuelve True o False según la pila este vacía o este llena

class PilaLSL(LSL):

    def __init__(self):         #init
        LSL.__init__(self)

    def apilar(self,d):         #apilar
        self.insertar(d)

    def imprimirPila(self):     #imprimir
        self.recorrerLista()

    def desapilar(self):
        p = self.primerNodo()
        d = p.retornarDato()
        self.borrar(p)
        return d

a = PilaLSL()
a.apilar('a')
a.apilar('e')
a.apilar('i')
a.recorrerLista()
a.desapilar()
a.recorrerLista()

#Crear un programa que muestre un menú donde el usuario pueda seleccionar entre:
#1. Apilar
#2. Desapilar
#3. Imprimir el contenido de la pila
#0. Salir

