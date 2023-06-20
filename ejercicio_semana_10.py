# Que solicite al usuario cierto numero de personas para agregar a un formulario.
# Que primero solicite el nimre de todas las personas que se ingresaran
# Que despues pregunte la esas de cada persona.
# Que luego pregunte el sexo de cada persona refiriendoe a ella por su nombre. 
# Si no se especifica el sexo se guardara la variable "No especifica"
# se unen lo tres datos introducidos en una tupla por persona y se imprime en la pantalla


def agregar_datos(lista, valor):
    '''
    Funcion que agrega un dato a una lista especificada
    '''
    if valor == '':
        valor = 'No especificado'
    lista.append(valor)
    return lista

nombres = []
edades = []
sexos = []

personas = int(input('¿Cuántas personas se quiere registrar? '))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i+1}: ').title()
    nombres = agregar_datos(nombres, nombre)
for i in range(personas):
    edad =input(f'Ingrese la edad de {nombres[i]}: ')
    edades = agregar_datos(edades, edad)
for i in range(personas):
    sexo = input(f'¿Cuál es el sexo de {nombres[i]}?: ')
    sexos =agregar_datos(sexos, sexo)
    
for i in zip(nombres, edades, sexos):
        print(i)
        