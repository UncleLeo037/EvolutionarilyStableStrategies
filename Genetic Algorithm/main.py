import genetic
import kuhn
import random

import matplotlib.pyplot as plt
import numpy as np
import os

def rand_gene():
    gene = []
    for _ in range(3):
        gene.append(str(random.randint(0, 2)))
    for _ in range(3):
        gene.append(str(random.randint(0, 3)))
    return "".join(num for num in gene if num)

def check(gene):
    score = 0
    if (gene[0] == '0' or gene[0] == '2'):
        if (gene[1] == '0' or gene[1] == '1'):
            if (gene[2] == '1' or gene[2] == '2'):
                score += 1

    if (gene[3] == '0' or gene[3] == '2'):
        if (gene[4] == '0' or gene[4] == '1'):
            if (gene[5] == '3'):
                score += 1
    
    return score

def result(population):
    p2J1 = 0
    p2J2 = 0
    p2Q1 = 0
    p2Q2 = 0

    strat = 0
    for i in population:
        gene = i[0]
        #strat += check(gene)
        if (gene[0] == '0' or gene[0] == '2'):
            if (gene[1] == '0' or gene[1] == '1'):
                if (gene[2] == '1' or gene[2] == '2'):
                    strat += 1

        if (gene[3] == '0' or gene[3] == '2'):
            if (gene[4] == '0' or gene[4] == '1'):
                if (gene[5] == '3'):
                    strat += 1
                    if (gene[3] == '0'):
                        p2J1 += 1
                    if (gene[3] == '2'):
                        p2J2 += 1
                    if (gene[4] == '0'):
                        p2Q1 += 1
                    if (gene[4] == '1'):
                        p2Q2 += 1
    
    
    if (p2J1):
        p2J = (p2J2/p2J1)
    else:
        p2J = 0

    if (p2Q1):
        p2Q = (p2Q2/p2Q1)
    else:
        p2Q = 0
    #print(p2Q)

    return ((strat/2)/genetic.POPULATION_SIZE)*100


def main():
    iterations = 49

    temp = [rand_gene() for _ in range(genetic.POPULATION_SIZE)]
    population = []
    for i in temp:
        population.append([i, kuhn.BANKROLL])

    x = np.array([])
    y = np.array([])

    for i in range(iterations+1):
        x = np.append(x, str(i+1))
        y = np.append(y, 0)

    y[0] = result(population)

    display = plt.bar(x, y, color="royalblue")
    plt.xlabel("Observation No.")
    plt.ylabel("Percentage of population")
    plt.ylim(0, genetic.POPULATION_SIZE)
    #manager = plt.get_current_fig_manager()
    #manager.full_screen_toggle()
    plt.pause(0.1)

    total = 0
    for j in range(iterations):
        population = genetic.algorithm(population)
        fit = result(population)
        total += fit

        y[j+1] = fit
        display.remove()
        display = plt.bar(x, y, color="royalblue")
        plt.pause(0.1)
    
    print("average:")
    print(total/iterations)
    plt.show()

if __name__ == "__main__":
    main()