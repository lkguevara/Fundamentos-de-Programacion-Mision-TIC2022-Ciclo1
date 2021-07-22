#DICCIONARIOS
"""Son junto a las listas las colecciones más utilizadas y se basan en una estructura mapeada donde cada elemento de la colección se encuentra identificado con una clave única, por lo que no puede haber dos claves iguales. En otros lenguajes se conocen como arreglos asociativos.

Los diccionarios se definen igual que los conjuntos, utilizando llaves, pero también se pueden crear vacíos con ellas:
"""

colores = {'amarillo':'yellow','azul':'blue'}
print(colores)
"""{'amarillo': 'yellow', 'azul': 'blue'}"""

#Encontrar el valor de una llave

print(colores['amarillo'])
"""yellow"""

#Mutabilidad
"""Los diccionarios son mutables, por lo que se les puede añadir elementos sobre la marcha a través de las claves:"""

colores['verde'] = 'green'
print(colores)

"""Como los diccionarios son mutables también podemos sobreescribir un valor:
"""
colores['amarillo'] = 'white'
print(colores)

# Función del()
"""Sirve para borrar un elemento del diccionario:"""

del(colores['amarillo'])
print(colores)
"""{'azul': 'blue', 'verde': 'green'}"""

# Lectura secuencial
"""Es posible utilizar iteraciones for para recorrer los elementos del diccionario:"""


edades = {'Hector':27,'Juan':45,'Maria':34}

for edad in edades:
    print(edad)

"""
Hector
Juan
Maria"""

# El método .items() 
"""nos facilita la lectura en clave y valor de los elementos. Devuelve ambos valores en cada iteración automáticamente y nos permite almacenarlos:"""

for i, valor in edades.items():
    print(i, valor)

"""
Hector 27
Juan 45
Maria 34"""


diccionario={"a":"hola", "b":"mundo"}

print(diccionario) #Imprime el diccionario
"""{'a': 'hola', 'b': 'mundo'}"""

print(list(diccionario)) #Imprime las llaves
"""['a', 'b']"""

print(list(diccionario.keys())) #Imprime las llaves
"""['a', 'b']"""

print(list(diccionario.values())) #Imprime los parametros de las llaves
"""['hola', 'mundo']"""

print("".join(list(list(diccionario.items())[1]))[2]) #Imprime letra por letra, el primer [] corresponde a la llave y el segundo al parametro de esa llave
"""u"""
# /*******************************************************************************************////////////////////////////


#SETS

#Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia a grupos y eliminación de elementos duplicados.

"""Para definir un conjunto vacío hay que llamar a su clase set (conjunto en inglés):"""

conjunto = {1,2,3,4}
conjunto.add(6)
print(conjunto)
"""{1, 2, 3, 4, 6}"""

#Colecciones desordenadas
"""Se dice que son desordenados porque gestionan automáticamente la posición de sus elementos, en lugar de conservarlos en la posición que nosotros los añadimos:"""

conjunto.add('H')
conjunto.add('A')
conjunto.add('Z')
print(conjunto)
"{1, 2, 3, 4, 'H', 6, 'Z', 'A'}"

#Pertenencia a grupos

grupo = {'Hector','Juan','Mario'}

"""Es fácil saber si un elemento se encuentra en un conjunto utilizando la sintaxis in. Se utiliza mucho para trabajar con grupos:"""
print('Hector' in grupo)
"""True"""

# Elementos únicos
"""Los conjuntos no pueden tener el mismo elemento más de una vez, se borran los duplicados automáticamente:"""
test = {'Hector','Hector','Hector'}
print(test)
"""{'Hector'}"""

#Conversiones con listas
"""Es muy útil transformar listas a conjuntos para borrar los elementos duplicados automáticamente y viceversa:"""

lista = [1,2,3,3,2,1]
print(lista)
"""[1, 2, 3, 3, 2, 1]"""

lista = list(set(lista)) #Se pasa a conjunto y así borrar los duplicados
print(lista)
"""[1, 2, 3]"""

# Conversiones con cadenas
"""Hacer esta transformación sirve para crear un conjunto con todos los caracteres de la cadena, pero sin duplicados:"""

cadena = "Al pan pan y al vino vino"
print(set(cadena))

