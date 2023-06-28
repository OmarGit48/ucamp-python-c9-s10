

import random
import matplotlib.pyplot as plt

def galton_simulation(levels, bolls):
    '''
    definition the funtion for the simulation
    '''
    columns = [0] * (levels + 1)
    '''for the numbers of columns to feel'''
    for _ in range(bolls):
        position = 6  # star tu feel in the midle of the columns
        for levels in range(levels):
            direction = random.choice([-1, 1]) #choice left (-1) or right (1) direction
            position += direction
        columns[position] += 1
        
    return columns

def grafic_results(columns):
    '''grafic de columns with de bolls'''
    plt.bar(range(len(columns)), columns)
    plt.xlabel('Columns')
    plt.ylabel('Number of bolls')
    plt.title('Galton Bell Simulation')
    plt.show()
    '''this is te grafic where X line is the columns and the Y line is the numbers of bolls'''
levels = 12  # this is the numbe of levels(star on 0 then te number of columns is 13)
bolls = 3000  # This is the number of bolls

result = galton_simulation(levels, bolls)
grafic_results(result)


