""" Dada una matriz 5x5, hallar lo siguiente: 
    1. suma_diagonal_principal.
    2. producto_diagonal_secundaria: 
    3. Módulo entre producto_diagonal_secundaria y suma_diagonal_principal.
    """
import numpy as np
def solucion(A):
    sum_diagonal_principal = 0
    
    n = A.shape[0]
   
    for i in range(n):
        sum_diagonal_principal+=A[i][i]
        
        
    prod_diagonal_secundaria=1
    j=-1    
    for i in range(n):        
        prod_diagonal_secundaria*=A[i][j]
        j-=1     
        
    resultado2_mod_resultado1=prod_diagonal_secundaria%sum_diagonal_principal

    return sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1
    
  
matriz_entrada = np.array([[73, 13,  6,  1, 29],
       [28, 72, 76, 86, 48],
       [94, 18, 32, 24, 33],
       [63, 11, 16, 69, 40],
       [38, 20, 45, 78, 61]])

dp_estudiante = solucion(matriz_entrada)[0]
ds_estudiante = solucion(matriz_entrada)[1]
ds_mod_dp_estudiante = solucion(matriz_entrada)[2]

print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")

print(f"""Suma de los elementos de la diagonal principal = {dp_estudiante}, Producto de los elementos de la diagonal secundaria = {ds_estudiante} y el modulo entre producto_diagonal_secundaria y suma_diagonal_principal es = {ds_mod_dp_estudiante}\n""")

# dp_correcto = 307
# ds_correcto = 33359744
# ds_mod_dp_correcto = 203


