# Parametros de tipo tupla, *args

# def promedio (*numeros):
#     '''
#     Recibe un sólo parámetro de tipo tupla, de valores numéricos
#     E imprime su promedio
#     '''
#     promedio = sum(numeros)/len(numeros)
#     print('El promedio es : ', promedio)
    
# promedio(4)
# promedio (4, 5, 6)
# promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)

######################################################

# def es_numero(titulo, *serie):
#     '''
#     Imprime un título
#     Verifica si el caracer ne l eparámetro de tipo tupla e sun numero o no lo es
#     '''
#     print (titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit():
#             print(f'{i} es numero')
#         else:
#             print(f'{i} no es numero')
# ##############################          
            
# # es_numero('Números', '1', '2', '3')            
# # es_numero('Letras', 'a', 'b', 'c')

# ###############################

# nombre = 'Mezcla'
# lista_varios = ['a', '2', 3, 'f', 5]
# es_numero(nombre, *lista_varios)

########################################################################################

# Parámetros tiupo diccionario **kwargs

def area(**dato): # **dato es una variable que recibe un diccionario
    ''' Calcuña el área de una figura y l aimprime en pantallo. ''' #Docstring
    
    # Si el diccionario tiene un aclave llamada 'figura' evalúa el calor de la clave
    if dato['figura']=='Rectangulo':
        print(dato['base']*dato['altura']) # Si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base' multimplicado por 'altura'
    elif dato['figura']== 'Triangulo':
        print(dato['base']*dato['altura']/2) # Si el valor de la clave es 'Triangulo' imprime el valor de la clave 'base' multiplicado por 'altura' dividido entre 2
    elif dato['figura'] == 'Circulo':
        print(3.141593*dato['radio']**2) # Si el calor de la clave es 'Circulo' imprime el valor de la clave 'radio' multiplicado por Pi elevado al cuadrado
    else:
        print('Figura desconocida') # Si el valor de la clave no es niungunda de las anteriores, im,priome 'Fiogura desconocida'
        
area(figura = 'Triangulo', base = 10, altura = 5)
area(figura = 'Circulo', radio = 10, color = 'Rojo')
area(figura = 'Dodecagono', lado =10)



        
        