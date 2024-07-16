from helper.helper import Constants, Func, Population_creator
from algorithm.algorithm import algorithm
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring
import matplotlib.pyplot as plt
import sys


class GUI:
    def __init__(self) -> None:
        
        self.constants = Constants()
        
        self.root = tk.Tk()
        self.root.title("генетический алгоритм")
        self.root.geometry('400x520')
        self.root['background'] = "gray"
        self.root.resizable(False, False)
        
        self.style_frame = ttk.Style()
        self.style_frame.configure("Style.TFrame", background = "gray")
        self.style_check_button = ttk.Style()
        self.style_check_button.configure("TCheckbutton", font=("Arial", 12), background="black", foreground = "black")
        self.style_button = ttk.Style()
        self.style_button.configure("TButton", font=("Arial", 18), background="black", foreground = "black", padding=(10,10,10,10))
        self.style_mini_label = ttk.Style()
        self.style_mini_label.configure("Mini.TLabel", font=("Arial", 12), padding = 5, foreground="black", background="gray")
        self.style_label = ttk.Style()
        self.style_label.configure("TLabel", font=("Arial", 14), padding = 5, foreground="white", background="gray")
        self.style_label_top = ttk.Style()
        self.style_label_top.configure("Top.TLabel", font=("Arial", 18), padding = 10, foreground="white", background="gray")
        
        self.main_menu = tk.Menu()
        self.main_menu.add_cascade(label="сохранить", command=self.safe_paremetres)
        self.main_menu.add_cascade(label="запустить", command=self.start_algoritm)
        self.main_menu.add_cascade(label="показать последния поколения", command=self.show)
        self.main_menu.add_cascade(label="выход", command=sys.exit)
        
        self.input_Frame = ttk.Frame(self.root, style="Style.TFrame")
        
        self.information_input_Label = ttk.Label(self.input_Frame, text="Входные данные", style="Top.TLabel") 
        self.information_input_Label.grid(row=0, column=0, columnspan=2)
        
        self.function_Label = ttk.Label(self.input_Frame, text="функция: ", style="Mini.TLabel")
        self.function_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.function_Entry.insert('end', "4*(x-2)**4 + (x-2*y)**2")
        self.function_Label.grid(column=0, row=1)
        self.function_Entry.grid(column=1, row=1)
        
        self.mutation_Label = ttk.Label(self.input_Frame, text="вероятность мутации (от 0 до 1): ", style="Mini.TLabel")
        self.mutation_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.mutation_Entry.insert('end', "0.1")
        self.mutation_Label.grid(column=0, row=2)
        self.mutation_Entry.grid(column=1, row=2)
        
        self.delta_Label = ttk.Label(self.input_Frame, text="коеффициент мутации: ", style="Mini.TLabel")
        self.delta_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.delta_Entry.insert('end', "0.05")
        self.delta_Label.grid(column=0, row=3)
        self.delta_Entry.grid(column=1, row=3)

        self.max_Label = ttk.Label(self.input_Frame, text="максимальное значение гена: ", style="Mini.TLabel")
        self.max_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.max_Entry.insert('end', "100")
        self.max_Label.grid(column=0, row=4)
        self.max_Entry.grid(column=1, row=4)
        
        self.min_Label = ttk.Label(self.input_Frame, text="минимальное значение гена: ", style="Mini.TLabel")
        self.min_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.min_Entry.insert('end', "-100")
        self.min_Label.grid(column=0, row=4)
        self.min_Entry.grid(column=1, row=4)
        
        self.size_population_Label = ttk.Label(self.input_Frame, text="размер популяции: ", style="Mini.TLabel")
        self.size_population_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.size_population_Entry.insert('end', "100")
        self.size_population_Label.grid(column=0, row=5)
        self.size_population_Entry.grid(column=1, row=5)

        self.size_generation_Label = ttk.Label(self.input_Frame, text="количество поколений: ", style="Mini.TLabel")
        self.size_generation_Entry = ttk.Entry(self.input_Frame, justify="center", width=20)
        self.size_generation_Entry.insert('end', "100")
        self.size_generation_Label.grid(column=0, row=6)
        self.size_generation_Entry.grid(column=1, row=6)
        
        self.input_Frame.grid(row=0, column=0)
        
        self.table_Frame = ttk.Frame(self.root, style="Style.TFrame", padding=10)
        self.table_Frame.grid(row=2, column=0, columnspan=2)
        
        self.Scrollbar = ttk.Scrollbar(self.table_Frame)
        self.Scrollbar.grid(row=0, column=2, sticky='ns')
        
        self.Table = ttk.Treeview(self.table_Frame, yscrollcommand=self.Scrollbar.set)
        self.Table['columns'] = ('Результат', 'Ген X', 'Ген Y')
        
        self.Table.heading('#0', text='Номер')
        self.Table.heading('Результат', text='Результат')
        self.Table.heading('Ген X', text='Ген X')
        self.Table.heading('Ген Y', text='Ген Y')
        self.Table.column('#0', width=50)
        self.Table.column('#1', width=110)
        self.Table.column('#2', width=105)
        self.Table.column('#3', width=105)

        self.Scrollbar.config(command=self.Table.yview)
        
        self.Table.grid(row=0, column=0, columnspan=2, sticky='nsew')
        
        self.solution_Frame = ttk.Frame(self.root, style="Style.TFrame")
        
        self.best_solution_Label = ttk.Label(self.solution_Frame, text=f"лучшее решение={self.constants.BEST_SOLUTION} при x={self.constants.BEST_COORDINATE[0]}, y={self.constants.BEST_COORDINATE[1]}", style="TLabel")
        self.best_solution_Label.grid(row=1, column=0)
        
        self.solution_Frame.grid(row=1, column=0)
        
        self.root.config(menu=self.main_menu)
    
    def start(self):
        self.root.mainloop()
    
    def start_algoritm(self):
        self.constants = algorithm(self.constants)
        self.best_solution_Label.config(text=f"лучшее решение={self.constants.BEST_SOLUTION} при x={self.constants.BEST_COORDINATE[0]}, y={self.constants.BEST_COORDINATE[1]}") 
    
    def safe_paremetres(self):
        self.constants.FUNC = Func(self.function_Entry.get())
        self.constants.MUTATION_CHANCE = float(self.mutation_Entry.get())
        self.constants.DELTA_MUTATION = float(self.delta_Entry.get())
        self.constants.POPULATION_SIZE = int(self.size_population_Entry.get())
        self.constants.MAX_GENERATIONS = int(self.size_generation_Entry.get())
        self.constants.POPULATION = Population_creator(float(self.min_Entry.get()), float(self.min_Entry.get()), float(self.max_Entry.get()), float(self.max_Entry.get()), self.constants.POPULATION_SIZE, self.constants.FUNC)
        self.constants.populations.clear()
        
    def show(self):
        N = int(askstring("количество поколений", "Введите количество поколений"))
        self.show_image(N, self.constants.populations)
    
    def show_image(self, N:int, populations):
        
        if N * self.constants.POPULATION_SIZE > len(populations):
            showerror(title="ошибка", message="вы не создали столько поколений")
            return
        
        population = [populations[i] for i in range(len(populations) - 1, len(populations) - N * self.constants.POPULATION_SIZE - 1, -1)]
        
        for i in range(len(self.Table.get_children())):
            self.Table.delete(self.Table.get_children()[0])
        
        for i in range(len(population)):
            self.Table.insert("", "end", text=f"{i + 1}", values=(round(population[i].fitness, 3), round(population[i].x, 3), round(population[i].y, 3)))
        
        x = list()
        y = list()
        for individ in population:
            ind = individ.clone()
            x.append(ind.x)
            y.append(ind.y)

        plt.clf()   
        plt.plot(x, y, 'go')
        plt.xlabel("x")
        plt.ylabel("Y")
        plt.show()