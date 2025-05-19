import numpy as np
# from generate_matrix import Matrix
import time

def sorting(matrix, cweight):
	n,m=matrix.a.shape
	available = np.array([True]*n)
	effective_weights=[]
	effective_degree=[]
	for first in range(m):
		if available.max()==0:
			break
		message=matrix.a.T.dot(np.multiply(cweight,available)).argmax()
		# print(message, matrix.a.T[message].dot(np.multiply(cweight,available)))
		effective_weights.append(matrix.a.T[message].dot(np.multiply(cweight,available)))
		effective_degree.append(matrix.a.T[message].dot(available))
		available=np.multiply(available,np.logical_not(matrix.a.T[message]))	
		# swap maximum effective degree message column with first unsorted message column
		temp=matrix.a[:,first].copy()
		matrix.a[:,first]=matrix.a[:,message].copy()
		matrix.a[:,message]=temp
	first_indices=[0]
	first_row_indices=[0]
	for i in range(len(effective_weights)):
		if effective_weights[i]*2<=effective_weights[first_indices[-1]]:
			first_indices.append(i)
			first_row_indices.append(sum(effective_degree[:first_indices[-1]]))
	first_indices.append(len(effective_weights))
	first_row_indices.append(n)
	newind=np.lexsort(np.rot90(matrix.a))
	matrix.a = matrix.a[newind]
	matrix.a = np.flip(matrix.a,axis=0)
	return [first_indices, first_row_indices, np.flip(cweight[newind])]

def try_transmission(sequences, coding_vector):
	sequences[:,coding_vector]+=1
	sat=0
	for client in sequences:
		if 0 in client and 1 in client:
			sat+=1
	sequences[:,coding_vector]-=1
	return sat
def transmission(matrix,cweight,first_row_indices):
	# print(matrix.shape)
	n,m=matrix.shape
	if m==0:
		return [],0
	sequences=np.zeros((n,3))
	coding_vectors=[]
	for message in range(m):
		filtered = np.array([i for (i,v) in zip(sequences,matrix[:,message]) if v==1])
		coding_vector = 0 if len(filtered)==0 else np.array([try_transmission(filtered, i) for i in range(3)]).argmax()
		for i in range(n):
			if matrix[i,message]:
				sequences[i,coding_vector]+=1
		coding_vectors.append(coding_vector)
		# print(coding_vector, end=' ')
	# print()
	sat=[]
	for j,s in enumerate(sequences):
		if 0 in s and 1 in s:
			sat.append(np.where(s==1)[0][0])
			for i,v in enumerate(coding_vectors):
				if v==sat[-1] and matrix[j][i]==1:
					sat[-1]=i
					matrix[j][i]=0
					# print(j+first_row_indices,i)
					break
			cweight[j+first_row_indices]*=.5
		else:
			sat.append(-1)
	# print(coding_vectors)
	return sat,1 if max(coding_vectors)==0 else 2
	# return [i for i in range(n) if not(0 in sequences[i] and 1 in sequences[i])]
def iteration(matrix,cweight,t,it):
	# print('############ ITERATION',it,'###########')
	if cweight is None or not len(cweight):
		return None
	# print(min(matrix.a.sum(axis=1)))
	first_indices, first_row_indices, cweight = sorting(matrix, cweight)
	# print(first_indices, first_row_indices)
	# matrix.display()
	itr_transmissions=0
	# print(matrix.a)
	for i in range(len(first_indices)-1):
		# print('______')
		satisfied,num_transmissions=transmission(matrix.a[first_row_indices[i]:first_row_indices[i+1],first_indices[i]:first_indices[i+1]],cweight,first_row_indices[i])
		itr_transmissions+=num_transmissions
	# print(itr_transmissions)
		# print('______\n')
		# display(matrix.a[first_row_indices[i]:first_row_indices[i+1],first_indices[i]:first_indices[i+1]],satisfied,cweight,first_row_indices[i])
		# print('______')
		# print('\n\n')	
	# print(matrix.a)
	arr = np.array([0]*len(cweight),dtype=float)
	for i in range(len(cweight)):
		# print("min = ", min(t,np.sum(matrix.a[i],axis = 0)))
		arr[i] = 0.5 ** (min(t,np.sum(matrix.a[i],axis = 0)))
		# print("arr = ",arr[i])
	# print("Arr=",arr)
	unsatisfied=[i for i,notsatisfy in enumerate(arr<np.array(cweight)) if notsatisfy]
	# print("Unsatisfied is ",unsatisfied)
	matrix.a=matrix.a[unsatisfied]
	return cweight[unsatisfied],itr_transmissions

def bingreedy(matrix, t):
	
	start = time.time()
	
	n = matrix.a.shape[0]
	tlogn_tr=0
	# print(matrix.a)
	
	matrix.matrix_sort()
	# print(matrix.a)
	cweight=np.array([1.0]*n)
	tlogn_tr=0
	for i in range(1,int(1e10)):
		op=iteration(matrix,cweight,t,i)
		if op is not None:
			cweight,num_transmissions=op
			# if len(cweight)!=m:
				# print(cweight)
			tlogn_tr+=num_transmissions
			# print(cweight)
			# print(matrix.a.sum(axis=1))
			if num_transmissions==0:
				break
		else:
			break    
  
	end = time.time() - start
	return tlogn_tr, end


# matrix = Matrix(100, 25, 3, 0.4, w=.2, fixP=True)
# print(matrix.a)
# print(bingreedy(matrix, 5))