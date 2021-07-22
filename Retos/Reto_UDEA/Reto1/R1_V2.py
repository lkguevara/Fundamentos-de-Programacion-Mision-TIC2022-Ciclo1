"""Se genera un entero entre 15 y 30 el cual será el tamaño del vector; luego se construye un objeto de la clase vector. Luego, se llena el vector con números enteros entre 1 y 99999 generados aleatoriamente.


Posteriormente se crea una variable suma, inicializada en cero, donde vamos a guardar la suma de los datos del vector que sean primos o que comiencen con dígito impar.

Ejemplo:
vector original = 30, 23, 19, 18, 7, 21, 31, 12, 41, 9
Los números que se suman son 30, 23, 19, 18, 7, 31, 12, 41, 9; por lo tanto la suma es 190"""

import random
import math


def esPrimo(n): #Un número primo es un número que SOLO es divisible por él mismo y el 1
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

def comienza_digito_impar(n):
    d = str(n)[0]
    d = int(d)
    if d%2!=0:
        return True
    else:
        return False


n= random.randint(15,30)
v=[0]*n
print(f'El tamaño del vector es {n}')

for i in range(n):
    v[i]=random.randint(1,99999)
print(f"El vector llenado es {v}")


suma=0
for i in range(n):
    if v[i] == esPrimo(v[i]) or comienza_digito_impar(v[i]):
        suma+=v[i]
    print(v[i])


print(f'El vector inicial es:\n {v}')
print(f'La suma de los números capicúa o pares es: \n {suma}')
