from Model import Model
from Simulation import Simulation
from os.path import dirname, join

        
# model = Model(join(dirname(__file__), "../notebooks/model_files/toy3.bnet"))
# simulation = Simulation(model, ['A','B'], [0, 0])
# result = simulation.get_last_states_probtraj()

model = Model("../notebooks/model_files/krasmodel15vars.bnet")
sim = Simulation(model, ['cc','KRAS','DSB','cell_death'], [1, 1, 1, 0])
result = sim.get_last_states_probtraj()
print(result)