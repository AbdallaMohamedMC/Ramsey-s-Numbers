import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy.linalg import eigvals, norm

# === Step 1: Generate a pseudorandom graph ===
n = 20  # number of nodes
d = 4   # degree

# Generate a random d-regular graph
G = nx.random_regular_graph(d, n)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=500)
plt.title(f"{d}-Regular Graph with {n} Nodes")
plt.show()

# Get the adjacency matrix as a NumPy array
A = nx.to_numpy_array(G)

# === Step 2: Compute eigenvalues and λ (second-largest eigenvalue) ===
eigenvalues = eigvals(A)
eigenvalues_sorted = sorted(np.abs(eigenvalues), reverse=True)
lambda_2 = eigenvalues_sorted[1]  # second-largest by absolute value

print(f"Second largest eigenvalue λ = {lambda_2:.4f}")

# === Step 3: Check spectral pseudorandomness condition ===
# Create all-ones matrix J
J = np.ones((n, n))

# Compute the normalized matrix (d/n) * J
normalized_J = (d / n) * J

# Calculate difference A - (d/n) * J
diff = A - normalized_J

# Compute spectral norm (2-norm) of the difference matrix
spectral_norm = norm(diff, 2)

print(f"Spectral norm ||A - (d/n)J|| = {spectral_norm:.4f}")
print("Pseudorandomness condition holds?", spectral_norm <= lambda_2)
