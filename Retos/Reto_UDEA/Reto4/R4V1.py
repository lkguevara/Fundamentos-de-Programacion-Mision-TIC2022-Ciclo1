def actualizar_estado_pestana(operaciones_usuario, pagina_default):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    pila_atras=[]
    pila_adelante=[]
    pagina_actual=pagina_default
    
    
    for acciones in operaciones_usuario:
        
        if acciones ==  "atras":
            pila_adelante.append(pagina_actual)
            pagina_actual=pila_atras.pop()
        elif acciones==  "adelante":
            pila_atras.append(pagina_actual)
            pagina_actual=pila_adelante.pop()
        elif acciones == pagina_actual:
            None
        else: 
            pila_atras.append(pagina_actual)
            pagina_actual=acciones
            pila_adelante=[]
            
            
            
            
            
    return pila_atras, pagina_actual, pila_adelante
actualizar_estado_pestana("twitter,udea,facebook", "google")