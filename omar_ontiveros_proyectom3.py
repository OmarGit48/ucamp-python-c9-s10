import random
import matplotlib.pyplot as plt

def galton_simulator(rows, balls):
    ''' define funtion for the Galton Bell code'''
    slots = [0] * rows  # start with parameters in 0
    
    for _ in range(balls):
        position = num_rows // 2  # sgtar in de midle
        
        for _ in range(rows):
            direction = random.choice([-1, 1])  # choice left or right
            
            # move the position de balls 
            position += direction
            if position > 11:
                position = 11
            elif position < 0:
                position = 0
          
        slots[position] += 1  # fill the slots of balls
    
    return slots    
# historgram parameters and configuration
def plot_distribution(slots):
    x = range(len(slots))
    y = slots
    plt.bar(x, y)
    plt.xlabel('Compartimento')
    plt.ylabel('Cantidad de bolas')
    plt.title('Distribución de la Campana de Galton')
    plt.show()


num_rows = 12
num_balls = 3000

# execute
distribution = galton_simulator(num_rows, num_balls)

# grafic the results of distribution
plot_distribution(distribution)