# numero1 = int(input("Ingrese el primer número: "))
# numero2 = int(input("Ingrese el segundo número: "))
# numero3 = int(input("Ingrese el tercer número: "))
# digito_mayor = 0
# posicion = 0

# while numero1 > 0:
#   digito = numero1 % 10
#   if digito > digito_mayor:
#     digito_mayor = digito
#     posicion = 1
#   numero1 = numero1 // 10
  
# while numero2 > 0:
#   digito = numero2 % 10
#   if digito>digito_mayor:
#     digito_mayor = digito
#     posicion = 2
#   numero2 = numero2 // 10
  
# while numero3 > 0:
#   digito = numero3 % 10
#   if digito>digito_mayor:
#     digito_mayor = digito
#     posicion = 3
#   numero3 = numero3 // 10
  
# if posicion == 1:
#   print(f"El mayor dígito ingresado es: {digito_mayor} y está en el primero numero")

# elif posicion == 2:
#   print(f"El mayor dígito ingresado es: {digito_mayor} y está en el segundo número")

# else:
#   print(f"El mayor dígito ingresado es: {digito_mayor} y está en el tercer número")


# 1.	Leer un número entero y determinar si es un número terminado en 4.  

n=int(input("Ingresa un numero entero"))

if n%10==4:
  print(f"el numero {n} termina en 4")
else:
  print(f"el numero {n} no termina en 4")


n=int(input("Ingresa un numero entero"))
while n > 0:
  if n%10==4:
    print(f"el numero {n} termina en 4")
    break
  else:
    print(f"el numero {n} no termina en 4")

  n+=1

# 2.	Leer un número entero y determinar si tiene 3 dígitos.


n=int(input("Ingresa un numero entero"))

if (len(str(n))==3):
  print(f"El número {n} ingresado tiene 3 digitos")
else:
   print(f"El número {n} ingresado no tiene 3 digitos")

# 3.	Leer un número entero y determinar si es negativo. 

n=int(input("Ingresa un numero entero"))

if (n<0):
  print(f"El número {n} ingresado es negativo")
else:
   print(f"El número {n} ingresado no es negativo")

# 4.	Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.  

n=int(input("Ingresa un numero entero de 2 digitos"))

suma=0

while n > 0:
  d=n%10
  suma+=d
  n//=10

print(f"La suma de los digitos ingresados es {suma}")

# 5.	Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.  

n=int(input("Ingresa un numero entero de 2 digitos"))

a= n//10
b= n%10

while n > 0:
    if a % 2 ==0:
        print(f'El primer digito es par')
    if b % 2 == 0:
        print(f'El segundo digito es par')
    if a %2 ==0 and b % 2 ==0:
        print(f'Los dos digitos son pares')
    else:
        print(f'No son pares')
        
    n=int(input("Ingresa un numero entero de 2 digitos"))

# 6.	Leer un número entero de dos dígitos menor que 20 y determinar si es primo.  



# 7.	Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.  



# 8.	Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.  



# 9.	Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.  



# 10.	Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.  



# 11.	Leer dos números enteros y determinar cuál es el mayor.  



# 12.	Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.  



# 13.	Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par.  



# 14.	Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.  




# 15.	Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.  



# 16.	Leer  un  número  entero  de  tres  dígitos  y  determinar  si  al  menos  dos  de  sus  tres  dígitos  son iguales. 



# 17.	Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.  



# 18.	Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.  



# 19.	Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables. 



# 20.	Leer tres números enteros y mostrarlos ascendentemente.



