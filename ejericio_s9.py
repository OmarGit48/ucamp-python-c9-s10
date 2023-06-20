# Utilizar al menos dos funciones
# Preguntar ucanots alumnos s eregistraran, en caso de no registrar una cantidad se asume seran 3 alumnos
# Preguntara el nombre y 2 calificaciones
# Mostrar el nombre en pantalla con inicial Mayuscula y promedio
# Al finalizar el preograma se mostrara una lista con el nombre de casa alumnoy sus calificaciones

def captura_alumnos(numero = 3):
    '''
    Registra alumnos y dos calificaciones
    Recibe como parametro la cantida de alumnos a registrar
    si no se especifica el numero de alumnos, se resitraran 3

    '''
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f'{i+1},- Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificacion {nombre}: '))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre, calificacion1, calificacion2)
    print('La calificaion de loS alumnos son:', lista_alumnos)
        
def promedio (nombre, calificacion1, calificacion2):
    '''
    Calcula el promedio de un aluno yu lo despliega en pantalla por medio de un mensaje
    Recibe como parametro el nomnre y dos calificaciones del alumno
    '''
    promedio = (calificacion1 + calificacion2) / 2
    print(f'El promedio de {nombre} es: {promedio}')
    
numero_alumnos = input('¿Cuantos alumnos desa registrar?') 

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()
    