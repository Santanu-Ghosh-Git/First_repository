import random

def sphere_function(chromosome):
    return sum(gene ** 2 for gene in chromosome)

def create_chromosome(bounds):
    return [random.uniform(b[0], b[1]) for b in bounds]

def mutate(chromosome, bounds, mutation_rate=0.1):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.uniform(bounds[i][0], bounds[i][1])
    return chromosome

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def select(population, fitnesses, num_parents):
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1])
    return [ind for ind, _ in sorted_pop[:num_parents]]

def genetic_algorithm(bounds, pop_size=50, generations=100, mutation_rate=0.1, crossover_rate=0.8):
    dim = len(bounds)
    population = [create_chromosome(bounds) for _ in range(pop_size)]

    for gen in range(generations):
        fitnesses = [sphere_function(ind) for ind in population]
        best_index = fitnesses.index(min(fitnesses))
        print(f"Generation {gen+1}, Best Fitness: {fitnesses[best_index]:.6f}")

        # Selection
        parents = select(population, fitnesses, pop_size // 2)

        # Crossover
        next_gen = []
        while len(next_gen) < pop_size:
            if random.random() < crossover_rate:
                parent1, parent2 = random.sample(parents, 2)
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = random.sample(parents, 2)
            next_gen.extend([child1, child2])

        # Mutation
        population = [mutate(ind, bounds, mutation_rate) for ind in next_gen[:pop_size]]

    # Final result
    fitnesses = [sphere_function(ind) for ind in population]
    best_index = fitnesses.index(min(fitnesses))
    return population[best_index], fitnesses[best_index]

# Example usage
if __name__ == "__main__":
    dim = 2
    bounds = [(-10, 10)] * dim
    best_solution, best_fitness = genetic_algorithm(bounds, generations=50)
    print(f"\nBest Solution: {best_solution}")
    print(f"Best Fitness: {best_fitness}")
