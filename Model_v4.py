import copy
import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import ast
import os

# Set parameters of model O(N**6) (with a connected graph):
N = 100  # Population size - default = 100
gmin, gmax = 2, 15  # Min / Max number of groups
qi = 1  # In-group success probability - default = 1
qo = 0.6  # Out-group success probability - default = 0.6
Bi = 1  # In-group benefit - default = 1
Bo = 2  # Out-group Benefit - default = 2
sigma = 100 / N  # To keep N*sigma ~  1 default 1 / N
p = 1  # Polarisation
trials = 100 * N  # Number of trials, keep min around 10*N. Takes around N generations to reach fixation
rmin, rmax, steps = 0.95, 0.999, 10  # min / max / steps Probability that j is selected from the same group as i.
matrix = "Aarhus"
date = str(datetime.datetime.now().strftime('%Y-%m-%d_(%H-%M)'))

# Save to log? True = Save
log = True
curr_dir = os.getcwdb()
filename = f"Saved_data/Logs/Date_{date}_log.csv"

if log:
    with open(filename, 'w+', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['N', 'Trials', 'rmin', 'rmax', 'steps', 'gmin', 'gmax'])
        csvwriter.writerow([N, trials, rmin, rmax, steps, gmin, gmax])
        csvwriter.writerow(['data'])

# Use special matrix?
matrix_use = False

# Save Figure produced? True = Save
figure = True

# Adjacency matrix
# Configured to just create a simple connected graph for now. Also array is used for efficiency purposes.
if matrix_use:
    with open("Saved_edges/" + matrix + ".txt", "r") as f:
        matrix_string = f.read()

    adj = ast.literal_eval(matrix_string)
    adj = np.array(adj)
    adj = adj.astype(int)

    # need to reformat N dependent params:
    N = len(adj)
    sigma = 10 / N  # To keep N*sigma ~  1 default 1 / N
    trials = 100 * N  # Number of trials, keep min around 10*N. Takes around N generations to reach fixation

else:
    adj = np.array([[1 if i != j else 0 for i in range(N)] for j in range(N)])

# Initial population saved as an array with value 1 suggesting polarised.
# member index: [polarisation (pi)]
start_population = np.array([1 for i in range(N)])

parameters = f"Model parameters: \n\nPopulation size, N: {N} \nMin num of groups, gmin: {gmin} \nMax num of groups, " \
             f"gmax: {gmax} \nIn-group success " \
             f"probability, qi: {qi} \nOut-group success probability, qo: {qo} \nIn-group benefit, " \
             f"Bi {Bi} \nOut-group benefit, Bo: {Bo} \nStrength of selection, sigma: {sigma}\nPolarisation p: {p} " \
             f"\nNumber of trails, trials: {trials} \nMin / max / steps of r: {rmin}, {rmax}, {steps}\n" \
             f"Save to log?: {log}\nSave figure?: {figure}\nUse matrix?: {matrix_use}\nMatrix used if so: {matrix}"

print(parameters)


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

for ri, r in enumerate(np.linspace(rmin, rmax, steps)):
    results.append([])
    print()
    print("##############################")
    print(f"Val of r: {r}")
    print(f"There is {steps - ri - 1} steps to go after this.")
    print()
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

                in_group_neighbours = []  # change to j selection group
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
                if j_selection_group:
                    j = random.choice(j_selection_group)  # choose j from the same group
                    j_pol = population[j]
                else:
                    j_pol = i_pol  # Just so the if statement below doesn't pass

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
        results[ri].append(pol_flips / trials)

    if log:
        with open(filename, 'a') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerow(results[ri])

fig, ax = plt.subplots()

X, Y = np.meshgrid(range(gmin, gmax + 1), np.linspace(rmin, rmax, steps))

plot = ax.pcolormesh(X, Y, np.array(results), shading='auto')
fig.colorbar(plot, label="p")
ax.set(title=f"Colour plot of probability of fixation for N={N}, Trails={trials}",
       xlabel="Number of groups",
       ylabel="Value of r",
       xticks=list(range(gmin, gmax + 1))
       )

if figure:
    plt.savefig("Saved_data/New_figs/N=" + str(N) + "_Trails=" + str(trials) + "_" + date + ".png")

plt.show()

# TODO make graph vary strength of selection vs fixation
# TODO find a network and plug in adjacency matrix & compare to baseline
# TODO think about varying parameters


# The more groups

# find optimal groups for r and pop
# generate random matrices and test them

# lit review:

# More expansive
# Sections are good
# Just expand the size
# More references
# No objection to the style of writing
# Don't include hand drawn diagrams
# Need a section on what the project is about just detail what the actual project
# Include the markov process in the moran process section
# All i need to do demonstrate i have a grasp of markov processes
# Use symbols in equations
# Use symbols instead of actual numbers, e.g. m individuals
# Write equations in general form.
# Then can write out equations in their general form.
# Try and keep it more general than specific.
# Get more figures in the affective polarisation section.
# make it known that affective polarisation is a real problem.
# Change the ordering a bit. Cultural evolution -> Moran -> Affective Polarisation
# Include a subsection in cultural evolution on evolutionary game theory (specifically moran process).
# Keep it relevant evolutionary game theory -> payoff matrix -> interactions -> leads to fitness function.
# Focusing on the fixation probability.
# Alex is not involved in marking the talk, will be fine to hear a practice and send draft early.

# start to think in the back of my mind how to predict the optimum.
