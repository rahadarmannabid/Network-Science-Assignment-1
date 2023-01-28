
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
#degree Distribution
list_of_touple_1 = [(0, 1), (0, 4), (0, 5), (0, 6), (0, 7), (0, 9), (0, 10), (0, 11), (1, 4), (1, 5), (1, 6), (1, 7), (1, 9), (1, 10), (1, 11), (2, 3), (2, 8), (3, 8), (4, 5), (4, 6), (4, 7), (4, 9), (4, 10), (4, 11), (5, 6), (5, 7), (5, 9), (5, 10), (5, 11), (6, 7), (6, 9), (6, 10), (6, 11), (7, 9), (7, 10), (7, 11), (9, 10), (9, 11), (10, 11)]
list_of_touple_2 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (7, 8), (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 10), (9, 11), (10, 11)]
list_of_touple_3 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (7, 8), (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 10), (9, 11), (10, 11)]
list_of_touple_4 = [(0, 1), (0, 4), (0, 5), (0, 6), (0, 7), (0, 9), (0, 10), (0, 11), (1, 4), (1, 5), (1, 6), (1, 7), (1, 9), (1, 10), (1, 11), (4, 5), (4, 6), (4, 7), (4, 9), (4, 10), (4, 11), (5, 6), (5, 7), (5, 9), (5, 10), (5, 11), (6, 7), (6, 9), (6, 10), (6, 11), (7, 9), (7, 10), (7, 11), (9, 10), (9, 11), (10, 11)]

name_of_variable = [list_of_touple_1, list_of_touple_2, list_of_touple_3, list_of_touple_4 ]
for i in range(0, len(name_of_variable)):
  
  G = nx.Graph(sorted(list_of_touple_4))
  
  degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
  dmax = max(degree_sequence)
  
  fig = plt.figure("Degree of a random graph", figsize=(8, 8))
  # Create a gridspec for adding subplots of different sizes
  axgrid = fig.add_gridspec(5, 4)
  
  ax0 = fig.add_subplot(axgrid[0:3, :])
  Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
  pos = nx.spring_layout(Gcc, seed=10396953)
  nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
  nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
  ax0.set_title("Connected components of G")
  ax0.set_axis_off()
  
  ax1 = fig.add_subplot(axgrid[3:, :2])
  ax1.plot(degree_sequence, "b-", marker="o")
  ax1.set_title("Degree Rank Plot")
  ax1.set_ylabel("Degree")
  ax1.set_xlabel("Rank")
  
  ax2 = fig.add_subplot(axgrid[3:, 2:])
  ax2.bar(*np.unique(degree_sequence, return_counts=True))
  ax2.set_title("Degree histogram")
  ax2.set_xlabel("Degree")
  ax2.set_ylabel("# of Nodes")
  labels = [2, 4, 6,8, 12]
  plt.xticks(labels, )
  
  fig.tight_layout()
  plt.show()