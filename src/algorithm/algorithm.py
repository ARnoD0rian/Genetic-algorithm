from helper.helper import Constants, add_in_pop
from algorithm.tournament import Tournament
from algorithm.population import Population
import random

def algorithm(const: Constants) -> Constants:
    population = Population(const.POPULATION)
    
    N_generation = 0
    max_pop_ind = list() #инициализация списков хранения лучшей особи в поколении и всех особей во всех поколениях
    pop_ind = list()
    max_pop_ind.append(min(population, key=lambda ind: ind.fitness))
    pop_ind = add_in_pop(pop_ind, population)
    while N_generation < const.MAX_GENERATIONS: 
        N_generation += 1
        offspring = Tournament(population, const.POPULATION_SIZE) #турнирный отбор
        
        for i in range(const.POPULATION_SIZE): #создание новой популяции
            offspring[i] = population.crossing(offspring[i], const.FUNC)
            
            if random.random() < const.MUTATION_CHANCE:
                offspring[i].mutation(const.DELTA_MUTATION)
                
        population = Population(offspring)
        pop_ind = add_in_pop(pop_ind, population)
        #add_image(N_generation, population)
        max_pop_ind.append(min(population, key=lambda ind: ind.fitness))
    
    const.POPULATION = population.copy() #копирование результатов работы алгоритма в класс Constants
    const.populations = pop_ind.copy()
    const.BEST_SOLUTION = round(max_pop_ind[-1].fitness, 3)
    const.BEST_COORDINATE = (round(max_pop_ind[-1].x, 3), round(max_pop_ind[-1].y, 3))
    const.POPULATION = add_in_pop(const.POPULATION, pop_ind)
    
    return const