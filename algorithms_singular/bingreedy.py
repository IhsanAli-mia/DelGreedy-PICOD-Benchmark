# from generate_matrix import Matrix
import numpy as np
import time

def matrix_grouping(matrix):
	n,m=matrix.a.shape
	available = [True]*n
	effective_degrees=[]
	# loop for grouping the messages by effective degree
	for first_message in range(m):
		# pick 1st message with maximum effective degree
		message = matrix.a.T.dot(available).argmax()
		# update available clients(those clients which are not effective clients of any message)
		if matrix.a.T.dot(available).max().round().astype(int)==0:
			break
		effective_degrees.append(matrix.a.T.dot(available).max().round().astype(int))
		available=np.multiply(available,np.logical_not(matrix.a[:,message]))	
		# swap maximum effective degree message column with first unsorted message column
		temp=matrix.a[:,first_message].copy()
		matrix.a[:,first_message]=matrix.a[:,message].copy()
		matrix.a[:,message]=temp
	first_indices=[0]
	first_row_indices=[0]
	for i in range(len(effective_degrees)):
		if effective_degrees[i]*2<=effective_degrees[first_indices[-1]]:
			first_indices.append(i)
			first_row_indices.append(sum(effective_degrees[:first_indices[-1]]))
	first_indices.append(len(effective_degrees))
	first_row_indices.append(n)
	return [first_indices, first_row_indices, len(np.unique(effective_degrees))]

def try_transmission(sequences, coding_vector):
	sequences[:,coding_vector]+=1
	sat=0
	for client in sequences:
		if 0 in client and 1 in client:
			sat+=1
	sequences[:,coding_vector]-=1
	return sat

def transmission(matrix):
	num_transmissions=1
	n,m=matrix.shape
	sequences=np.zeros((n,3))
	for message in range(m):
		filtered = np.array([i for (i,v) in zip(sequences,matrix[:,message]) if v])
		if len(filtered)==0:
			coding_vector=0
		else:
			coding_vector = np.array([try_transmission(filtered, i) for i in range(3)]).argmax()
		if coding_vector!=0:
			num_transmissions=2
		for i in range(n):
			if matrix[i,message]:
				sequences[i,coding_vector]+=1
	# for i,row in enumerate(matrix):
	# 	print(0 in sequences[i] and 1 in sequences[i])
	next_round = np.array([i for i,row in enumerate(matrix) if not(0 in sequences[i] and 1 in sequences[i])])
	# print(next_round)
	return next_round, num_transmissions

def bingreedy(matrix):
    
    start = time.time()
    
    transmissions = 0
    
    while matrix.a.shape[0]:
        matrix.matrix_sort()
        first_indices, first_row_indices, _ = matrix_grouping(matrix)
        next_round = np.empty(0).astype(int)
        
        for i in range(len(first_indices)-1):
            next_round_indices, num_transmissions=transmission(matrix.a[first_row_indices[i]:first_row_indices[i+1],first_indices[i]:first_indices[i+1]])
            next_round = np.append(next_round,first_row_indices[i]+next_round_indices).astype(int)
            transmissions+=num_transmissions
        matrix.a=np.asarray([row for i,row in enumerate(matrix.a) if i in next_round]).astype(int)
        
    time_taken = time.time() - start

    return transmissions,time_taken
# # Example usage
# if __name__ == "__main__":
#     random_seed = 42
    
#     n = 120  # number of vertices
#     m = 120  # number of hyperedges
#     t = 1  # minimum vertex degree
#     delta = 10  # maximum vertex degree
#     w = 1  # weight parameter

#     matrix = Matrix(n, m, t, delta, w)
#     matrix.display()
    
#     transmissions = bingreedy(matrix)
#     print(transmissions)