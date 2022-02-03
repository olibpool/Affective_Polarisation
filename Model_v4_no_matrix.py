import copy
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import csv

# Set parameters of model O(N**6) (with a connected graph):
N = 20  # Population size - default = 100
gmin, gmax = 2, 10  # Min / Max number of groups
qi = 1  # In-group success probability - default = 1
qo = 0.6  # Out-group success probability - default = 0.6
Bi = 1  # In-group benefit - default = 1
Bo = 2  # Out-group Benefit - default = 2
sigma = 10 / N  # To keep N*sigma ~  1 default 1 / N
p = 1  # Polarisation
trials = 100 * N  # Number of trials, keep min around 10*N. Takes around N generations to reach fixation
r = 0.99  # Probability that j is selected from the same group as i.

parameters = f"Model parameters: \n\nPopulation size, N: {N} \nMin num of groups, gmin: {gmin} \nMax num of groups, " \
             f"gmax: {gmax} \nIn-group success " \
             f"probability, qi: {qi} \nOut-group success probability, qo: {qo} \nIn-group benefit, " \
             f"Bi {Bi} \nOut-group benefit, Bo: {Bo} \nStrength of selection, sigma: {sigma}\nPolarisation p: {p} " \
             f"\nNumber of trails, trials: {trials} \n"

print(parameters)

# Save to log and/or csv? True = Save
log = False
csvsave = False
filename = "Logs/Model " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ".log")

# Save Figure produced? True = Save
figure = False

# Create log file
if log:
    f = open(filename, "a")
    f.write(parameters)
    f.write("\n")
    f.write("\nThese parameters give the following p-values: \n")
    f.close()

# Initial population saved as an array with value 1 suggesting polarised.
# member index: [polarisation (pi)]
start_population = np.array([1 for i in range(N)])


# Expected fitness
def wi_func(group_size, pi, pobar):  # account for group size
    return (group_size / N) * pi * qi * Bi + (1 - group_size / N) * (1 - pi) * (1 - pobar) * qo * Bo


# Calculates probability of switching strategy
def prob_function(w_i, w_j):
    return 1 / (1 + np.exp(sigma * (w_i - w_j)))


# Calculates pobar
def pbar(group):
    outgroup_pol = [population[n] for n in population if int(n * g / N) != group]
    return np.mean(outgroup_pol)


results = []

for g in range(gmin, gmax + 1):
    pol_flips = 0  # Number of times that the population finishes with 0 polarisation

    group_sizes = []  # List to save the value of each group
    group_indexes = []  # List to save the first index of each group
    groups = [int(n * g / N) for n in range(N)]

    for n in range(g):
        group_sizes.append(groups.count(n))
        group_indexes.append(sum(group_sizes[:n]))

    group_indexes.append(N - 1)

    for counter in range(trials):
        # Choose a random member of the population and flip their polarisation
        initial = random.randrange(N)
        population = copy.deepcopy(start_population)
        population[initial] = 0

        for _ in range(200 * N):
            # Select i and calculate properties
            i = random.randrange(N)
            i_pol = population[i]
            i_group = int(i * g / N)

            # Split i neighbours into in/out groups
            index_of_first = group_indexes[i_group]
            index_of_last = group_indexes[i_group + 1]

            # Select j, according to r
            if random.random() < r:
                j = random.randrange(index_of_first, index_of_last + 1)
                while j == i:
                    j = random.randrange(index_of_first, index_of_last + 1)
            else:
                j = random.choice(
                    list(range(0, index_of_first)) + list(range(index_of_last + 1, N))
                )
            j_pol = population[j]

            # Only continue if the polarisations are different
            if i_pol != j_pol:
                i_group_size = group_sizes[i_group]
                i_pobar = pbar(i_group)

                j_group = int(j * g / N)
                j_group_size = group_sizes[j_group]
                j_pobar = pbar(j_group)

                # Expected fitness for i and j
                wi = wi_func(i_group_size, i_pol, i_pobar)
                wj = wi_func(j_group_size, j_pol, j_pobar)

                # Probability that i will copy j strategy
                prob = prob_function(wi, wj)

                if random.random() < prob:
                    population[i] = population[j]

                # Check whether the absorbing state of zero polarisation or maximal polarisation has been reached
                first = population[0]
                if first in [0, 1] and np.all(population == first):
                    if first == 0:
                        # print("flipped!")
                        pol_flips += 1
                    break

    print()
    print("The probability that zero polarisation takes over is:")
    print(pol_flips / trials)
    print(f"For {g} groups.")
    results.append(pol_flips / trials)

    if log:
        with open(filename, "a") as f:
            f.write(f"g= {g} " + str(pol_flips / trials) + "\n")

fig, ax = plt.subplots()
ax.plot(range(gmin, gmax + 1), results)
ax.set(title=f"Population size: {N}, Trails: {trials}",
       xlabel="Number of groups",
       ylabel="Probability of ending with 0 polarisation",
       ylim=[0, max(results) * 1.1])

if figure:
    plt.savefig("Saved_data/Population_size:" + str(N) + "_Trails:" + str(trials) + "_" + str(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ".png")

if csvsave:
    f = open("Saved_data/model_v4.csv")

    writer = csv.writer(f)

    writer.writerow()


plt.show()

# TODO make graph vary strength of selection vs fixation
# TODO find a network and plug in adjacency matrix & compare to baseline
# TODO think about varying parameters


# The more groups
