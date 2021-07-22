#FUNCIONES

"""Se definen con la palabra reservada def(), el nombre de la función y unos paréntesis, que también se utilizan para hacer la llamada:"""

# Funcion sin parametro
def suma():  #def es la palabra reservada
    print(5+3)
suma()

# Funciones - Parametros

def sumar(x,y):
    print(num1+num2)

num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))
sumar(num1,num2)

# Funcion que retorna valores

def sumar(x,y):
    total= num1+num2
    return total

num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))

suma = sumar(num1,num2)
print(suma)


"""************************EJEMPLOS*********************************"""
#1. Calcular el numero mayor de 2 números
def mayor(num1,num2):
    if num1<num2:
        return num2
    else:
        return num1


x= int(input("ingrese el primer numero"))
y= int(input("ingrese el segundo numero"))

if x != y:
    nmayor = mayor(x,y)
    print(f"El numero mayor es {nmayor}")
else:
    print("Los numeros son iguales")


#2. Calcular el cociente y el residuo de 2 numeros por medio de funciones
def division(dividendo, divisor):
    cociente=dividendo // divisor
    residuo=dividendo % divisor
    return cociente, residuo


x= int(input("ingrese el primer numero"))
y= int(input("ingrese el segundo numero"))

a,b=division(x,y)
print(f'El cociente es {a} y el residuo es {b}')

#3. Realizar un programa que pida dos números enteros y muestre en pantalla el siguiente menú
"""CALCULADORA
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR
SELECCIONE UNA OPCION
El usuario debe digitar un número y el programa realiza el cálculo respectivo y muestra el resultado
en pantallA"""

def entradaDatos():
    num1 = int(input("Digite el primer número: "))
    num2 = int(input("Digite el segundo número: "))
    return num1, num2

def mostrarMenu():
    opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
    return opcion

def suma(numero1,numero2):
    suma = numero1 + numero2
    return suma

def resta(numero1,numero2):
    print("La resta es: ", numero1 - numero2)

def multiplicacion(numero1, numero2):
    print("La multiplicación es: ", numero1 * numero2)

def division(numero1, numero2):
    print("La división es: ", numero1 / numero2)

while(True):
    numero1,numero2 = entradaDatos()
    opcion = mostrarMenu()
    if opcion == 1:
        total = suma(numero1,numero2)
        print ("la suma es ",total)
    elif opcion == 2:
        resta(numero1,numero2)
    elif opcion == 3:
        multiplicacion(numero1,numero2)
    elif opcion == 4:
        division(numero1,numero2)
    elif opcion == 5:
        print("Hasta la vista")
        break
    else:
        print("Opción invalida")

#5. Extrayendo las funciones a un archivo mathFunctions.py

import mathFunctions

while(True):
    numero1,numero2 = mathFunctions.entradaDatos()
    opcion = mathFunctions.mostrarMenu()
    if opcion == 1:
        total = mathFunctions.suma(numero1,numero2)
        print ("la suma es ",total)
    elif opcion == 2:
        mathFunctions.resta(numero1,numero2)
    elif opcion == 3:
        mathFunctions.multiplicacion(numero1,numero2)
    elif opcion == 4:
        mathFunctions.division(numero1,numero2)
    elif opcion == 5:
        print("Hasta la vista")
        break
    else:
        print("Opción invalida")


# 6. Conversion de dinero 

def converorMoneda():
    pesos=float(input("Ingrese el valor en pesos colombianos"))
    valorDolar=3600
    conversionDolar=round((pesos/valorDolar),2)
    print(f'{pesos} pesos colombianos a dolares es {conversionDolar}')

converorMoneda()

# 7. Un bus viaja a 30km/h en promedio, 90km recoger pasajeros demora 2 minutos por pasajero, bajar pasajero demora 1 minuto.

# ¿Cuántos minutos demora el bus, dada una cantidad de pasajeros que se subieron y otra cantidad que se bajaron?




def tiempoRecorrido(pasajero_subida,pasajero_bajada):
    velocidad=30
    distanciaRecogePasajero=90
    recorridoMinutos = ((distanciaRecogePasajero/velocidad)*(60))+(pasajero_subida*2)+(pasajero_bajada)
    return recorridoMinutos


print(tiempoRecorrido(40,38))
