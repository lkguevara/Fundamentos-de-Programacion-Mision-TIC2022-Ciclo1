"""son una forma de crear listas de una manera elegante simplificando el código al máximo"""

"""[element for element in iterable if condition] 
Por cada elemento en una lista, se agrega ese elemento a otra lista si se cumple una condicion"""

numeros=[numero for numero in range (1, 101)]
print(numeros)

numeros_altos=[numero for numero in numeros if numero >50]
print(numeros_altos)


