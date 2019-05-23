import pickle
import bz2
from genalg.GA import ga

genes = {'x':(-2, 2),
        'y':(-1, 3)}

def evaluate(individual):

    # constants
    a = 1
    b = 100

    #  unpack chromosome
    x = individual.CHROMOSOME['x']
    y = individual.CHROMOSOME['y']

    individual.FITNESS_SCORE = (pow(a - x, 2) + b * pow(y - pow(x, 2), 2))

sim = ga(genes, evaluate, results_folder = "demo-rosenbrock")
sim.run_simulation()
sim.results.plot_fitness()

RESULTS_FOLDER = "demo-rosenbrock/"

with bz2.BZ2File(RESULTS_FOLDER + "results_obj", 'rb') as f:
    results = pickle.load(f)


print(results.data)
print(results.__dict__.keys())
print(results.epochs)
print(results.data["genes"][0])

results.animate('x', 'y', optimum = [1, 1], inset = [0.75, 1.25, 0.75, 1.25])


results.print_best()

