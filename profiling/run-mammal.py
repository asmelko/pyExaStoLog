import exastolog

model = exastolog.Model("../notebooks/model_files/mammalian_cc.bnet")
sim = exastolog.Simulation(
    model, 
    ['CycE','CycA','CycB','Cdh1','Rb_b1','Rb_b2','p27_b1','p27_b2'], 
    [0, 0, 0, 1, 1, 1, 1, 1]
)
sim.get_last_states_probtraj()
