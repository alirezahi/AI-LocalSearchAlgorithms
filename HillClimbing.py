import random

class HillClimbing():
    def __init__(self, problem, *args, **kwargs):
        self.problem = problem

    def solve(self, algorithm_type='normal',*args, **kwargs):
        current_state = self.problem.initial_state()
        best_found = False
        number_of_attempts = 1000
        attempts = number_of_attempts
        random_restart_try = 5
        random_results = []
        while not best_found:
            neighbour_nodes = self.problem.neighbours(current_state)
            if algorithm_type in ['normal','random-restart']:
                best_neighbour_node = min(neighbour_nodes, key=lambda x: self.problem.heuristic(x))
            if algorithm_type == 'stochastic':
                best_neighbour_node = random.choice(list(filter(lambda x : self.problem.heuristic(x) < self.problem.heuristic(current_state),neighbour_nodes)) or [current_state])
            if algorithm_type == 'first-choice':
                best_neighbour_node = (list(filter(lambda x: self.problem.heuristic(x) < self.problem.heuristic(current_state), neighbour_nodes)) or [current_state])[0]
            attempts -= 1
            if self.problem.heuristic(best_neighbour_node) <= self.problem.heuristic(current_state):
                current_state = best_neighbour_node
            if self.problem.is_goal(current_state) or attempts < 0:
                best_found = True
            if algorithm_type == 'random-restart':
                if attempts == 0:
                    if random_restart_try > 0:
                        attempts = number_of_attempts
                        random_restart_try -= 1
                        random_results.append([current_state,self.problem.heuristic(current_state)])
                        current_state = self.problem.initial_state()
                    else:
                        current_state = min(random_results,key=lambda x : x[1])[0]
                        best_found = True
        print(current_state)
