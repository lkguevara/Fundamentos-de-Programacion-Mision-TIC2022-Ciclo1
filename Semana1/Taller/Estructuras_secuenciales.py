import math

# 1. Lea desde el teclado el nombre y la edad de cualquier persona e imprima tanto el nombre como la edad 
nombre = input("Ingrese su nombre")
edad = int(input("Ingrese su edad"))
print(f'Su nombre es {nombre} y tiene {edad} años')

# 2. Lea dos números. Calcule la suma e imprima la suma y los dos números.

num1 = int(input("Ingrese el primer número"))
num2 = int(input("Ingrese el segundo número"))
suma= num1+num2
print(f'La suma total de los números indicados es {suma}')

# 3. Leer un número y calcular el 5% del número leído.

num1 = int(input("Ingrese un número"))
porcentaje= num1*0.05
print(f'El 5% del valor ingresado es {porcentaje}')


# 4. Elaborar un algoritmo que calcule e imprima el área de un triangulo, sabiendo que se conoce su base y su altura.

base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))
area_Triangulo= base*altura
print(f'El area del triangulo es {area_Triangulo}')

# 5. Calcular el área de un rectángulo

base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))
area_Rectangulo= base*altura
print(f'El area del triangulo es {area_Rectangulo}')

# 6. Calcular el área de un cuadrado

base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))
area_cuadrado= base*altura
print(f'El area del triangulo es {area_cuadrado}')


# 7. Calcular el área de un circulo
radio = int(input("Ingrese el radio"))
area_circulo= math.pi*radio**2
print(f'El area del triangulo es {area_circulo}')

# 8. Un alumno posee 3 notas en la materia de algoritmos y desea saber cual será su calificación final

nota1= int(input("Ingrese la primera nota"))
nota2= int(input("Ingrese la segunda nota"))
nota3= int(input("Ingrese la tercera nota"))
nota_promedio= (nota1+nota2+nota3)/3
print(f'El promedio de calificación es {nota_promedio}')

# 9. Calcule e imprima el promedio de edad de 3 personas.

edad1= int(input("Ingrese la edad 1"))
edad2= int(input("Ingrese la edad 2"))
edad3= int(input("Ingrese la edad 3"))
edad_promedio= (edad1+edad2+edad3)/3
print(f'El promedio de calificación es {edad_promedio}')

# 10. Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad cambiaría es un dato desconocido

Valor_Pesos= int(input("Ingrese la cantidad de pesos a convertir"))
dolar= int(input("Ingrese el valor del dolar actual"))
conversión= (Valor_Pesos*dolar)
print(f'El promedio de calificación es {conversión}')

# 11. Calcular el número de pulsaciones que una persona debe tener por cada 11 segundos de ejercicio, si la formula es: num. Pulsaciones = (220 - edad)/10

edad= int(input("Ingrese su edad"))
Pulsación_segundo= ((220 - edad)/10)/60
Resultado=Pulsación_segundo*11
print(f'El promedio de pulsaciones cada 11 segundos es {Resultado}')

# 12. Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior.

salario= int(input("Ingrese su salario anterior"))
aumento=salario+(salario*0.25)
print(f'Su salario actual es {aumento}')

# 13. El dueño de una tienda compra un artículo a un precio determinado. Obtener el precio en que lo debe vender para obtener una ganancia del 30%.

Precio_Articulo= int(input("Ingrese el precio del producto"))
Precio_Venta=Precio_Articulo+(salario*0.30)
print(f'Su salario actual es {Precio_Venta}')

# 14. Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera.

tiempo1= int(input("Ingrese el tiempo obteniedo el lunes"))
tiempo2= int(input("Ingrese el tiempo obteniedo el miercoles"))
tiempo3= int(input("Ingrese el tiempo obteniedo el viernes"))
tiempo_promedio= (tiempo1+tiempo2+tiempo3)/3
print(f'El promedio de calificación es {tiempo_promedio}')

# 15. Leer el nombre de un empleado, su salario básico por hora y el número de horas trabajadas en el mes. Calcular su salario mensual e imprimir tanto el nombre como su salario

nombre= input("Ingrese el nombre del empleado")
Salario_Hora= int(input("Ingrese el salario por hora"))
horas_Trabajadas_Mes= int(input("Ingrese las horas trabajadas en el mes"))
Salario_Mensual= Salario_Hora*horas_Trabajadas_Mes
print(f'El empleado {nombre} tiene un salario mensual de ${Salario_Mensual} pesos')

# 16. Preste $500.000 y pague $ 570.000 Cuanto interés me cobraron

prestamo=500000
pago=570000
diferencia=pago-prestamo
interes_generado= int((diferencia/prestamo)*100)
print(f'El interes generado por el prestamo realizado fue {interes_generado}%')

# 17. Calcular la cantidad a pagar de matricula por un estudiante de la siguiente forma: el total a pagar es igual a los cargos fijos mas los cargos variables. Los cargos fijos son $300000 y los cargos variables se calculan sumando el 10% del patrimonio y el 15% de la renta. Leer los datos necesarios

cargoFijo= 300000
patrimonio= int(input("Ingrese el valor del patrimonio"))
renta= int(input("Ingrese el valor de la renta"))
cargoVariable= (patrimonio*0.10)+(renta*0.15)
valor_Matricula= int(cargoFijo+cargoVariable)
print(f'El valor total de la matricula es de ${valor_Matricula} pesos')

# 18. La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula: Masa = (presión * volumen)/(0.37 * (temperatura + 460)) Calcular la masa.

presion= int(input("Ingrese la presion"))
volumen= int(input("Ingrese el volumen"))
temperatura= int(input("Ingrese la temperatura"))
masa= int((presion*volumen)/(0.37 * (temperatura + 460)))
print(f'El valor de la masa es {masa}')


# 19. En un hospital existen tres áreas: Ginecología, Pediatría, Traumatología. El presupuesto anual del hospital se reparte conforme a la sig. Tabla:
# Área Porcentaje del presupuesto
# Ginecología 40%
# Traumatología 30%
# Pediatría 30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto  presupuestal.

presupuesto_Anual= int(input("Ingrese valor del presupuesto anual"))
Ginecología= int(presupuesto_Anual*0.4)
Traumatología= int(presupuesto_Anual*0.3)
Pediatría= int(presupuesto_Anual*0.3)
print(f'El valor que recibirá cada área es lo siguiente: Ginecología ${Ginecología}, Traumatología ${Traumatología}, y Pediatría ${Pediatría}')

# 20. Un alumno desea saber cual será su nota definitiva si la calificación se obtiene de la sig. manera:
# Examen 90%
# Promedio de tareas 10%
# En esta materia se pidió un total de tres tareas.

tarea1= int(input("Ingrese la nota de la tarea 1"))
tarea2= int(input("Ingrese la nota de la tarea 2"))
tarea3= int(input("Ingrese la nota de la tarea 3"))
promedio_Tareas= (tarea1+tarea2+tarea3)/3
examen= int(input("Ingrese la nota del examen"))
nota_final= int((examen*0.9)+(promedio_Tareas*0.10))
print(f'El promedio de calificación es {nota_final}')

# 21. Conocidos dos valores, elaborar un programa que calcule el resultado de dividir el primero sobre el segundo.

valor1= int(input("Ingrese primer valor"))
valor2= int(input("Ingrese segundo valor"))
resultado= int(valor1/valor2)
print(f'El resultado de la división es {resultado}')

# 22. Un empleado trabaja 48 horas en la semana a razón de $ 12000 la hora, la retención en la fuente es de 5% del salario básico. Se desea saber cual es el salario neto del trabajador.

salario_Hora=12000
salario_Mes=salario_Hora*48*4
retencion=salario_Mes*0.05
salarioTotal= int(salario_Mes-retencion)
print(f'El salario neto del trabajador es {salarioTotal}')

# 23. Hacer un algoritmo que, capture por pantalla los dos lados diferentes de un rectángulo, encuentre el perímetro y el área del mismo.

base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))
area_Rectangulo= base*altura
perimetro= 2*base+2*altura
print(f'El area del triangulo es {area_Triangulo} y el perimetro es {perimetro}')

# 24. Elabore Un algoritmo que capture un número por pantalla y obtenga su cuadrado y su cubo.

num = int(input("Ingrese un número"))
cuadrado= int(num**2)
cubo= int(num**3)
print(f'El cuadrado del número ingresado es {cuadrado} y el cubo es {cubo}')

# 25. Capturar por pantalla el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la Longitud de la circunferencia.
import math

radio = int(input("Ingrese el radio"))
area_circulo= int(math.pi*radio**2)
longitud_Circuferencia= int(math.pi*(radio*2))
print(f'El area del circulo es {area_circulo} y la longitud de circunferencia es {longitud_Circuferencia}')

# 26. Dados los tres lados de un triangulo, haga un algoritmo que encuentre:
# perímetro, semiperimetro y el área de un triangulo

base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))
lado1 = int(input("Ingrese el lado 1"))
lado2 = int(input("Ingrese el lado 2"))
lado3 = int(input("Ingrese el lado 3"))
area_Triangulo= base*altura
perimetro_Triangulo= lado1+lado2+lado3
semiperimetro_Triangulo= (lado1+lado2+lado3)/2
print(f'El area del triangulo es {area_Triangulo}, su perimetro es {perimetro_Triangulo} y su semiperimetro es {semiperimetro_Triangulo}')

# 27. Escribir un programa al cual ingrese la velocidad de un móvil expresada en metros por segundo e imprima en pantalla la velocidad en kilómetros por hora.

velocidad = int(input("Ingrese la velocidad en m/s"))
velocidad_convertida = velocidad*3600/1000
print (f'La velocidad en km/h es {velocidad_convertida}')

# 28. Una farmacia aplica al precio de los remedios el 10% de descuento. Hacer un programa que ingresado el valor de la compra calcule el descuento y el precio final

Precio_Remedio = int(input("Ingrese el costo del remedio"))
Precio_descuento = Precio_Remedio -(Precio_Remedio*0.10)
print (f'El precio del remedio con descuento es {Precio_descuento}')

# 29. Diseñe un algoritmo que determine el porcentaje de varones y de mujeres que hay en un salón de clases
cantidad_Estudiantes = int(input("Ingrese el número total de estudiantes"))
cantidad_Mujeres = int(input("Ingrese el número de mujeres"))
cantidad_Hombres = int(input("Ingrese el número de hombres"))
porcentaje_Mujer=cantidad_Mujeres*100/cantidad_Estudiantes
porcentaje_hombre=cantidad_Hombres*100/cantidad_Estudiantes
print (f'El porcentaje de mujeres es {porcentaje_Mujer} y el porcentaje de hombres es {porcentaje_hombre}')

# 30. El sueldo neto de un vendedor se calcula como la suma de un sueldo básico de 450.000 más el 12% del monto total vendido. Diseñe un algoritmo que determine el sueldo neto de un vendedor sabiendo que hizo tres ventas en el mes.

sueldo_basico=450000
monto_vendido= int(input("Ingrese el monto vendido"))
SueldoNeto= sueldo_basico + (monto_vendido*0.12)
print (f'El sueldo neto del vendedor es {SueldoNeto}')

# 31. Leer el sueldo de tres empleados y aplicarles un aumento del 10, 12 y 15% respectivamente. Desplegar el resultado.

sueldoEmpleado1= int(input("Ingrese el sueldo del empleado 1"))
sueldoEmpleado2= int(input("Ingrese el sueldo del empleado 2"))
sueldoEmpleado3= int(input("Ingrese el sueldo del empleado 3"))

print (f'El sueldo neto del empleado 1 es {sueldoEmpleado1 + (sueldoEmpleado1 * 0.1)}\nEl sueldo neto del empleado 2 es {sueldoEmpleado2 + (sueldoEmpleado2 * 0.12)} \nEl sueldo neto del empleado 3 es {sueldoEmpleado3 + (sueldoEmpleado3 * 0.15)}')

# 32. Diseñe un algoritmo que exprese la capacidad de un disco duro en megabytes,kilobytes y bytes, conociendo la capacidad del disco en gigabytes. Considere que 1 kilobyte = 1024 bytes, 1 megabyte = 1024 kilobyte, 1 gigabyte = 1024 megabytes.

capacidadDisco= int(input("Ingrese la capacidad del disco duro en Gigabytes"))
capacidad_megabytes = capacidadDisco*1024
capacidad_kilobytes = capacidad_megabytes*1024
capacidad_bytes = capacidad_kilobytes*1024

print (f'La capacidad del disco duro en megabytes es {capacidad_megabytes}\nLa capacidad del disco duro en kilobytes es {capacidad_kilobytes}\ny la capacidad del disco duro en bytes es {capacidad_bytes}')

# 33. Elabore un programa que realice la conversión de cm a pulgadas Donde 1cm = 0.39737 pulgadas.

medida_cm= int(input("Ingrese el valor en cm"))
conversión= medida_cm*0.39737

print (f'la conversion de los {medida_cm} cm ingresados a pulgadas es {conversión}pulgadas')

# 34.Elabore un programa que realice la conversión de libras a kilogramos
# Donde 1 Kg. = 2.2046 libras.

medida_lb= int(input("Ingrese el valor en libras"))
conversión= medida_lb/2.2046

print (f'la conversion de las {medida_lb} libras ingresadas a kilogramos es {conversión} kilogramos')

# 35. Obtener la edad de una persona en meses, si se ingresa su edad en años y meses. Ejemplo: Ingresado 3 años 4 meses debe mostrar 40 meses

edad_años= int(input("Ingrese su edad en años"))
edad_meses= int(input("complemente su edad en meses"))
conversión= (edad_años*12)+edad_meses

print (f'su edad en meses es {conversión}')

# 36. Desplegar el peso dado en kilos de una persona en gramos, libras y toneladas.

peso= int(input("Ingrese su peso en kg"))
peso_tonelada= peso*0.001
peso_libra= peso*2.2046
peso_gramo= peso_libra*500

print (f'su peso en kilogramos es {peso}\nEn toneladas es {peso_tonelada}\nEn libras es {peso_libra}\ny En gramos es {peso_gramo}')

# 37. Programa que evalúa la función y = 5x^2 3x + 2

x=int(input("Ingrese el valor de x"))
y= int(5*x**2-3*x+2)
print(f'el valor de y es {y}')

# 38.Un alumno desea saber cual será su promedio general en las tres materias mas difíciles que cursa y cual será el promedio que obtendrá en cada una de ellas Estas materias se evalúan como se muestra a continuación:

# La calificación de Matemáticas se obtiene de la sig. manera:
# Examen 90%
# Promedio de tareas 10%
# En esta materia se pidió un total de tres tareas.

# La calificación de Física se obtiene de la sig. manera:
# Examen 80%
# Promedio de tareas 20%
# En esta materia se pidió un total de dos tareas.

# La calificación de Química se obtiene de la sig. manera:
# Examen 85%
# Promedio de tareas 15%
# En esta materia se pidió un promedio de tres tareas.

tarea1_matematicas= int(input("Ingrese la nota de la tarea 1 de matematicas"))
tarea2_matematicas= int(input("Ingrese la nota de la tarea 2 de matematicas"))
tarea3_matematicas= int(input("Ingrese la nota de la tarea 3 de matematicas"))
promedio_Tareas= (tarea1_matematicas+tarea2_matematicas+tarea3_matematicas)/3
examen= int(input("Ingrese la nota del examen de matematicas"))
nota_final_matematicas= int((examen*0.9)+(promedio_Tareas*0.10))

tarea1_fisica= int(input("Ingrese la nota de la tarea 1 de fisica"))
tarea2_fisica= int(input("Ingrese la nota de la tarea 2 de fisica"))
promedio_Tareas= (tarea1_fisica+tarea2_fisica)/2
examen= int(input("Ingrese la nota del examen de fisica"))
nota_final_fisica= int((examen*0.8)+(promedio_Tareas*0.2))

tarea1_quimica= int(input("Ingrese la nota de la tarea 1 de quimica"))
tarea2_quimica= int(input("Ingrese la nota de la tarea 2 de quimica"))
tarea3_quimica= int(input("Ingrese la nota de la tarea 3 de quimica"))
promedio_Tareas= (tarea1_quimica+tarea2_quimica+tarea3_quimica)/3
examen= int(input("Ingrese la nota del examen de quimica"))
nota_final_quimica= int((examen*0.85)+(promedio_Tareas*0.15))

nota_final=int(nota_final_matematicas+nota_final_fisica+nota_final_quimica)/3

print(f'El promedio general de calificación es {nota_final}\nEl promedio general de calificación de matematicas es {nota_final_matematicas}\nEl promedio general de calificación de fisica es {nota_final_fisica}\ny El promedio general de calificación de quimica es {nota_final_quimica}')

# 39. Realizar un algoritmo que permita solucionar y mostrar por pantalla la siguiente ecuación: T= r3/y *w5 Donde: r=c2+b2* a2 w=20,457 y= w+c3+b2 se deben leer los valores de a, b, c.

a=int(input("Ingrese el valor de a"))
b=int(input("Ingrese el valor de b"))
c=int(input("Ingrese el valor de c"))
r=c*2+b*2*a*2
w=20.457
y= w+c*3+b*2
T= r*3/y*w*5
print(f'el valor de T es {T}')

# 40. El Nacional juega tres partidos en un mes y gana el 20% de lo recolectado por venta de boletería en el primer partido; el 30 % en el segundo partido y el 40 % en el tercer partido. Muestre, Cuánto es el recaudo total en el mes? y cuánto gana el equipo en el mes?.

venta_primer_partido= int(input("Ingrese el valor total vendido en el primer partido"))
venta_segundo_partido= int(input("Ingrese el valor total vendido en el segundo partido"))
venta_tercer_partido= int(input("Ingrese el valor total vendido en el tercer partido"))

comisión_primer_partido=venta_primer_partido*0.2
comisión_segundo_partido=venta_segundo_partido*0.3
comisión_tercer_partido=venta_tercer_partido*0.4

total_venta=venta_primer_partido+venta_segundo_partido+venta_tercer_partido
total_comisión=comisión_primer_partido+comisión_segundo_partido+comisión_tercer_partido

print(f'El total vendido en el mes fue {total_venta} y el total comisionado en el mes fue {total_comisión}')

# 41. Escriba un algoritmo que muestre el área de un rombo.

D = int(input("Ingrese la diagonal mayor"))
d = int(input("Ingrese la diagonal menos"))
area_rombo= (D*d)/2
print(f'El area del rombo es {area_rombo}')

# 42.Elaborar un algoritmo que permita leer valores de A y B e imprima y,z,w

a=int(input("Ingrese el valor de a"))
b=int(input("Ingrese el valor de b"))

y= 3*a*a*b*b*(2*a)**1/2
z= 12*a/b
w= 4*((2**a*a)**1/2)*(3*a*a*b*b - ((2*a)**1/2))

print(f'el valor de y es {y}\nel valor de z es {z}\ny el valor de w es {w}')

# 43. Elaborar un algoritmo que permita leer los valores para x,y,z y w e imprima el # valor de F
x=int(input("Ingrese el valor de x"))
y=int(input("Ingrese el valor de y"))
z=int(input("Ingrese el valor de z"))
w=int(input("Ingrese el valor de w"))

F= ((4*x*x*y*y*((2*z*w)*1/2))**2)/4*x/b

print(f'el valor de F es {F}')

# 44. Elaborar un algoritmo que lea el radio de una esfera y calcule el volumen y el area

import math
r=int(input("Ingrese el valor del radio de la esfera"))
volumen=(4*math.pi*r**3)/3
area=math.pi*r**2

print(f'el volumen de la esfera es {volumen} y el area es {area}')

# 45. Elaborar un algoritmo que imprima Z
import math

z=(1/(2*math.pi)**1/2)**math.e

print(f'el valor de z es {z}')

# 46.Realizar un algoritmo que permita obtener el valor de c y f, a partir de las siguientes ecuaciones

a=int(input("Ingrese el valor de a"))
x=int(input("Ingrese el valor de x"))
b=int(input("Ingrese el valor de b"))
y=int(input("Ingrese el valor de y"))
d=int(input("Ingrese el valor de d"))
e=int(input("Ingrese el valor de e"))

c=a*x+b*y
f=d*x+e*y

print(f'el valor de c es {c} y el valor de f es {f}')

# 47. Escribir un programa para convertir una medida dada en pies a sus equivalentes en yarda. pulgadas, centimetros y metros

pies= int(input("Ingrese la medida en pies"))
conversion_yarda= pies/3
conversion_pulgadas= pies/12
conversion_centimetro= conversion_pulgadas*2.54
conversion_metros= conversion_centimetro/100


print (f'la medida de {pies} pies en yarda es {conversion_yarda}\nEn pulgadas es {conversion_pulgadas}\nEn centimentros es {conversion_centimetro}\nEn metros es {conversion_metros}')

# 48.Los ingenieros de sistemas Lidin y Tidin han sido contratados por la empresa "casinos asociados" para realizar una aplicación que permita determinar el valor a pagar a cada empleado por trabajar en su casino. Cada empleado que labora en su casino tiene un nombre, el valor de la hora u el número de horas trabajadas. Cada trabajador tienen un descuento del 7% sobre el salario bruto, determinar el salario neto a paga

nombre= input("ingrese el nombre del empleado")
valor_hora= int(input("Ingrese el valor de la hora laborada"))
numero_horas= int(input("Ingrese la cantidad de horas trabajadas"))
sueldo_base=valor_hora*numero_horas
sueldo_neto=sueldo_base-(sueldo_base*0.07)
print(f'El sueldo neto del trabajador {nombre} es de {sueldo_neto}')

# 49. Construya un programa tal, que dados los datos enteros de a y b, escriba el resultado de la siguiente expresión: A= (a+b)**2

a=int(input("Ingrese el valor de a"))
b=int(input("Ingrese el valor de b"))

A=(a+b)**2

print(f'el valor de A es {A}')

# 50. Realizar un algoritmo que calcule la edad de una persona
from datetime import datetime
from dateutil.relativedelta import relativedelta


anio= int(input("Ingrese el año de nacimiento"))
mes= int(input("Ingrese el mes de nacimiento"))
dia= int(input("Ingrese el día de nacimiento"))

edad = relativedelta(datetime.now(), datetime(anio, mes, dia))
print(f"{edad.years} años, {edad.months} meses y {edad.days} días")

# 51. Elabore un programa en Python que lea una temperatura en grados Celsius, la convierta a grados Kelvin y muestre el resultado con un mensaje bien explicativo.No use aproximaciones

tc=float(input("ingrese la temperatura en grados celsius"))
tk=tc+273.15
print(f'La temperatura de {tc} a grados kelvin es {tk}')

# 52. Elabore un programa en Python que lea un entero de tres dígitos y produzca como salida los dígitos del número leído con su correspondiente mensaje. Por ejemplo, si el número leído es 271, la salida deberá ser (sin texto adicional):
# 2
# 7
# 1

numero=str(input("ingrese un numero entero de 3 digitos "))
print(numero[0])
print(numero[1])
print(numero[2])

# 53. Elabore programa en Python que lea dos números enteros y que imprima la suma, resta, multiplicación, división y módulo del primero por el segundo.

n1=int(input("Ingrese el primer numero entero "))
n2=int(input("Ingrese el segundo numero entero "))
suma=n1+n2
resta=n1-n2
multiplicacion=n1*n2
division=n1/n2
modulo=n1%n2

print(f'{suma}\n{resta}\n{multiplicacion}\n{division}\n{modulo}')

# 54.Elabore programa en Python que imprima la suma de los números enteros de -200 hasta 600


i=1
suma=0

for i in range(-200,600+1):
    print(i)
    suma+=i
print(f'La suma de los numeros enteros desde -200 hasta 600 es {suma}')





