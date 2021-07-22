import pandas as pd

devs1 = pd.read_json("io_pandas.json")  #Traer el archivo json en modo lectura
print(devs1)

"""     
    cc   nombre  salario  years
0  1540     Luis  2500000      5
1  4521     Lola  2500000      6
2  1236  Ricardo  2500000      8
3  7896  Armando  2500000     10
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     25
6  1415   Lorena  2500000     15 """

devs2 = pd.read_csv("io_pandas.csv") #Traer el archivo csv en modo lectura 
print(devs2)

"""     
    cc   nombre  salario  years
0  1540     Luis  2500000      5
1  4521     Lola  2500000      6
2  1236  Ricardo  2500000      8
3  7896  Armando  2500000     10
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     25
6  1415   Lorena  2500000     15 """

#Ambos archivos se ven de la misma forma, sin embargo al abrir el archivo de manera individual se ve totalmente diferente; Dicho proceso lo podemos llamar CAJA NEGRA. Toma sus datos y los coloca en un dataFrame.

devs1 = pd.read_json("io_pandas.json")
print(devs1["nombre"]) #Se imprime ahora una SERIE con única columna

"""
0       Luis
1       Lola
2    Ricardo
3    Armando
4    Rodrigo
5     Manuel
6     Lorena
Name: nombre, dtype: object"""

print(devs1[["nombre","salario"]]) #Se imprime ahora una LISTA


print(devs1.index)  #Se imprime  los indices
"""Int64Index([0, 1, 2, 3, 4, 5, 6], dtype='int64')"""

print(devs1.columns) #Se imprime  las columnas
"""Index(['cc', 'nombre', 'salario', 'years'], dtype='object')"""

print(devs1.loc[4]) #Se imprime la serie de el indice número 4
"""
cc            1010
nombre     Rodrigo
salario    2500000
years           15
Name: 4, dtype: object"""

print(devs1.loc[[4,5]]) #Se imprime la serie de el indice número 4 y 5
"""
     cc   nombre  salario  years
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     25"""





#********************************************************************************************************************

