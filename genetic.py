import kuhn
import random

POPULATION_SIZE = 100
MUTATION_RATE = 0.2
MAX_GENERATIONS = 100

def mutation(child):
    new_child = list(child)
    n = random.randint(0, 5)
    if (n < 3):
        i = random.randint(0, 2)
    elif (n > 2):
        i = random.randint(0, 3)
    
    new_child[n] = str(i)
    return "".join(new_child)

def crossover(x, y):
    c = random.randint(1, 4)
    child = x[:c] + y[c:]
    return child

#this algorthm uses the tournement selection method
def selection(population):
    tournament_size = POPULATION_SIZE // 10
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])

#the replication method from genetic programming has been used to promote stability
def replication(population):
    new_population = []
    for i in population:
        if (i[1] > 0):
            new_population.append([i[0], kuhn.BANKROLL])
    return new_population

def algorithm(population):
    for _ in range(MAX_GENERATIONS):
        population = kuhn.poker(population)
        new_population = replication(population)
        while (len(new_population) < POPULATION_SIZE):
            x = selection(population)
            y = selection(population)
            child = crossover(x[0], y[0])
            if random.random() < (MUTATION_RATE):
                child = mutation(child)
            new_population.append([child, kuhn.BANKROLL])
        population = new_population
    return population