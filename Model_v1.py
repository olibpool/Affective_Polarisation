import copy
import numpy as np
import random
import datetime

# Set properties of model:

N = 1000  # Population size
g = 4  # Number of groups # TODO vary this and make graph
qi = 1  # In-group success probability - default = 1
qo = 0.6  # Out-group success probability -defualt = 0.6
Bi = 1  # In-group benefit - default = 1
Bo = 2  # Out-group Benefit - default = 2
sigma = 1 / N  # To keep N*sigma ~  1 default 1/N
p = 1  # Polarisation
trials = 10000  # Number of trials, keep around 10*N. Takes around N generations to reach fixation

parameters = f"Model properties: \n\nPopulation size, N: {N} \nNumber of groups, g: {g} \nIn-group success " \
             f"probability, qi: {qi} \nOut-group success probability, qo: {qo} \nIn-group benefit, " \
             f"Bi {Bi} \nOut-group benefit, Bo: {Bo} \nStrength of selection, sigma: {sigma}\nPolarisation p: {p} " \
             f"\nNumber of trails, trials: {trials} \n"

print(parameters)

# Save to log? True = Save
log = True
filename = "Logs/Model " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ".log")

# Create log file
if log:
    f = open(filename, "a")
    f.write(parameters)
    f.write("\n")
    f.write("\nThese parameters give the following p-values: \n")
    f.close()

# Initial population saved as a dictionary with value 1 suggesting polarised.
# member index: [polarisation (pi)]
start_population = np.array([1 for i in range(N)])

# Adjacency matrix
# Configured to just create a simple connected graph for now. Also array is used for effciency purposes.
adj = np.array([[1 if i != j else 0 for i in range(N)] for j in range(N)])


# Expected fitness
def wi_func(pi, pobar):
    return pi * qi * Bi + (1 - pi) * (1 - pobar) * qo * Bo


# Finding neighbours
def neighbours(i):
    pos_neighbours = adj[i]
    neigh = np.where(pos_neighbours == 1)[0]
    return neigh


# Calculates probability of switching strategy
def prob_function(w_i, w_j):
    return 1 / (1 + np.exp(sigma * (w_i - w_j)))


# Calculates pobar
def pbar(group, neigh):
    outgroup_neigh_pol = [population[n] for n in neigh if int(n * g / N) != group]
    return np.mean(outgroup_neigh_pol)


results = []

for tests in range(10):
    pol_flips = 0  # Number of times that the population finishes with 0 polarisation

    for counter in range(trials):
        # Choose a random member of the population and flip their polarisation
        initial = random.randrange(N)
        population = copy.deepcopy(start_population)
        population[initial] = 0

        for _ in range(200 * N):
            # Select i and calculate properties
            i = random.randrange(N)
            i_pol = population[i]
            i_neighbours = neighbours(i)

            # Select j and calculate properties
            j = random.choice(i_neighbours)
            j_pol = population[j]

            # Only continue if the polarisations are different
            if i_pol != j_pol:

                i_group = int(i * g / N)
                i_pobar = pbar(i_group, i_neighbours)

                j_neighbours = neighbours(j)
                j_group = int(j * g / N)
                j_pobar = pbar(j_group, j_neighbours)

                # Expected fitness for i and j
                wi = wi_func(population[i], i_pobar)
                wj = wi_func(population[j], j_pobar)

                # Probability that i will copy j strategy
                prob = prob_function(wi, wj)

                if random.random() < prob:
                    population[i] = population[j]

                # Check whether the absorbing state of zero polarisation or maximal polarisation has been reached
                first = population[0]
                if first in [0, 1] and all(flag == first for flag in population):
                    if first == 0:
                        pol_flips += 1
                    break

    print()
    print("The probability that zero polarisation takes over is:")
    print(pol_flips / trials)
    results.append(pol_flips / trials)

    if log:
        with open(filename, "a") as f:
            f.write(str(pol_flips / trials) + "\n")

avg = sum(results) / len(results)

if log:
    with open(filename, "a") as f:
        f.write(f"\n The average p-val was: {avg} \n\n The results were: \n")
        f.write(str(results))
        f.close()

# TODO make graph vary strengh of selection vs fixation
# TODO find a network and plug in adjacency matrix & compare to baseline
# TODO think about varying parameters
