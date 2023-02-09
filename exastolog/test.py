from Model import Model
from Simulation import Simulation
from os.path import dirname, join

        
model = Model(join(dirname(__file__), "../notebooks/model_files/toy3.bnet"))
simulation = Simulation(model, ['A','B'], [0, 0])
result = simulation.get_last_states_probtraj()
print(result)