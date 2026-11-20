import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

# Toy model weighted adjacency matrix
original_graph = np.array([
	[6, 3, 2, 3, 5, 0],
	[3, 17, 4, 0, 0, 0],
	[2, 4, 8, 12, 1, 0],
	[3, 0, 12, 6, 4, 0],
	[5, 0, 1, 4, 8, 8],
	[0, 0, 0, 0, 8, 4]
])

# Convert edge weights to inverse distances (higher adjacency frequency = shorter distance)
with np.errstate(divide='ignore', invalid='ignore'):
	reciprocal_graph = np.where(original_graph != 0, 1 / original_graph, 0)

graph = csr_matrix(reciprocal_graph)
output_file = 'Closeness_toymodel_con_peso_inverso.txt'

with open(output_file, 'w') as file:
	for i in range(graph.shape[0]):
		dist_matrix = dijkstra(graph, unweighted=False, directed=False, indices=i)
		row_sum = np.sum(dist_matrix)
		row_with_sum = np.append(dist_matrix, row_sum)
		reciprocal_sum = 1 / row_sum if row_sum != 0 else 0
		row_with_sum = np.append(row_with_sum, reciprocal_sum)

		file.write(f"Closeness {i}:\n")
		np.savetxt(file, [row_with_sum], fmt='%f', delimiter='\t')

print(f"Shortest paths and closeness values saved to: {output_file}")