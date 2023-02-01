import exastolog

model = exastolog.Model("../notebooks/model_files/EMT_cohen_ModNet.bnet")
sim = exastolog.Simulation(
    model, 
    ['ECMicroenv','DNAdamage','Metastasis','Migration','Invasion','EMT','Apoptosis','Notch_pthw','p53'], 
    [1, 1, 0, 0, 0, 0, 0, 1, 0]
)
sim.get_last_states_probtraj()
