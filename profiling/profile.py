import exastolog
import cProfile
import pstats
from pstats import SortKey

def run():
    model = exastolog.Model("../notebooks/model_files/krasmodel15vars.bnet")
    sim = exastolog.Simulation(model, ['cc','KRAS','DSB','cell_death'], [1, 1, 1, 0])
    sim.get_last_states_probtraj()

cProfile.run("run()", "profile-stats")

p = pstats.Stats('profile-stats')

p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()