class HillClimbing():
    def __init__(self, problem, *args, **kwargs):
        self.problem = problem

    def solve(self, *args, **kwargs):
        current_state = self.problem.initial_state()
        best_found = False
        attempts = 1000
        while not best_found:
            neighbour_nodes = self.problem.neighbours(current_state)
            best_neighbour_node = min(
                neighbour_nodes, key=lambda x: self.problem.heuristic(x))
            attempts -= 1
            if self.problem.heuristic(best_neighbour_node) < self.problem.heuristic(current_state):
                current_state = best_neighbour_node
            if self.problem.is_goal(current_state) or attempts < 0:
                best_found = True
