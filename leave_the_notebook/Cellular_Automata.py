import random
from matplotlib import pyplot as plt

def random_string(length):
    return [random.randint(0,2) for _ in range(length)]

def neighborhoods():
    return [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1),(2,2)]

def ternary(n):
    a = [0,1,2]
    b = []
    while True:
        s = n//3
        y = n%3
        b = b+[y]
        if s == 0:
            break
        n = s
    return b

def internary(rule_number):
    in_ternary=ternary(rule_number)
    ternary_length = len(in_ternary)
    if ternary_length != 9:
        padding = 9-ternary_length
        in_ternary = in_ternary + [0]*padding
    return in_ternary

def spacetime_diagram(spacetime_field, size=12, colors=plt.cm.Greys):
    plt.figure(figsize=(size,size))
    plt.imshow(spacetime_field, cmap=colors, interpolation='nearest')
    plt.show()

    
class ECA(object):
    
    def __init__(self, initial_condition):
        self.initial = initial_condition
        self.spacetime = [initial_condition]
        self.current_configuration = initial_condition.copy()
        self._length = len(initial_condition)

        
    def evolve(self, time_steps, in_ternary):
        lookup = dict(zip(neighborhoods(), reversed(in_ternary)))
        length = len(self.initial)
        
        spacetime_field = [self.initial]
        current_configuration = self.initial.copy()

        for t in range(time_steps):
            new_configuration = []
            for i in range(length):

                neighborhood = (current_configuration[(i-1)], 
                                current_configuration[i])

                new_configuration.append(lookup[neighborhood])

            current_configuration = new_configuration
            spacetime_field.append(new_configuration)
    
        return spacetime_field

