import copy
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime

# Set parameters of model O(N**6) (with a connected graph):
N = 100  # Population size - default = 100
gmin, gmax = 2, 2  # Min / Max number of groups
qi = 1  # In-group success probability - default = 1
qo = 0.6  # Out-group success probability - default = 0.6
Bi = 1  # In-group benefit - default = 1
Bo = 2  # Out-group Benefit - default = 2
sigma = 1 / N  # To keep N*sigma ~  1 default 1 / N
p = 1  # Polarisation
trials = 100 * N  # Number of trials, keep min around 10*N. Takes around N generations to reach fixation
r = 0.9  # Probability that j is selected from the same group as i.

parameters = f"Model parameters: \n\nPopulation size, N: {N} \nMin num of groups, gmin: {gmin} \nMax num of groups, " \
             f"gmax: {gmax} \nIn-group success " \
             f"probability, qi: {qi} \nOut-group success probability, qo: {qo} \nIn-group benefit, " \
             f"Bi {Bi} \nOut-group benefit, Bo: {Bo} \nStrength of selection, sigma: {sigma}\nPolarisation p: {p} " \
             f"\nNumber of trails, trials: {trials} \n"

print(parameters)

# Save to log? True = Save
log = False
filename = "Logs/Model " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ".log")

# Save Figure produced? True = Save
figure = True

# Create log file
if log:
    f = open(filename, "a")
    f.write(parameters)
    f.write("\n")
    f.write("\nThese parameters give the following p-values: \n")
    f.close()

# Initial population saved as an drray with value 1 suggesting polarised.
# member index: [polarisation (pi)]
start_population = np.array([1 for i in range(N)])

# Adjacency matrix
# Configured to just create a simple connected graph for now. Also array is used for efficiency purposes.
adj = np.array([[1 if i != j else 0 for i in range(N)] for j in range(N)])


# Expected fitness
def wi_func(group_size, pi, pobar):  # account for group size
    return (group_size / N) * pi * qi * Bi + (1 - group_size / N) * (1 - pi) * (1 - pobar) * qo * Bo


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

for g in range(gmin, gmax + 1):
    pol_flips = 0  # Number of times that the population finishes with 0 polarisation

    group_sizes = []  # List to save the value of each group
    groups = [int(n * g / N) for n in range(N)]

    for n in range(g):
        group_sizes.append(groups.count(n))

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
            i_neighbours = neighbours(i)

            # Split i neighbours into in/out groups
            index_of_first_in_i_group = sum(group_sizes[0:i_group])
            index_of_last = index_of_first_in_i_group + group_sizes[i_group]

            in_group_neighbours = [] #change to j selection group
            out_group_neighbours = []
            for n in i_neighbours:
                if index_of_first_in_i_group <= n < index_of_last:
                    in_group_neighbours.append(n)
                else:
                    out_group_neighbours.append(n)

            # Choose group to select j from, according to r
            if random.random() < r:
                j_selection_group = in_group_neighbours
            else:
                j_selection_group = out_group_neighbours

            # Select j and calculate properties
            j = random.choice(j_selection_group)  # choose j from the same group
            j_pol = population[j]

            # Only continue if the polarisations are different
            if i_pol != j_pol:
                i_group_size = group_sizes[i_group]
                i_pobar = pbar(i_group, i_neighbours)

                j_neighbours = neighbours(j)
                j_group = int(j * g / N)
                j_group_size = group_sizes[j_group]
                j_pobar = pbar(j_group, j_neighbours)

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
    plt.savefig("Saved_data/Population size: " + str(N) + " Trails: " + str(trials) + "  " + str(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ".png")

plt.show()

# TODO make graph vary strength of selection vs fixation
# TODO find a network and plug in adjacency matrix & compare to baseline
# TODO think about varying parameters


# The more groups
