import random
class Genetic():
    def __init__(self,problem,generation_population=6,pc=25,pm=10, *args, **kwargs):
        self.problem = problem
        self.generation_population = generation_population
        self.pc = 25
        self.pm = 10

    def solve(self, *args, **kwargs):
        #initializtion
        chromosomes = [chromosome for chromosome in self.problem.initial_state()]
        ideal_situtaion = False
        while not ideal_situtaion:
            #Evaluation
            evaluated = [self.problem.heuristic(eval_num) for eval_num in chromosomes]
            #Selection
            fitness = [1/(1+eval_num) for eval_num in evaluated]
            total = sum(fitness)
            probability = [fitness_item/total for fitness_item in fitness]
            cumulative_probability = [sum(probability[:i]) for i in range(1,self.generation_population+1)]
            random_roulette_wheel = [random.random() for i in range(self.generation_population)]
            newChromosome = [list(filter(lambda chromosome: chromosome > i, chromosomes))[0] for i in random_roulette_wheel]
            chromosomes = newChromosome[:]
            #Crossover
            crossover_items = []
            for chromosome_number in range(self.generation_population):
                if random.random() < self.pc:
                    crossover_items.append(chromosome_number)
            number_of_crossovers = len(crossover_items)
            crossovered_chromosomes = []
            for index,chromosome_number in enumerate(crossover_items):
                #Below line has to be changed. Because we don't know of the size of chromosomes - here I have consider it 3
                crossover_point = random.randint(1,3)
                crossovered_chromosomes.append(chromosome_number,chromosomes[chromosome_number][:crossover_point]+chromosomes[crossover_items[number_of_crossovers-index]][crossover_point:])
            for index,new_ch in crossovered_chromosomes:
                chromosomes[index] = new_ch
            #Mutation
            
