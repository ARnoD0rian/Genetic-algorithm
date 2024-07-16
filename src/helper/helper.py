from algorithm.population import Population
from algorithm.creators import Population_creator
import random

#сохранение и использование функции
class Func:
    def __init__(self, func: str)->None:
        self.func = func
        
    def value(self, x = 0, y = 0)->float:
        return eval(self.func)

class Constants: # параметы работы алгоритма
    def __init__(self) -> None:
        self.FUNC = Func("4*(x - 2)**4 + (x - 2*y)**2")
        # константы генетического алгоритма
        self.POPULATION_SIZE = 100   # количество индивидуумов в популяции
        self.MAX_GENERATIONS = 100
        self.MUTATION_CHANCE = 0.1
        self.DELTA_MUTATION = 0.05
        self.POPULATION = Population_creator(-100, -100, 100, 100, self.POPULATION_SIZE, self.FUNC)
        self.BEST_SOLUTION = 0
        self.BEST_COORDINATE = (0, 0)
        self.populations = list()
        
    def __repr__(self) -> str:
        return f"best solution: {self.BEST_SOLUTION}, best coordinate: {self.BEST_COORDINATE}"

def add_in_pop(pop_ind: list, population: Population): #добавление индивидов в массив всех индивидов всех поколений
    for individ in population:
        pop_ind.append(individ.clone())
    return pop_ind