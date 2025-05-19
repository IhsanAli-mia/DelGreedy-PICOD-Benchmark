import numpy as np
# from generate_matrix import Matrix
import time

def algorithm1_picod(incidence_matrix, max_degree):
    """
    Implementation of PICOD scheme construction algorithm using NumPy incidence matrix input.
    
    Parameters:
    - incidence_matrix: A NumPy array where incidence_matrix[i][j] = 1 if 
      vertex i is in hyperedge j, and 0 otherwise.
    - max_degree: Maximum degree of the hypergraph
    
    Returns:
    - color: Dictionary mapping vertices to their colors
    - transmissions: List of transmissions (sum of vertices with same color)
    """
    start = time.time()
    
    # Convert to numpy array if not already
    incidence_matrix = np.asarray(incidence_matrix)
    # Transpose the incidence matrix
    # incidence_matrix = incidence_matrix.T
    num_hyperedges, num_vertices = incidence_matrix.shape
    
    # Initialize
    # Create a list of hyperedges as sets for easier manipulation
    H_prime = []
    for j in range(num_hyperedges):
        edge = set(np.where(incidence_matrix[j, :] == 1)[0])
        H_prime.append(edge)
        
    # print(H_prime)
    
    vertices = set(range(num_vertices))
    c = 1
    color = {}
    transmissions = []
    delta = max_degree
    # print(delta)
    
    # Track degrees of vertices (sum of columns)
    degree = {v: np.sum(incidence_matrix[:, v]) for v in vertices}
    
    # print(degree)
    
    remaining_vertices = set(vertices)
    
    
    for delta in range(max_degree, 0, -1):
        empty = True
        for v in remaining_vertices.copy():
            if degree[v] == delta:
                color[v] = c
                empty = False
                remaining_vertices.remove(v)
                # print(H_prime)
                hyperedges_to_be_removed = []
                for e in H_prime:
                    if v in e:
                        for u in e:
                            degree[u] -= 1
                        hyperedges_to_be_removed.append(e)
                        # H_prime.remove(e)
                # print(hyperedges_to_be_removed)
                for edge_to_remove in hyperedges_to_be_removed:
                    H_prime.remove(edge_to_remove)
                # print(H_prime)
                        
        if empty == False:
            # print(color)
            transmissions.append(1)
            c += 1    
    
        if not H_prime:
            break
    
    # while H_prime:
    #     colored = []
    #     empty = True
        
    #     # Find vertices with degree == delta
    #     candidates = [v for v in remaining_vertices if degree[v] == delta]
    #     # print(candidates)
        
    #     if not candidates:
    #         delta -= 1  # Reduce delta and retry
    #         if delta == 0:
    #             break  # No more vertices with positive degree
    #         continue
        
    #     # Assign color to candidates
    #     for v in candidates:
    #         color[v] = c
    #         colored.append(v)
    #         remaining_vertices.remove(v)
    #         empty = False
        
    #     if empty:
    #         delta -= 1
    #         continue
        
    #     # Update hyperedges and degrees
    #     new_hyperedges = []
    #     for e in H_prime:
    #         intersect = e.intersection(colored)
    #         if intersect:
    #             # Remove hyperedge and decrement degrees
    #             for u in e:
    #                 if u not in colored:
    #                     degree[u] -= 1
    #         else:
    #             new_hyperedges.append(e)  # Keep hyperedge if no colored vertex
    #     H_prime = new_hyperedges
        
    #     # Record transmission (sum of colored vertices)
    #     transmissions.append(sum(colored))
    #     c += 1
        
    time_taken = time.time() - start
    # print(colored)
    # print(color)
    
    return len(transmissions), time_taken

# incidence_matrix = np.array([[0,1,1,0],[0,0,0,1],[0,1,0,1],[1,0,0,0],[0,1,0,0]])
# print(incidence_matrix)

# actual_max_degree = np.max(np.sum(incidence_matrix, axis=0))
# print(f"Actual maximum degree: {actual_max_degree}")

# # Run the PICOD algorithm
# color, transmissions = algorithm1_picod(incidence_matrix, actual_max_degree)

# # Display results
# print("\nVertex coloring:")
# for vertex, c in sorted(color.items()):
#     print(f"Vertex {vertex}: Color {c}")

# print("\nTransmissions:", transmissions)

# # Visualize the coloring
# print("\nColored Matrix:")
# colored_vertices = {}
# for i in range(incidence_matrix.shape[0]):
#     if i in color:
#         colored_vertices[i] = color[i]
#     else:
#         colored_vertices[i] = 0  # Uncolored

# # Sort by color for visualization
# for c in range(1, max(color.values()) + 1):
#     vertices_with_color = [v for v, col in color.items() if col == c]
#     print(f"Color {c} vertices: {vertices_with_color}")

# np.random.seed(42)  # For reproducibility

# # Parameters
# n = 6  # number of vertices
# m = 4  # number of hyperedges
# t = 2  # minimum vertex degree
# delta = 4  # maximum vertex degree
# w = 0.3  # weight parameter

# # Generate incidence matrix
# matrix_obj = Matrix(n, m, t, delta, w)
# print("Generated Incidence Matrix:")
# matrix_obj.display()

# # Get the actual matrix
# incidence_matrix = matrix_obj.a
# print("Matrix shape:", incidence_matrix.shape)

# # Calculate actual maximum degree
# actual_max_degree = np.max(np.sum(incidence_matrix, axis=1))
# print(f"Actual maximum degree: {actual_max_degree}")

# # Run the PICOD algorithm
# color, transmissions = algorithm1_picod(incidence_matrix, actual_max_degree)

# # Display results
# print("\nVertex coloring:")
# for vertex, c in sorted(color.items()):
#     print(f"Vertex {vertex}: Color {c}")

# print("\nTransmissions:", transmissions)

# # Visualize the coloring
# print("\nColored Matrix:")
# colored_vertices = {}
# for i in range(incidence_matrix.shape[0]):
#     if i in color:
#         colored_vertices[i] = color[i]
#     else:
#         colored_vertices[i] = 0  # Uncolored

# # Sort by color for visualization
# for c in range(1, max(color.values()) + 1):
#     vertices_with_color = [v for v, col in color.items() if col == c]
#     print(f"Color {c} vertices: {vertices_with_color}")