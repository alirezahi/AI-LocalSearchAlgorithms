import random
class Problem():
    def initial_state(self):
        #a tuple that n-th item shows the place of n-th queen in the n-th column
        return tuple(random.randint(1,8) for i in range(8))

    def neighbours(self,state):
        result = []
        for index,current_place in enumerate(state):
            for new_place in list(range(1,current_place)) + list(range(current_place+1,9)):
                result.append(state[: index] +tuple([new_place]) + state[index + 1:])
        return result

    def heuristic(self,state):
        heuristic_result = 0
        #The heuristic function calculates the number of pair of queens attacking each other
        for i in range(8):
            for j in range(i+1,8):
                if abs(state[i] - state[j]) in [abs(i - j), 0]:
                    heuristic_result += 1
        return heuristic_result

    def is_goal(self,state):
        return self.heuristic(state) == 0

from HC import *
p = Problem()
a = HillClimbing(p)
a.solve()
