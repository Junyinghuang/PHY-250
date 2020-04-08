import Cellular_Automata
from matplotlib import pyplot as plt

initial_conditions = Cellular_Automata.random_string(20)
field= Cellular_Automata.ECA(initial_conditions)
Cellular_Automata.spacetime_diagram(field.evolve(20,Cellular_Automata.internary(3101)),12)
plt.savefig('rule3101.pdf')