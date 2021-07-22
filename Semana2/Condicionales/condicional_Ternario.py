#CONDICIONAL TERNARIO

"""Se trata de una cláusula if , else que se define en una sola línea y puede ser usado por ejemplo, dentro de un print()"""
#Ejemplo
hora = 4
mensaje= "hola" if hora < 6 else "Adios"
print(mensaje)

# ***************************************************************MINTIC************************************************************

#1. Crear una lista que indique si cada numero es par o impar, el resultado se guardará en nueva lista

numeros=[numero for numero in range(1,51)]

par_impar = list(map(lambda numero: f'{numero} par' if numero % 2 ==0 else f'{numero} impar' ,numeros))
print(par_impar)





