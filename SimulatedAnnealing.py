import random
from math import exp

class SimulatedAnnealing():
    def __init__(self, problem, *args, **kwargs):
        self.problem = problem
    
    def solve(self):
        current_state = self.problem.initial_state()
        count = 0
        local_try = 1000
        temperature = 10000
        sch = 0.99
        t_min = 1
        while temperature > t_min:
            print(current_state)
            random_neighbour = random.choice(self.problem.neighbours(current_state))
            efficiency = self.problem.heuristic(random_neighbour) - self.problem.heuristic(current_state)
            #Replace new state if it is better than older one
            if efficiency < 0:
                current_state = random_neighbour
            #Replace new state if the probability is good
            elif exp((-(efficiency))/temperature) > random.random():
                current_state = random_neighbour
            temperature *= sch
        print(current_state)
