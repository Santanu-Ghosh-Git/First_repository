import random

class Particle:
    def __init__(self, dim, bounds):
        self.position = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.best_position = list(self.position)
        self.best_value = float('inf')

    def update_velocity(self, global_best_position, w, c1, c2):
        for i in range(len(self.velocity)):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            social = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive + social

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
            # clamp position within bounds
            self.position[i] = max(bounds[i][0], min(self.position[i], bounds[i][1]))

def sphere_function(position):
    return sum(x**2 for x in position)

def pso(num_particles, dim, bounds, max_iter, w=0.5, c1=1.5, c2=1.5):
    particles = [Particle(dim, bounds) for _ in range(num_particles)]
    global_best_position = [0.0 for _ in range(dim)]
    global_best_value = float('inf')

    for t in range(max_iter):
        for particle in particles:
            fitness = sphere_function(particle.position)

            if fitness < particle.best_value:
                particle.best_value = fitness
                particle.best_position = list(particle.position)

            if fitness < global_best_value:
                global_best_value = fitness
                global_best_position = list(particle.position)

        for particle in particles:
            particle.update_velocity(global_best_position, w, c1, c2)
            particle.update_position(bounds)

        print(f"Iteration {t+1}/{max_iter}, Best Value: {global_best_value:.6f}")

    return global_best_position, global_best_value

# Example usage
if __name__ == "__main__":
    dim = 2  # number of dimensions
    bounds = [(-10, 10)] * dim
    best_pos, best_val = pso(num_particles=30, dim=dim, bounds=bounds, max_iter=50)
    print(f"\nBest Position: {best_pos}")
    print(f"Best Value: {best_val}")
