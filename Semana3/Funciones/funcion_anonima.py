#Lambda parametros : instrucción
#Lambda entradas : salidas

function_lambda = lambda parametro: parametro*2

print(function_lambda(5))

"""Validar si una palabra es palindromo"""
 
def palindromo(texto):
    return texto == texto[::-1]

palindromo("oso")


#Aplicando Lambda

palindromo_lambda = lambda texto: texto.lower().replace('','') == texto[::-1].lower().replace('','')
palindromo_lambda("oso")
