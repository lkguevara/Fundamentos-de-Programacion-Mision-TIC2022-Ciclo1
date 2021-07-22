"""Se genera un entero entre 15 y 30 el cual será el tamaño del vector; luego se construye un objeto de la clase vector. Luego, se llena el vector con números enteros entre 1 y 99999 generados aleatoriamente.

Con el vector creado se suman los datos que sean números
capicúa (se lee igual de derecha a izquierda o izquierda a derecha) o que comiencen con dígito par.
Recuerde que un número es capicúa, es aquel que se lee igual
de izquierda a derecha que de derecha a izquierda, por ejemplo, el 32523.

Ejemplo:
Vector 154, 6412, 74595, 77877, 4862, 96325. Note que los
números que comienzan por un dígito par son 6412, 4862 y es capicúa el número 77877 porlo tanto estos son los números a sumar. 
Suma = 6412 + 77877 + 4862 = 89151"""

import random
import math

"""Función para inventir el número"""
def invierteNumero(n):
    nunu =0
    m=n
    while m>0:
        digito=m%10
        nunu=nunu*10+digito
        m=m//10
    return nunu


"""Función que retorna el primer digito de un número x"""

def comienzaCon(x):
    pd=x
    while pd > 9:
        pd=pd//10
    return pd

n=random.randint(15,30)
v=[0]*n
print(f'El tamaño del vector es {n}')

for i in range(n):
    v[i]=random.randint(1,99999)
print(f'El vector ya llenado es :\n {v}')

suma=0


for i in range(n):
    nunu = invierteNumero(v[i])
    if v[i] == nunu or comienzaCon(v[i] % 2 == 0):
        suma +=v[i]
        # print(v[i])  
    
       
print(f'El vector inicial es:\n {v}')
print(f'La suma de los números capicúa o pares es: \n {suma}')







