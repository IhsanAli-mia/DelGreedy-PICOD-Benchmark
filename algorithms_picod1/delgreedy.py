import numpy as np
# from generate_matrix import Matrix
import time

def independant_set(matrix, transmissions=0):
	if matrix.shape[0]!=0:
		n,m=matrix.shape
		# my_matrix=Matrix(10,10,10)
		# my_matrix.a=matrix
		# my_matrix.display()
	else:
		return transmissions
	available = [True]*n
	for message in range(m):
		if matrix[:,message].dot(np.logical_not(available))==0:
			available=np.multiply(available,np.logical_not(matrix[:,message]))
			# if sum(matrix[:,message])!=0:
			# 	print(message,end=' ')
	# print(' ')
	return independant_set(np.array([row for i,row in enumerate(matrix) if available[i]]).astype(int),transmissions+1)


def delgreedy(matrix):
    
    start = time.time()
    
    matrix.matrix_sort()
    transmissions = independant_set(matrix.a)
    
    time_taken = time.time() - start
    
    return transmissions,time_taken

# n = 16  # number of vertices
# m = 14  # number of hyperedges
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

# colors, transmissions = sort_and_picod(incidence_matrix)
# print("Colors assigned to vertices:", colors)
# print("Number of transmissions:", transmissions)