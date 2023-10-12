import random
import math
import matplotlib.pyplot as plt

# Define the cities and their coordinates
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 1),
    'D': (4, 4),
    'E': (5, 2),
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Genetic Algorithm parameters
population_size = 100
num_generations = 500
mutation_rate = 0.02

# Generate an initial population
def generate_initial_population(cities):
    population = []
    cities_list = list(cities.keys())
    for _ in range(population_size):
        random.shuffle(cities_list)
        population.append(cities_list[:])
    return population

# Calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    total_distance += distance(route[-1], route[0])  # Return to the starting city
    return total_distance

# Select parents for crossover using tournament selection
def select_parents(population):
    tournament_size = 5
    selected_parents = []
    for _ in range(2):  # Select 2 parents
        tournament = random.sample(population, tournament_size)
        selected_parents.append(min(tournament, key=calculate_total_distance))
    return selected_parents

# Perform crossover to create a child route
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start, len(parent1) - 1)
    child = [None] * len(parent1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining_cities = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining_cities[j]
            j += 1
    return child

# Perform mutation on a route
def mutate(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Main Genetic Algorithm loop
def genetic_algorithm(cities):
    population = generate_initial_population(cities)
    best_distances = []
    for generation in range(num_generations):
        population = sorted(population, key=calculate_total_distance)
        best_distances.append(calculate_total_distance(population[0]))
        parents = select_parents(population)
        child = crossover(parents[0], parents[1])
        mutate(child)
        population[-1] = child  # Replace the worst route with the child
        print(f"Generation {generation + 1}: Best distance = {best_distances[-1]}")
    
    # Plot the best distance over generations
    plt.plot(best_distances)
    plt.xlabel('Generation')
    plt.ylabel('Best Distance')
    plt.title('Genetic Algorithm - Traveling Salesman Problem')
    plt.show()
    
    return population[0]

# Run the Genetic Algorithm
best_route = genetic_algorithm(cities)
print("Best Route:", best_route)
print("Best Distance:", calculate_total_distance(best_route))