"""Realizar una calculadora en Python de cadenas de bits con tres
operaciones básicas: operación AND, operación OR, operación XOR,
teniendo en cuenta la siguiente tabla de verdad"""

def calculadora(bits1, bits2, OP):
    
    
    #PROGRAMA ACÁ LA SOLUCIÓN
    a= str(bits1)
    b= str(bits2)
    resultado=""
    
    
    for a, b in zip(bits1, bits2):
        if OP == "OR":
            if a == "0" and b == "0":
                resultado+="0"
            else:
                resultado+="1"
        if OP == "AND":
            if a == "1" and b == "1":
                resultado+="1"
            else:
                resultado+="0"
        if OP == "XOR":
            if a == "1" and b == "1" or a == "0" and b == "0":
                resultado+="0"
            else:
                resultado+="1"
                
    
                
    return resultado

print(calculadora('1100110', '1110111', "AND"))


num1=[1,1,5,1]
num2=[1,0,0,1]
acumulador=[]

for n1,n2 in zip(num1,num2):
    if n1==1 and n2==1:
        acumulador.append(5)
    else:
        acumulador.append(0)
    
print(acumulador)



 

