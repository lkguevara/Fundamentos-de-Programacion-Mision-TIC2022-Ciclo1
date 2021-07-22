# 1. Construir un programa que lea un entero n>0 y calcule la suma de todos los enteros desde 1 hasta n

limite=int(input("Digite un número"))

i=1
suma=0

while i <= limite:
    print(i)
    suma+=i
    i+=1    

print("la suma total de los numeros ingresados es", suma)


# 2. Contruir un programa que permita calcular y mostrar el factorial de un entero ingresado por el teclado
import time
start_time = time.time()

limite=int(input("Digite un número"))
i=1
factorial=1

while i <= limite:
    print(i)
    factorial*=i
    i+=1    

print("la multiplicación total de los numeros ingresados es", factorial)
print("--- %s seconds ---" % (time.time() - start_time))

# 3. Determine el nuevo salario de una persona en una lista de empleados
nombre=input("ingrese el nombre del empleado")
while nombre != "":
    salario=int(input(f'{nombre} ingrese salario'))
    aumento=0
    if salario < 1000:
        aumento = salario*0.1
    nuevo_salario= salario+aumento
    print(f'El trabajador {nombre} aumento de salario a {nuevo_salario}')
    nombre=input("ingrese nuevo nombre")    
print("fin")

# 4. Elaborar un programa para determinar el nuevo salario de una persona, contando a cuantas se les hizo el calculo, cuantas tuvo aumento mayor que cero, el total de salarios anteriores, el total de aumentos, el total de nuevos salarios, el promedio salarial antes y despues del aumento y el promedio de aumentos

contador=0 #Cantidad de personas procesadas#
contAu=0 #Cantidad de personas con aumento >0#
tsa=0 #Total salarios anteriores#
tau=0 #total aumentos#
tns=0 #total de nuevos salarios#

nombre=input("ingrese el nombre")
while nombre != "":
    salario=int(input(f'{nombre} ingrese su salario'))
    tsa +=salario #acumulando el salario#
    contador+=1
    aumento=0
    if salario <1000:
        aumento=salario*0.1
        tau+=aumento #Se acumula en el total de aumentos#
        contAu+=1
    nuevo_salario=salario+aumento
    tns+=nuevo_salario
    print(f'nombre {nombre}\tsalario {salario}\taumento {aumento}\tnuevo salario de {nuevo_salario}')
    nombre=input("ingrese nuevo nombre")
psa = tsa/contador
pau = tau/contador
pns = tns/contador

print(f'Total empleados {contador}\t total con aumento > 0 = {contAu}')
print(f'Total salarios anteriores {tsa}\tpromedio {psa}')
print(f'Total aumentos {tau}\tpromedio {pau}')
print(f'Total nuevos salarios {tns}\tpromedio {pns}')


# 5. determinar si un numero x es primo o no

x=int(input("ingrese un numero entero"))
i=2 #Los numeros primos inician en 2#
while i<= x**(0.5) and x % i !=0:
    i+=1
if i> x**(0.5):
    print(f'{x} es un número primo')
else:
    print(f'{x} no es un número primo, es divisible por {i}')

# 5. escribir los numeros primos desde 2 hasta 1000

x=3
while x<= 100:
    i=2
    while i<= x**(0.5) and x % i !=0:
        i+=1
    if i> x**(0.5):
        print(x)
    x+=2


# *********************CICLO FOR ****************************************

# 1. La suma de los enteros desde 1 hasta n

n=int(input("ingrese un número"))

i=1
suma=0

for i in range(1,n+1):
    print(i)
    suma+=i
print(f'La suma de los numeros enteros hasta {n} es {suma}')

# 2. El factorial de un entero n

n=int(input("ingrese un número"))

i=1
factorial=1

for i in range(1,n+1):
    print(i)
    factorial*=i
print(f'El factorial de los numeros enteros hasta {n} es {factorial}')


# *********************BREAK ****************************************

# 1. Numero primos

x=int(input("ingrese un número entero"))

if x % 2 == 0:
    print(f'{x} NO es un numero primo, es un numero PAR')
    exit(0)

i=2

for i in range(3,int(x**(0.5))+1, 2):
    if x % i == 0:
        print(f'{x} NO es un numero primo, es divisible por {i}')
        break
if x % i != 0:
    print(f'{x} es un numero primo')


my_set = {5,8,9,2,4}
print(my_set)

# 2. Tabla de multiplicar un número

n=int(input("Ingrese el número de la tabla de multiplicar"))

i=1
multiplicación=0

for i in range(1,11):
  multiplicación= n*i
  print(f'{n} * {i} = {multiplicación}')
  print()

# 2. Tabla de multiplicar varios números

n=int(input("Ingrese el numero de tabla que se iniciará"))
n2=int(input("Ingrese hasta que numero de tabla desea finalizar"))

m=int(input("Ingrese desde que número de cada tabla va a iniciar"))
m2=int(input("Ingrese hasta que número de cada tabla va a multiplicar"))


i=1
j=1
multiplicación=0

for i in range(n,n2):
  print(f'Tabla de multiplicar del {i}:')
  for j in range(m,m2):    
    print(f'{i}*{j} = {i*j}')
  print()
  


  
  

    












    



