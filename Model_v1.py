import copy
import timeit

import numpy as np
import random


def main():
    # Set properties of model:

    N = 100  # Population size
    g = 5  # Number of groups
    qi = 1  # In-group success probability - default = 1
    qo = 0.6  # Out-group success probability 0.6
    Bi = 1  # In-group benefit - default = 1
    Bo = 2  # Out-group Benefit
    sigma = 1 / (N - N / 10)  # To keep N*sigma ~  1
    p = 1  # Polarisation
    trials = 10000  # Number of trials

    print(f"Model properties: \n\nPopulation size, N: {N} \nNumber of groups, g: {g} \n"
          f"In-group success probability, qi: {qi} \nOut-group success probability, qo: {qo} \n"
          f"In-group benefit, Bi {Bi} \nOut-group benefit, Bo: {Bo} \n"
          f"Strength of selection, sigma: {sigma}\nPolarisation p: {p} \nNumber of trails, trials: {trials}")

    # Initial population saved as a dictionary with value 1 suggesting polarised.
    # member index: [polarisation (pi), group number]
    start_population = {i: [p, 0] for i in range(N)}

    g_num = -1
    # Assigning the group numbers - note this breaks for small N
    for j in range(0, N, int(N / g)):
        g_num += 1

        if j + int(N / g) < N:
            for k in range(j, j + int(N / g)):
                start_population[k][1] = g_num
        else:
            for k in range(j, N):
                start_population[k][1] = g_num

    # Adjacency matrix
    # Configured to just create a simple connected graph for now.
    adj = [[1 if i != j else 0 for i in range(N)] for j in range(N)]

    # Choose a random member of the population and flip their polarisation
    initial = random.randrange(N)
    start_population[initial][0] = 0

    pol_flips = 0  # Number of times that the population finishes with 0 polarisation

    # Expected fitness
    def wi_func(pi, pobar):
        return pi * qi * Bi + (1 - pi) * (1 - pobar) * qo * Bo

    # Finding neighbours
    def neighbours(i):
        pos_neighbours = adj[i]
        neigh = []
        index = 0

        for n in pos_neighbours:
            if n != 0:
                neigh.append(index)
            index += 1

        return neigh

    # Calculates probability of switching strategy
    def prob_function(w_i, w_j):
        return 1 / (1 + np.exp(sigma * (w_i - w_j)))

    # Calculates pobar
    def pbar(population, group, neigh):
        total = 0
        count = 0

        for n in neigh:
            if population[n][1] != group:
                total += population[n][0]
                count += 1

        return total / count

    def loop():
        pol_flips = 0

        for __ in range(trials):
            initial = random.randrange(N)
            population = copy.deepcopy(start_population)
            population[initial][0] = 0

            for _ in range(100 * N):
                # Select i and calculate properties
                i = random.randrange(N)
                i_neighbours = neighbours(i)
                i_group = population[i][1]
                i_pobar = pbar(population, i_group, i_neighbours)

                # Select j and calculate properties
                j = random.choice(i_neighbours)
                j_neighbours = neighbours(j)
                j_group = population[j][1]
                j_pobar = pbar(population, j_group, j_neighbours)

                # Expected fitness for i and j
                wi = wi_func(population[i][0], i_pobar)
                wj = wi_func(population[j][0], j_pobar)

                # Probability that i will copy j strategy
                prob = prob_function(wi, wj)

                if random.random() < prob:
                    population[i][0] = population[j][0]

                # Check whether the absorbing state of zero polarisation or maximal polarisation has been reached
                first = population[0][0]
                if first in [0, 1] and all(flag == first for [flag, _] in population.values()):
                    if first == 0:
                        pol_flips += 1
                    break
        return pol_flips

    pol_flips = loop()

    print()
    print("The probability that zero polarisation takes over is:")
    print(pol_flips / trials)

    return

main()