import gaga as ga

genes = {'x':(-1.5, 1.5),
        'y':(-1.5, 1.5)}

def evaluate(individual):

    #  unpack chromosome
    x = individual.genes['x']
    y = individual.genes['y']

    individual.fitness_score = pow(x, 2) + pow(y, 2)


sim = ga.ga(genes,
            evaluate,
            selection = 'roulette_wheel',
            epoch = 25,
            mutate = 0.1,

            population_size = 25)
# sim.run_simulation()
#
# sim.results.plot_fitness()
# sim.results.print_best()
# sim.results.animate('x', 'y', optimum = [0, 0])