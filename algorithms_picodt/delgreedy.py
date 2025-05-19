import numpy as np
# from generate_matrix import Matrix
import time

def picod_sort(matrix):
	n,m=matrix.shape
	available = [True]*n
	# loop for sorting the messages by effectve degree
	for first_message in range(m):
		# pick 1st message with maximum effective degree
		message = matrix.T.dot(available).argmax()
		# update available clients(those clients which are not effective clients of any message)
		if matrix.T.dot(available).max().round().astype(int)==0:		
			break
		available=np.multiply(available,np.logical_not(matrix[:,message]))	
		# swap maximum effective degree message column with first unsorted message column
		temp=matrix[:,first_message].copy()
		matrix[:,first_message]=matrix[:,message].copy()
		matrix[:,message]=temp
	# sort clients in lexicographic order, so grouping is easier
	# matrix = matrix[np.lexsort(np.rot90(matrix))]
	# matrix = np.flip(matrix,axis=0)
	return matrix

def independant_set(matrix, countsat, transmissions=0):
	n,m=matrix.shape
	# Thess are the base case of recursion. If length(countsat) == 0 then this means all clients have been satisfied
	# then we just have to output the no of transmissions. NOte that the actual transmissions are not shown here, neither
	# the actual independent set. To see the actual index code being formed, you have to print out the matrices or message indices
	# in independent sets at appropriate places
	if len(countsat)!=0: #This is the count of how many msgs which have been decoded by the clients
		n,m=matrix.shape
	else:
		return transmissions
	# print(matrix)
	matrix=picod_sort(matrix)
	# display(matrix)
 
	available = [True]*n # This is the set of clients all of them are not yet served, so they are not all available
	removemsg=[]
	for message in range(m):
		if matrix[:,message].dot(np.logical_not(available))==0: # This is checking if the currently considered message is available in the request set of a previously chosen client ( this dot product is 0 => the considered message is NOT available in the request set of ANY previously served client)
			available=np.multiply(available,np.logical_not(matrix[:,message])) # The set of not yet served clients is updated here. That is, if the new messages is present in that client then that client becomes unavailable
			countsat=countsat-matrix[:,message] # (This means the clients given by matrix[:,message]  [The 'message'th column refers to the clients which are missing the message. All these now decode the message, hence count-sat is updated to this, indicating that those clients served by the present message have their count-sat-value reduced by 1)
			removemsg.append(message) #removemsg is collecting the set of messages in the independent set to be removed. These messages are removed because, in the present state of the graph, ALL clients which can be served by them have been served by them
			
	# print("removemsg = ",removemsg)
	# if removemsg==[]:
	# 	return transmissions
	matrix=np.delete(matrix,removemsg,axis=1) # all the messages in 'removemsg' vector are removed from the matrix. [axis=1] implies the column corresponding to these messages are removed from the matrix
	# print(removemsg)
	removeclnt=[]
	for i,count in enumerate(countsat): # To check the ith value in countsat, which is called count here
		if count==0:
			removeclnt.append(i) # If that ith value in countsat is 0, then this means ith rx is satisfied. This client-index is then added to removeclnt
	countsat=np.delete(countsat,removeclnt) # Remove the clients which have been listed for removal, in removeclnt
	matrix=np.delete(matrix,removeclnt,axis=0) # Delete the rows of the matrix , corresponding to clients, scheduled for removal
	return independant_set(matrix,countsat,transmissions+1) # Note that this does NOT return the independent set actually. It only returns the return value of the recursive call of independent-set-funtion, with the input to the function being the updated matrix, countsat, and the value of transmissions.

def delgreedy(matrix,t):
    start = time.time()
    
    matrix.matrix_sort() 
    n,m = matrix.a.shape
    
    array = [0]*n
    for i in range(n):
        array[i] = min(t,np.sum(matrix.a[i],axis = 0)) # This is calculating the min(t,Size-of-request-set) for each client i.
    
    picod_t_tr = independant_set(matrix.a,array,0) # Start the recursion with input matrix (matrix.a), the current count-sat=array, and the currentnooftransmissions=0). Note that by the recursion, the base case will return just the number of transmissions. So picod_t_tr will contain no. of . transmissions only
    
    end = time.time() - start
    
    return picod_t_tr, end


# matrix = Matrix(100, 25, 3, 0.4, w=.2, fixP=True)
# print(matrix.a)
# print(delgreedy(matrix, 5))

# matrix = Matrix(10, 5, 1, 0.4, w=.3, fixP=True)
# matrix.a = np.array([
#     [0, 1, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [0, 0, 0, 1, 1],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0]
# ])

# print(delgreedy(matrix,2))