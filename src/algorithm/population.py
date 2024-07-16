from algorithm.individual import Individual

class Population(list): # класса популяции, наследуется от списка
    def __init__(self, *args):
        super().__init__(*args)
        
    def crossing(self, parents: tuple, func)->Individual: #кроссинговер
        
        parent_1, parent_2 = parents
        child = Individual((parent_1.x + parent_2.x) / 2, (parent_1.y + parent_2.y) / 2) # создается индивид нового поколения со среднеарифметическими параметрами родителей.
        child.calculation_fitness(func)
        
        return child