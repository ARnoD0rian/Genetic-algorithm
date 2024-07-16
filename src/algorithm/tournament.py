from algorithm.population import Population
import random
    
def Tournament(population: Population, POPULATION_SIZE)->Population: #турнирный отбор
    
    offspring = Population()
    best_individ = min(population, key=lambda ind: ind.fitness)
    offspring.append((best_individ, best_individ))
    for _ in range(1, POPULATION_SIZE):
        
        individs = random.choices(population, k=3)
        individs.sort(key=lambda ind: ind.fitness)
        
        offspring.append((individs[0].clone(), individs[1].clone()))
        
    
    return offspring