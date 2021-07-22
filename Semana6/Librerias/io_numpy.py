#LIBRERIA NUMPY

"""NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.

Incorpora una nueva clase de objetos llamados arrays (vectores (1D) o matrices(2D y 3D)) que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación."""

#Instalación de la libreria
"""#pip install numpy
#pip install --upgrade pip"""

# importamos la librería numpy, y le damos como nombre np dentro del programa

import numpy as np

#Ahora que tenemos la librería, empecemos creando un vector de 5 elementos.

"""Para crear un array se utiliza la siguiente función de NumPy: #np.array(lista)#"""
lista=[25,12,15,66,12.5]
vector=np.array(lista)
print(vector)


#función np.arange()

"""Otra función que nos permite crear un array NumPy es numpy.arange. Al igual que la función predefinida de Python range, genera un conjunto de números entre un valor de inicio y uno final, pudiendo especificar un incremento entre los valores, pero, al contrario de lo que ocurre con range, el resultado aquí es un array NumPy"""

import numpy as np
arr2=np.arange(24).reshape(4,6) # El número 24 indica el rango de números: 0 hasta 24// el reshape(Número filas, numero de columnas) de la matriz
print(arr2)












