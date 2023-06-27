
import random
import matplotlib.pyplot as plt

def simulate_gantt_chart(num_canicas, num_pisos):
    # Inicializar los pisos con 0 canicas
    pisos = [0] * num_pisos

    # Simular la caída de las canicas
    for _ in range(num_canicas):
        piso_actual = 0

        # Hacer que la canica caiga hasta llegar al último piso
        while piso_actual < num_pisos - 1:
            if random.random() < 0.5:  # 50% de probabilidad de moverse hacia izquierda
                piso_actual += 1
            else:  # 50% de probabilidad de moverse hacia derecha
                piso_actual = max(0, piso_actual - 1)

        # Incrementar el contador de canicas en el último piso alcanzado
        pisos[piso_actual] += 1

    # Dibujar el gráfico de Gantt
    # fig, ax = plt.subplots()
    # ax.bar(range(num_pisos), pisos)
    # plt.xlabel('Pisos')
    # plt.ylabel('Número de canicas')
    # plt.title('Campana de Gantt')
    # plt.grid(True)
    # plt.show()

# Ejemplo de uso
num_canicas = 3000
num_pisos = 12

simulate_gantt_chart(num_canicas, num_pisos)
