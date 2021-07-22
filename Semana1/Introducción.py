import math

#1. FUNCIÓN PRINT

"""Es una instrucción que nos permite mostrar correctamente el valor de una cadena (u otros valores/variables) por pantalla"""

print("Hola Python")
currentYear = 2021
PI = 3.1416
print("El año actual es:" + " " + str(currentYear), str(PI))
print(f'El año actual es {currentYear} y el valor de la constante es {PI}')


# *****************************************************************************************************************************************
#2. TIPOS DE DATOS

#a. Números
"""Números Enteros: Que no tienen una parte decimal y van desde menos infinito a más infinito ---> 5
   Números Florantes: Números que tienen una parte decimal escrita con un punto ---> 5.5 """

#b. Variables
"""Una variable es un identificador que representa un espacio en la memoria. A este espacio se le puede asignar un valor para utilizarlo posteriormente como si se tratase de un valor literal, incluso se puede operar con otras variables y reasignarle otro valor en cualquier momento."""

numero=3 #Variable llamada número y se le asigna el numero 3

#c. Cadenas de texto "String"

"""Siempre se definen entre comillas simples o dobles"""

Texto="Hola Mundo" #Variable llamada texto y se le asigna una cadena de texto "hola mundo"
Texto='Hola Mundo'

#d. Booleanos: True or False


# **************************************************************************************************************************************
#3. SLICING EN LAS CADENAS

"""El slicing es una capacidad de las cadenas que devuelve un subconjunto o subcadena utilizando dos índices [inicio:fin]:

El primer índice indica donde empieza la subcadena (se incluye el carácter).
El segundo índice indica donde acaba la subcadena (se excluye el carácter)."""


palabra = "Python"
palabra[0:2]
'Py'
palabra[0:3]
'Pyt'
palabra[2:]
'thon'

"""Si un índice se encuentra fuera del rango de la cadena, dará error:
   
   palabra[99]

IndexError  Traceback (most recent call last)
<ipython-input-47-b31ddef6ab27> in <module>()
----> 1 palabra[99]
IndexError: string index out of range"""


"""Pero con slicing esto no pasa y simplemente se ignora el espacio hueco:
      palabra[:99]

      'Python'
"""

#INMUTABILIDAD
"""Una propiedad de las cadenas es que no se puede modificar su contenido. Si intentamos reasignar un carácter, no nos dejará:
palabra[0] = "N"

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-51-c87a9e773639> in <module>()
----> 1 palabra[0] = "N"
TypeError: 'str' object does not support item assignment"""


"""Sin embargo, utilizando slicing y concatenación podemos generar nuevas cadenas fácilmente:


palabra = "N" + palabra[1:]
palabra

'Nython'"""


# **************************************************************************************************************************************
#4. LECTURA POR TECLADO

"""Una forma de trabajar con datos dinámicos es a través del teclado con la instrucción input() que lee y devuelve una cadena"""

valor = input("Introduce un valor: ")
# Introduce un valor: 100
'100'


# Se utiliza la función int() para transformar una variable cadena a entero:


valor = int(input("Introduce un número entero: "))
valor * 2

# Introduce un número entero: 500
1000

# También se tiene la función float() que hace lo propio pero transformando la cadena a flotante:


valor = float(input("Introduce un número entero o flotante: "))
valor * 2

# Introduce un número entero o flotante: : 3.14
6.28

# **************************************************************************************************************************************
#4. OPERADORES DE ASIGNACIÓN

#Suma en asignación
a = 5
a += 5  

#Resta en asignación
a = 5
a -= 10  

#Producto en asignación
a = 5
a *= 2  

#División en asignación
a = 5
a /= 2  

#Módulo en asignación
a = 5
a %= 2

#Potencia en asignación
a = 5
a **= 3


# **************************************************************************************************************************************
#5 OPERADORES DE COMPARACIÓN
#  <, >, ==, !=, <=, >=   True  False
variable = 3 == 5
print (f'la operación es {variable}') #False
variable = 3 == 3
print (f'la operación es {variable}') #True
variable = 9 >= 9
print (f'la operación es {variable}') #True


# ****************************************************EJEMPLOS MINTIC ********************************************************************
#1. Realizar una suma, resta, multiplicación, división y módulo

numero1 = 4
numero2 = 5

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
div = 10 // 3 #división entera
div2 = 10 / 3 #división normal
modulo = 25 % 2
potencia = 2 ** 3
print(f'Los numeros ingresados son : {numero1} y {numero2}\nEl valor de la suma es: {suma},\nEl valor de la resta es: {resta},\nEl producto es: {producto},\nLa división entera es: {div},\nLa división flotante es: {div2},\nEl módulo es: {modulo},\ny El valor de la potencia es: {potencia}')

#2. Realizar la raiz cuadrada

import math

raizP = 4 ** (1/2) #raiz con potencia
raiz_pow = pow(9,1/2) #raiz con pow
raiz_math = math.sqrt(16) #raiz con funcion sqrt
print(f'El valor de la raiz con potencia es: {raizP},\nEl valor de la raiz con método pow es: {raiz_pow},\ny El valor de la raiz con método math es: {raiz_math} ')


#3. Lea desde el teclado el nombre y la edad de cualquier persona e imprima tanto
#el nombre como la edad

#lectura de teclado
nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
print("Su nombre es" + nombre + "y su edad es " + str(edad))
print (f'Su nombre es {nombre} y su edad es {edad} años')

#4. Lea dos números. Calcule la suma e imprima la suma y los dos números.

numero1 = int(input("Digite el primero número: "))  #entrada de información
numero2 = int(input("Digite el segundo número"))

suma = numero1 + numero2  #proceso de información

print(f'La suma de {numero1} con {numero2} es igual a {suma}') #salida de datos

"""#47 Escribir un programa para convertir una medida dada en pies a sus
equivalentes en:
1. Yardas
2. Pulgadas
3. Centímetros
4. Metros
(1 pie =12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54cm, 1m= 100cm). Leer el 
número de pies e imprimir el número de yardas, pies, pulgadas, centímetros y 
metros."""

pies = float(input("Digite la medida inicial en pies: "))
pulgadas = 12 * pies
print (f'La medida en pulgadas es {pulgadas}')

import math
a = 2
b = 9
c = 3
x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2*a)
print(x1)

# *****************************MIO*****************************************************

import math

currentYear = 2021
print(f'El año actual es, {currentYear} y este es el mejor') #Imprimir todo en una misma línea#

raiz = pow(9,1/2) #Raiz cuadrada#
print(raiz) 

raiz = math.sqrt(16) #Raiz cuadrada opción principal#
print(raiz) 

nombre = input("Teclee su nombre ")

apellido = input(f"ahora {nombre} teclee su apellido ")

edad = input(f"Muy bien {nombre} {apellido} ahora teclee su edad")





