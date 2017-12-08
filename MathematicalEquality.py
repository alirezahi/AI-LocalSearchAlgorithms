import random

class Problem():
    def initial_state(self):
        return [random.randint(0,30) for i in range(4)]

    def rand_gen(self, gen_num=None):
        return random.randint(0,30)

    def heuristic(self, state):
        heuristic_result = 0
        heuristic_result = state[0] + 2*state[1] + 3*state[2] + 4*state[3] - 40
        return heuristic_result

    def is_goal(self, state):
        return self.heuristic(state) == 0


from Genetic import *
p = Problem()
a = Genetic(p)
a.solve()
