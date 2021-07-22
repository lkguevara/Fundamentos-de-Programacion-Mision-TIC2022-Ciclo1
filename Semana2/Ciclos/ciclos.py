#CICLOS

#SENTENCIA WHILE

"""Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True. Queda en las manos del programador decidir el momento en que la condición cambie a False para hacer que el While finalice."""

#EJEMPLOS

#1. Programa que imprima los 100 primeros números naturales
contador = 1
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#2. Programa que calcule el promedio de los primeros 100 números naturales
contador = 1        #contador
suma = 0            #acumulador
while contador <= 100:
    suma = suma + contador
    contador = contador + 1
promedio = suma / (contador - 1)
print("El promedio es igual a: ", promedio)

#3. Programa que solicite un número al usuario y se calcule el promedio desde el 1 hasta ese número dado
limite = int(input("Digite un número"))
suma = 0
i = 1
while i <= limite:
    suma = suma + i
    i = i + 1
promedio = suma / limite
print("El promedio es igual a : ", promedio)

#4. Realizar un programa que imprima los números pares que hay del 1 al 100
#opcion 1
import time
start_time = time.time()
contador = 1
while contador <= 10000:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

print("--- %s seconds ---" % (time.time() - start_time))

#opcion2
import time
start_time = time.time()
contador = 2
while contador <= 10000:
    print(contador)
    contador = contador + 2
time = (time.time() - start_time)
print("--- %s seconds ---" % time)

#Programa que imprima los 100 primeros números naturales
contador = 1
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#******************************************************************************************************************************************

##SENTENCIA FOR

"""
for i in range(valorInicial, valorFinal, variación):
#instrucciones del ciclo"""

#Ejemplos:

#1. Establecer un límite y escribir los numeros de 4 en 4

dato = int(input("Digite el valor máximo"))
for contador in range(4,dato+1,4): # (inicia en 4; tamaño del dato + 1; de a 4 pasos )
    print(contador)                   

#2. Hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay.

nombre = input("Digite el nombre del producto: ")
cantidad = int(input("Digite la cantidad disponible del producto: "))
print(f'Del producto {nombre} se tienen {cantidad} unidades')   #Almacena un solo producto

#solicitar varios productos el nombre y la cantidad
#opcion 1
rango = int(input("Digite la cantidad de productos"))
for i in range(rango):
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')

#opcion 2
while True:
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')
    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '2':
        break

#Estructuras de datos  ( ) , [ ] , { }
#listas [ ] corchetes
listado = [2, 3, 4, 5, 6, 3 , 4]
print(listado)
print(listado[3])
print(len(listado)) #length tamaño

#Si quiero sumar los valores de esta lista
#opcion 1
suma = 0 #acumulador
i = 0 #contador de posicion no de valor
while i < len(listado):
    suma = suma + listado[i]
    i = i + 1

#opcion2
listado = [2, 3, 4, 5, 6, 3, 4]
suma = 0
for item in listado:
    suma = suma + item
print(suma)

listado = [2, 3, 4, 5, 6, 3, 4]
print(listado)
listado.append(6)
print(listado)
listado.remove(6)
print(listado)
print(dir(listado))

#tupla () parentesis  -> inmutable no puede cambiar  mutable o inmutable
datos = (2,3,4,5)
print(datos)
datos = (1,2,3,4)
print(datos)

#Sets { } llaves -> Conjuntos
datos = {6, 4, 2, 1}
print(datos)
#print(datos[1])   #error no hay posiciones especificas
datos.add(8)
print(datos)
datos.remove(4)
print(datos)
datos.add(8)
print(datos)

if 2 in datos:
    print("El numero 2 si se encuentra en el conjunto")

datos = {6, 4, 2, 1}
datos2 = {5, 1, 3}
print(datos)
print(datos2)
comunes = datos.intersection(datos2)
print(comunes)
todos = datos.union(datos2)
print(todos)

#Diccionarios -> Es un par llave y valor
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)

producto = {
    'nombre': 'fab',
    'cantidad': 2
}

#Agregar elementos al dicccionario
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)
datos['correo'] = "edwin@gmail.com"
print(datos)

#imprimir un diccionario

for i in datos:  #imprime la llave
    print(i)


for i in datos.values():   #imprime el valor
    print(i)


for llave, valor in datos.items():  #imprime el par de llave y valor
    print(llave, " \t ", valor)

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
inventario = []         #creamos una lista vacía
while True:             #ciclo infinito
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))

    producto = {           #creo mi diccionario
        'nombre': nombre,
        'cantidad': cantidad
    }

    inventario.append(producto)

    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '2':            #condicion para finalizar el ciclo
        break

for i in inventario:
    print("Del producto", i['nombre'], "usted tienen ",i['cantidad'], "unidades")

#**************************************************************************************************************************

#SENTENCIA BREAK- CONTINUE

#Instrucción break
"""Sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración"""

# Primer ejemplo
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale", c)
        break #Rompe el ciclo
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)

"""c vale 1
c vale 2
c vale 3
Rompemos el bucle cuando c vale 4"""


# Segundo ejemplo
for letra in "Python":
    if letra == "h":
        break
    print ("Letra actual : " + letra)

# Tercer ejemplo
var = 10
while var > 0:
    var = var -1
    if var == 5:
        break
    print ("Valor actual de la variable : " + str(var))

print ("fin del script")


#Instrucción continue
"""Sirve para "saltarse" la iteración actual sin romper el bucle."""

# Primer ejemplo

c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteración", c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)

"""
c vale 1
c vale 2
c vale 5
c vale 6
Se ha completado toda la iteración y c vale 6"""


# Segundo ejemplo
for letra in "Python":
    if letra == "h":
        continue
    print ("Letra actual : " + letra)


# Tercer ejemplo
var = 10
while var > 0:
    var = var -1
    if var == 5:
        pass
    print ("Valor actual de la variable :" + str(var))

print ("fin del script")

#*****************************************************************EJEMPLOS*********************************************************

#1. Crear un menú interactivo de la siguiente manera:

"""
Bienvenido al menú interactivo
¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
1
Hola, espero que te lo estés pasando bien
¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
2
Introduce el primer número: 10
Introduce el segundo número: 5
El resultado de la suma es:  15.0
¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
kdjsk
Comando desconocido, vuelve a intentarlo
¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
3
¡Hasta luego! Ha sido un placer ayudarte"""


print ("Bienvenido al menú interactivo")

while True:
    print("""¿Qué quieres hacer? Escribe una opción : \n1.Saludar\n2. Sumar dos números\n3. Salir""")
    opcion = input("Ingrese una opcion")
    if opcion == "1":
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == "2":
        num1=int(input("Introduce el primer número"))
        num2=int(input("Introduce el segundo número"))
        suma= num1+num2
        print(suma)
        break
    else:
        print("¡Hasta luego! Ha sido un placer ayudarte!")
        
    
