# def sumar(parametro1,parametro2):
#     """Funciòn que suma dos parametros y los imprime en pantalla"""
#     print('suma: ', parametro1 + parametro2)
    
# argumento1 = 5
# argumento2 = 7

# # Invocando a la funcion por medio de parametro variables
# sumar(argumento1, argumento2)    

# # Invocando ala funciòn por medio de parametros de valor
# sumar('mundo¡', 'Hola')

# sumar('hola')

###########################################
# Parametros opcionales

def muestra_alumno(nombre, edad = 18, sexo = 'F'):
    '''
    Es una funcion que muestra en pantalla el nomnbre, edad y el sexo de un alumno
    Recibe tres parámetros.
    1. Nombre
    2. Edad = 18
    3. Sexo = 'F'
    '''
    print(f'Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}')

# Ejecucion de función con un parametro obligatorio
muestra_alumno('Maria')

# Ejecución utilizando el parametro obligatorio y unos opcionañ
muestra_alumno('Maria', 22)

# Ejecucion de funcion con el primer y ultimo parametro
muestra_alumno('Juan', sexo = 'M')

    
    