#####OPERACIONES BÁSICAS####

#1. Crear una funcion que reciba el tamaño del arreglo y el usuario debe llenarlo con numeros aleatorios entre 1 y 99. Una vez se tenga el arreglo se deberá hacer los siguientes: 
# a.Mostrar los datos
# b. Cantidad de datos
# c.sumar los datos
# d.Posición del dato mayor 
# e.Posición del dato menor 
# f. Intercambiar los datos
# g.Ordenar los datos
# g.números pares e impares

import random #libreria para añadir numeros aleatorios

def aleatorio(arreglo,n):
    for i in range(0,n):
        arreglo[i]=random.randint(1,99) #Función para llenar los datos del vector de manera aleatoria de 1 a 99.    

n= int(input("Digite el tamaño del vector")) #tamaño del vector
arreglo=[0]*n #inicializando el vector
# print(arreglo)
aleatorio(arreglo,n) 
print(f'a. El vector generado es el siguiente: {arreglo}') 
print(f'b. El tamaño del vector es: {len(arreglo)}') 

suma=0
contador=0
for i in range (0,n):
    suma+=arreglo[i]
    contador+=suma
print(f'c. El vector generado tiene la siguiente suma: {suma}')

mayor=arreglo[0]
menor=arreglo[0]

for i in range(0,n):
    if arreglo[i] > mayor:
        mayor = arreglo[i]
    if arreglo[i] < menor:
        menor = arreglo[i]   

print(f'd. El mayor dato es: {mayor}')
print(f'e. El menor dato es: {menor}')

for i in range(n):
    if(i<n):
        aux=arreglo[i]
        arreglo[i]+=i+1
        arreglo[i] = aux

print(f'f. El nuevo vector generado es el siguiente: {arreglo}') 

band = False #El vector se encuentra desordenado

while band == False:
    band = True
    for i in range(n-1):
        if arreglo[i] > arreglo[i+1]:
            aux=arreglo[i]
            arreglo[i] = arreglo[i+1]
            arreglo[i+1] = aux
            band = False

print(f'g. El ordenamiento del arreglo con el metodo burbuja es: {arreglo}') 

numerosPares = []
numerosImpares = []

for i in range(0,n):           
    if arreglo[i] % 2 == 0:
        numerosPares.append(arreglo[i])
    else:
        numerosImpares.append(arreglo[i])
print("Numeros pares: ",numerosPares)
print("Numeros impares: ",numerosImpares)

# 2 Censo a 10 municipios

def sumaTotal(V, n):
    suma=0
    for i in range (1, n):
        suma+=V[i]
    return suma

def mayorDato(V, n):
    mayor=0
    for i in range (n):
        if V[i] > V[mayor]:
            mayor =i
    return mayor

#Lo anterior es crear funciones que me ayuden a indicar la totalidad de habitantes y el municipio con mayor numero de habitantes.

n = 10 #Numero de municipios a revisar

nomMunicipio = [",", "medellin", "bello", "envigado", "sabaneta", "sabaneta", "itagui", "rionegro", "La ceja", "Entrerios", "andes", "abejorral",] # Los municipios a explorar
acumulador_municipio = [0] * (n+1) #Se inicializa en 0 y se colocan 11 espacios para que llegue de 1 a 10
municipio=int(input("Ingrese el codigo del municipio"))

while municipio !=0:
    np=int(input("ingrese el número de personas")) #Numero de personas del municipio
    acumulador_municipio[municipio]+=np #Acumulador del numero de personas
    municipio=int(input("Ingrese el codigo del municipio")) #Nuevamente pregunta otro municipio para hacer el mismo proceso
    #Cuando se coloque cero se sale del ciclo y pasa al FOR

for i in range (1, n+1):
    print(f'Municipio {nomMunicipio[i]}, Habitantes = {acumulador_municipio[i]} ')

    #Revisa los datos anteriores y se genera la impresion
th=sumaTotal(acumulador_municipio, n)
print(f"Total habitantes {th}")
i=mayorDato(acumulador_municipio,n)
print(f"El mayor numero de habitantes es del municipio {nomMunicipio[i]} con {acumulador_municipio[i]} habitantes")



#REPASO VECTORES#
import random
n= int(input("ingrese el tamaño del vector"))
v= [0]*n

for i in range(0,n):
    v[i]= random.randint(1,9)
print(v)


mayor =  v[0]
posicionMayor=0

for i in range(n):
    if v[i]> mayor:
        mayor = v[i]
        posicionMayor=i


print(f'el numero mayor es {mayor}')
print(f'Esta en la posición {posicionMayor}')

# 2. Leer 10 numeros y determinar en que posición se encuentran los numeros terminados en 4

v= [0]*(10)

for i in range(10):
    v[i] = random.randint(1,50)

print(v)

for i in range(10):
    if v[i] % 10 == 4:
        print(i, end=',')

# 3. Leer 10 numeros enteros y determinar cuales son numeros primos, dos divisores 1 y el numero
import random

n = int(input(("Digite el tamaño del vector")))

v= [0]*n

for i in range (n):
    v[i]= random.randint(1,50)
print(v)

for i in range (n):
    divisores = 1
    for j in range (2, v[i]+1):        
        if v[i] % j == 0:
            divisores+=1

    if divisores > 2:
        print(f"el numero {v[i]} no es primo")

    else:
        print(f"El numero {v[i]} es primo")






