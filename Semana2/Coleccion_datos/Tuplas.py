#Tuplas
"""Son unas colecciones muy parecidas a las listas con la peculiaridad de que son inmutables:"""

tupla = (100,"Hola",[1,2,3],-50)
print(tupla)

"""(100, 'Hola', [1, 2, 3], -50)"""

#Indexación y slicing

print(tupla[0]) #Imprime la tupla en la posición 0
"""100"""

print(tupla[-1])
"""-50"""
print(tupla[2:])
"""[1,2,3], -50"""

print(tupla[2][-1]) #Se busca la posición 2 que es la lista y dentro de dicha lista se busca la posición -1
"""3"""


#Inmutabilidad

#tupla[0] = 50
"""---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-b45433b4cee9> in <module>()
----> 1 tupla[0] = 50
TypeError: 'tuple' object does not support item assignment"""

#Función len()
"""Igual que si fuera una lista podemos utilizarla para saber la longitud de una tupla:"""

print(len(tupla)) 
"""4"""

#Métodos integrados index()
"""Sirve para buscar un elemento y saber su posición en la tupla:"""

tupla.index(100)
"""0"""

#count()
"""Sirve para contar cuantas veces aparece un elemento en una tupla:"""


tupla.count(100)
"""1"""

#append()
"""Al ser inmutables, las tuplas no disponen de métodos para modificar su contenido:"""
tupla.append(10)
"""---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-758d195ec9d7> in <module>()
----> 1 tupla.append(10)
AttributeError: 'tuple' object has no attribute 'append'"""