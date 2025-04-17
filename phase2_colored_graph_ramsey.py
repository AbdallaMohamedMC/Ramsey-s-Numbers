import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import combinations

# Parameters
n = 30         # Number of nodes
d = 10         # Degree for regular graph
colors = ['red', 'blue']  # Two edge colors

# Step 1: Generate pseudorandom regular graph
G = nx.random_regular_graph(d, n)

# Step 2: Randomly color the edges
edge_colors = {}
for u, v in G.edges():
    edge_colors[(u, v)] = random.choice(colors)

# Step 3: Add color attribute to the edges
for (u, v), color in edge_colors.items():
    G[u][v]['color'] = color

# Step 4: Visualize the graph
pos = nx.spring_layout(G, seed=42)
edge_color_list = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, pos, with_labels=True, edge_color=edge_color_list, node_color='lightblue')
plt.title("Random 2-Colored Pseudorandom Graph")
plt.show()

# Step 5: Function to find largest monochromatic clique
def find_largest_monochromatic_clique(G, target_color):
    max_clique = []
    nodes = list(G.nodes())

    # Check all subsets of nodes of increasing size
    for size in range(2, len(nodes) + 1):
        for subset in combinations(nodes, size):
            subgraph = G.subgraph(subset)
            all_colored = True
            for u, v in subgraph.edges():
                if G[u][v].get('color') != target_color:
                    all_colored = False
                    break
            if all_colored and nx.is_clique(subgraph):
                if len(subset) > len(max_clique):
                    max_clique = list(subset)
    return max_clique

# Step 6: Run clique detection for both colors
for color in colors:
    clique = find_largest_monochromatic_clique(G, color)
    print(f"Largest {color} clique has {len(clique)} nodes: {clique}")
