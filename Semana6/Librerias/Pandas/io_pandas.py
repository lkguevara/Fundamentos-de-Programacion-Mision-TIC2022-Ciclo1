#PANDAS
#pip install pandas

"""es una herramienta de manipulación y análisis de datos de código abierto rápida, potente, flexible y fácil de usar,
construida sobre el lenguaje de programación Python"""
#Serie: Es una lista de una dimensión
import pandas as pd

serie1=pd.Series([4,5,8])
"""
0    4      
1    5      
2    8  
"""

serie2=pd.Series({"nombre":"juan", "edad":15})
"""
nombre    juan
edad       15
"""

#Dataframe: recibe elementos o conjunto de elementos, su diferencia es que la serie recibe un valor por cada llave, el dataframe recibe un valor pero como lista. (Listas y columnas)

frame1=pd.DataFrame({"dia":[25,26,27], "mes":[3,4,5]})
"""
   dia  mes
0   25    3
1   26    4
2   27    5 """

# ********************************************************************************************************************************
#EJEMPLOS

#1. Imprimiendo un diccionario sin  pandas y con pandas
import pandas as pd

devs = [
{"cc":1540, "nombre":"Luis","salario":2500000,"years":5},
{"cc":4521, "nombre":"Lola","salario":2500000,"years":6},
{"cc":1236, "nombre":"Ricardo","salario":2500000,"years":8},
{"cc":7896, "nombre":"Armando","salario":2500000,"years":10},
{"cc":1010, "nombre":"Rodrigo","salario":2500000,"years":15},
{"cc":1212, "nombre":"Manuel","salario":2500000,"years":25},
{"cc":1415, "nombre":"Lorena","salario":2500000,"years":15}]
print(f'imprimiendo sin pandas : \n {devs}')

#2. Convirtiendo a data frames:

devs_data_frame=pd.DataFrame(devs)
print(f'imprimiendo con pandas : \n {devs_data_frame}')

"""
imprimiendo con pandas : 
      cc   nombre  salario  years
0  1540     Luis  2500000      5
1  4521     Lola  2500000      6
2  1236  Ricardo  2500000      8
3  7896  Armando  2500000     10
4  1010  Rodrigo  2500000     15
5  1212   Manuel  2500000     25
6  1415   Lorena  2500000     15"""

print(f'accediendo a un dato : \n {devs_data_frame["cc"]}')

""" 
0    1540
1    4521
2    1236
3    7896
4    1010
5    1212
6    1415
Name: cc, dtype: int64"""

#3. Pasando de diccionario a csv

"""Debe ejecutarse desde la consola con: open in integrad terminal y una vez estando ahi: py -nombre del archivo.py- """


devs_data_frame.to_csv("io_pandas.csv", index=False) # -Nombre del dataframe-to(nombre de la extensión, en este caso csv)(-nombre del nuevo archivo csv,index: corresponde a los subindices y en este caso para que no aparezcan)


#4. Pasando de diccionario a json

"""Para que el formato se vea ordenado se coloca: shift + alt + f"""

devs_data_frame.to_json("io_pandas.json")

#Index: indice de cada dataFrame
#Columns: Las columnas de cada dataFrame
#Loc: Me imprime los subindices que se requieran
