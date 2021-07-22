"""Estadística TESLA
Tabajando sobre el archivo TSLA.csv, se solicita la siguienta información:

#1. Crear un nuevo archivo llamado 'tendencia.csv' donde se informe por fecha si el precio de las acciones subieron o bajaron
#2. Fecha y valor del volumen más alto.
#3. Fecha y valor del volumen más bajo.
#4. Fecha y valor de la apertura más baja.
#5. Fecha y valor del cierre más alto.
"""

import csv

def solucion():
    leer_csv = open("TSLA.csv", "r") #Importando el archivo
    tesla = csv.reader(leer_csv) #Se va a leer el archivo con el método reader
    list_tesla = []
    for i in tesla:
        list_tesla.append(i)
    leer_csv.close()

    list_date, list_volumen, list_open, list_close = [], [], [], []

    # for i in list_tesla:
    #   print(i)

    for j in list_tesla[1:]:
        list_date.append(j[0])
        list_volumen.append(float(j[6]))
        list_open.append(float(j[1]))
        list_close.append(float(j[4]))

    # Cálculos
    max_vol = max(list_volumen)





# resultados= solucion()