#OPEN(file_name,mode)

"""Los modos que se pueden encontrar son:
-r: por defecto abre un archivo en modo lectura
-a: abre un archivo en modo append para poder agregar datos al final
-w: abre un archivo en modo escritura
-a+: abre un archivo en modo update para agregar datos al final de este, leer el archivo y crear el archivo si no existe.
"""

file_readed = open("info.txt", "a") #Abre el archivo en modo append
file_readed.write("\nHola mundo") #Escribir en el archivo
file_readed.close() #Se cierra el string

"Al ejecutar en la consola 'py manejo_archivos.py' se me creará el archivo txt"

import pandas as pd

data_frame=pd.read_csv("io_pandas.csv")
print(data_frame)

"""
     cc   nombre  salario  years
0  1540     Luis  2500000      5
1  4521     Lola  2500000      6
2  1236  Ricardo  2500000      8
3  7896  Armando  2500000     10
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     25
6  1415   Lorena  2500000     15"""

nombre_columna = "salario"
print(data_frame[nombre_columna])

"""
0    2500000
1    2500000
2    2500000
3    2500000
4    2500000
5    2500000
6    2500000
Name: salario, dtype: int64"""

columnas = ["cc","years"]
print(data_frame[columnas])

"""
   cc  years
0  1540      5
1  4521      6
2  1236      8
3  7896     10
4  1010     15
5  1212     25
6  1415     15"""


#Funcion .loc



print(data_frame.loc[3])

"""cc            7896
nombre     Armando
salario    2500000
years           10
Name: 3, dtype: object"""

print(data_frame.loc[3, "nombre"])
"""Name: 3, dtype: object
Armando"""

print(data_frame.loc[3:5])
"""     
    cc   nombre   salario   years
3  7896  Armando  2500000     10
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     2"""

print(data_frame.loc[data_frame["salario"] > 1500000]) #Aplicando una condición

# print(data_frame.loc[data_frame["salario"] > 1500000 and data_frame["years"]>3])  #Lanza un error

palabra = "uis"
print(data_frame.loc[lambda dev: dev ["salario"] > 1500000 ])

#print(data_frame.loc[lambda dev: palabra in dev ["nombre"]]) #Lanza un error
print(data_frame.loc[lambda dev: dev ["nombre"].str.contains(palabra)]) #De esta forma se pueden operar
"""     
    cc   nombre     salario      years
0  1540   Luis      2500000      5"""

#Función .drop()
"""Elimine filas o columnas especificando los nombres de las etiquetas y el eje correspondiente, o especificando directamente el índice o los nombres de las columnas"""

