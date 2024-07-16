from algorithm.individual import Individual
from algorithm.population import Population
import random

def Individual_creator(min_x, min_y, max_x, max_y, func)->Individual: #инициализация индивида для первой популяции
    new_Individual = Individual((max_x - min_x)* random.random() + min_x, (max_y - min_y)* random.random() + min_y)
    new_Individual.calculation_fitness(func)
    return new_Individual
    
def Population_creator(min_x, min_y, max_x, max_y, POPULATION_SIZE, func)->Population: # инициализация начальной популяции
    return Population([Individual_creator(min_x, min_y, max_x, max_y, func) for i in range(POPULATION_SIZE)])