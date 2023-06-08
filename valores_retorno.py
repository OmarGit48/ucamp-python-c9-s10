# def promedio (*numeros):
#     return sum(numeros)/len(numeros)

# x = promedio(4,5,6)
# print (x)

# def area(**dato): # **dato es una variable que recibe un diccionario
#     ''' Calcuña el área de una figura y l aimprime en pantallo. ''' #Docstring
    
#     # Si el diccionario tiene un aclave llamada 'figura' evalúa el calor de la clave
#     if dato['figura']=='Rectangulo':
#         return (dato['base']*dato['altura']) # Si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base' multimplicado por 'altura'
#     elif dato['figura']== 'Triangulo':
#         return (dato['base']*dato['altura']/2) # Si el valor de la clave es 'Triangulo' imprime el valor de la clave 'base' multiplicado por 'altura' dividido entre 2
#     elif dato['figura'] == 'Circulo':
#         return (3.141593*dato['radio']**2) # Si el calor de la clave es 'Circulo' imprime el valor de la clave 'radio' multiplicado por Pi elevado al cuadrado
#     else:
#         print('Figura desconocida') # Si el valor de la clave no es ninguna de las anteriores, imprime 'Figura desconocida'

# # Ejemplo d ellamada a la función
# triangulo = area(figura = 'Triangulo', base = 10, altura = 5) # llama a la función area con los parámetros 'figura'. 'base', y 'altiura'
# print(f'El area del triángulo es: {triangulo}') 
# circulo = area(figura = 'Círculo', radio = 10, color = 'Rojo') # Llama a la función area con los parámetros 'figura', 'radio', y 'color'
# print(f'El area del Círculo es: {circulo}')
# dodecagono = area(figura = 'Dodecagono', lado =10) # Lama a al función area con los parámetros 'figura', y 'lado'
# print(f'El area del Dodecagono es: {dodecagono}')

#############################################
# Recursividad de funciones en Python

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero -1)
    
print('El factorial de 0 es (0!):',factorial(0))
print('El factorial de 1 es (1!):',factorial(1))
print('El factorial de 2 es (2!):',factorial(2))