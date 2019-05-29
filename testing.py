import gaga as ga

genes = {'x':(-2, 2),
        'y':(-1, 3)}

def evaluate(individual):

    a = 1
    b = 100

    x = individual.genes['x']
    y = individual.genes['y']

    individual.fitness_score = (pow(a - x, 2) + b * pow(y - pow(x, 2), 2))

sim = ga.ga(genes, evaluate, results_folder = 'demos/demo-rosenbrock-pycharm')
sim.run_simulation(seed=0)

sim.results.plot_fitness()
sim.results.print_best()
sim.results.animate('x', 'y', optimum = [1, 1], fmax = 20)