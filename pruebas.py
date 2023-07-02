

#     valores = [0] * 12
# for canica in range(1, 3001):
#     indice = 5
    
#     for nivel in range(1, 13):
    #     lado = random.choice([-1, 1])
    #     if lado == 1:
            
            
    # valores[indice] += 1

# valores
############################################################
# import random
# import matplotlib.pyplot as plt

# def recorrido(num_canicas, num_niveles):
#     valores = [0] * num_niveles
    
#     for canica in range(1, num_canicas + 1):
#         indice = None
        
#         for nivel in range(1, num_niveles + 1):
#             lado = random.choice([-1, 1])
#             if lado == 1 and indice is None:
#                 indice = num_canicas // 2
#             elif lado == -1 and indice is None:
#                 indice = (num_canicas // 2) - 1
#             # que pasa si estoy en el extremo izq
#             elif indice == 0:
#                 indice = 1
#             # que pasa si estoy en el extremo der
#             elif indice == num_niveles - 1:
#                 indice = num_niveles - 2
#             else:
#                 indice = indice + lado
                
                
#         valores[indice] += 1

#     return valores
# def grafic_results(num_niveles):
#     '''grafic de columns with de bolls'''
#     plt.bar(range(len(num_niveles)), num_niveles)
#     plt.xlabel('Columns')
#     plt.ylabel('Number of bolls')
#     plt.title('Galton Bell Simulation')
#     plt.show()
    
# valores = recorrido(3000, 12)
# dibujar_histograma(valores)

#################################################################

import random
import matplotlib.pyplot as plt

def galton_simulator(rows, balls):
    slots = [0] * (rows + 1)  # Inicializar los compartimentos con ceros
    
    for _ in range(num_balls):
        position = num_rows // 2  # Comenzar en la posición central
        
        for rows in range(num_rows):
            direction = random.choice([-1, 1])  # Elegir izquierda o derecha
            
            # Mover la posición hacia la izquierda o la derecha
            position += direction
            if position >= 11:
                slots = 11
            elif position <= 0:
                slots = 0
            else:
                continue           
        slots[position] += 1  # Incrementar el contador en el compartimento final
    
    return slots    

def plot_distribution(slots):
    x = range(len(slots))
    y = slots
    plt.bar(x, y)
    plt.xlabel('Compartimento')
    plt.ylabel('Cantidad de bolas')
    plt.title('Distribución de la Campana de Galton')
    plt.show()

# Configuración del simulador
num_rows = 11
num_balls = 3000

# Ejecutar la simulación
distribution = galton_simulator(num_rows, num_balls)

# Graficar la distribución resultante
plot_distribution(distribution)



