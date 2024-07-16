import random

#класс, который хранит параметры об индивиде
class Individual:
    
    def __init__(self, x, y) -> None:
        self.x = x #хросомы
        self.y = y
        self.fitness = 0 #значение целевой функции
        
    def clone(self): #клонирование индивида
        new_Individual = Individual(self.x, self.y)
        new_Individual.fitness = self.fitness
        return new_Individual
    
    def calculation_fitness(self, func) -> float: #расчет приспособленности для индивида
            self.fitness = func.value(self.x, self.y)
    
    def mutation(self, DELTA_MUTATION)->None: # мутация индивида
        delta_x = (random.random() * DELTA_MUTATION) * (-1)**(random.randint(0, 1))
        delta_y = (random.random() * DELTA_MUTATION) * (-1)**(random.randint(0, 1))
        self.x += delta_x
        self.y += delta_y
            
    def __repr__(self) -> str:
        return f"{self.x}, {self.y}, {self.fitness}"