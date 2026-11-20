import numpy as np
import networkx as nx

# Toy model weighted adjacency matrix
original_graph = np.array([
	[6, 3, 2, 3, 5, 0],
	[3, 17, 4, 0, 0, 0],
	[2, 4, 8, 12, 1, 0],
	[3, 0, 12, 6, 4, 0],
	[5, 0, 1, 4, 8, 8],
	[0, 0, 0, 0, 8, 4]
])

# Convert edge weights to inverse distances
with np.errstate(divide='ignore', invalid='ignore'):
	reciprocal_graph = np.where(original_graph != 0, 1 / original_graph, 0)

# Build weighted undirected NetworkX graph
G = nx.from_numpy_array(reciprocal_graph, parallel_edges=False, create_using=None, edge_attr='weight')
output_file = 'Betweenness_toymodel_con_peso_inverso.txt'

# Compute weighted betweenness centrality for all nodes
betweenness_dict = nx.betweenness_centrality(G, k=None, normalized=False, weight="weight", endpoints=False)
node_centralities = list(betweenness_dict.values())

with open(output_file, 'w') as file:
	for i, val in enumerate(node_centralities):
		file.write(f"Betweenness {i}:\n")
		np.savetxt(file, [val], fmt='%f', delimiter='\t')

print(betweenness_dict)
print(f"Betweenness values saved to: {output_file}")