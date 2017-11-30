class HillClimbing():
    def __init__(self, problem,*args, **kwargs):
        self.problem = problem
    
    def solve(start, *args, **kwargs):
        current_state = self.problem.start
        best_found = False
        attempts = 1000
        while not best_found:
            neighbour_nodes = self.problem.neighbours()
            best_neighbour_node = min(neighbour_nodes,key=lambda x:self.problem.heuristic(x))
            attempts -= 1
            if is_goal(best_neighbour_node) or attemps < 0:
                best_found = True

