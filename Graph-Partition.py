import random


class Problem():
    def __init__(self, *args, **kwargs):
        self.graph = {
            'a':{'b','c'},
            'b':{'a','c','d','e'},
            'c':{'a','f'},
            'd':{'b','f','j'},
            'e':{'b','g'},
            'f':{'c','d','i'},
            'g':{'e','h','j','k'},
            'h':{'g','k'},
            'i':{'f','j'},
            'j':{'d','i','g','l'},
            'k':{'g','h','l'},
            'l':{'j','k'}
        }

        
    def initial_state(self):
        #list of first group
        fg = random.sample(self.graph, int(len(self.graph) / 2))
        #list of second group
        sg = list(set(self.graph.keys()) - set(fg))
        return (fg,sg)

    def neighbours(self, state):
        result = []
        for first_index,first_node in enumerate(state[0]):
            for second_index,second_node in enumerate(state[1]):
                result.append((
                    list(state[0][:first_index] + [second_node]+state[0][first_index+1:]),
                    list(state[1][:second_index] + [first_node] + state[1][second_index+1:])
                ))
        return result

    def heuristic(self, state):
        heuristic_result = 0
        for first_node in self.graph:
            for second_node in self.graph[first_node]:
                if (first_node in state[0] and second_node in state[1]) or (second_node in state[0] and first_node in state[1]):
                    heuristic_result += 1
        return heuristic_result



from SimulatedAnnealing import *
p = Problem()
a = SimulatedAnnealing(p)
a.solve()
