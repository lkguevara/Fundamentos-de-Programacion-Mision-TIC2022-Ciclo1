#LISTAS

"""Las listas se tratan de un tipo compuesto de dato que puede almacenar distintos valores (llamados ítems o elementos) ordenados entre [ ] y separados con comas"""

nombres = ["Jorge", "Jose", "Ricardo", "Manuel"]
print(nombres)

nombres.append("Mario") #Agrega un elemento al final de la lista
print(nombres)

print(nombres.count("Mario")) #Número de ocurrencias del dato

nombres.pop(1) #Elimina un elemento de la lista, si se coloca parametro elimina cierto elemento y sin parametro elimina el último
print(nombres)

nombres.remove("Ricardo") #Elimina un elemento especifico de la lista
print(nombres)

nombres.sort() #Se ordena de menor a mayor
print(nombres)

nombres.reverse() #Se ordena de mayor a menor
print(nombres)

#RECORRER ELEMENTOS
#RECORRIDO_TOTAL: va de principio a fin

numeros = [54,5,25,85,12,35,74,53]

for numero in numeros:
    if numero % 2 ==0:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} no es par')
    numero+=1

#RECORRIDO_PARCIAL: Al momento de encontrar el dato se detiene

numeros = [54,5,25,85,12,35,74,53]

def numeroMayor():
    for numero in numeros:
        if numero > 6*9:
            return numero

print(numeroMayor())


#Ejemplo 1 En una lista dada, calcular el área y añadir dicho número

lista= [[3,2],[5,7],[8,9]]
print()
print(lista)

for i in range(len(lista)):
    area =lista[i][0]*lista[i][1]
    lista[i].append(area)
print(lista)








