import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def randomMatrix(size, prob):
    g = nx.erdos_renyi_graph(size, prob)

    m = nx.to_numpy_array(g)

    return m.astype(int)


