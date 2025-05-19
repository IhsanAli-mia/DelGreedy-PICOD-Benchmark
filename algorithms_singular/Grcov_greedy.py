import numpy as np
from math import floor, ceil
# from generate import Matrix
import time

##############3
def GrCovTgreedy(matrix, s, t, iterations=0, indices=[]):
    
    start = time.time()
    
    n,m = matrix.shape
    # print("initial matrix \n", matrix)
    
    cweight = np.array([t]*n)

    while not(n == 0 or m == 0):
        if iterations == 0:
            indices = np.arange(m)
        if s:
            matrix_sort(matrix)
        taken = np.array([0]*n)

        selected_columns = []
        
        best_columns=[]
        for col in range(m):
            satisfied_clients = (matrix[:, col] + taken) == 1
            satisfied_count = np.count_nonzero(satisfied_clients)
            ##print(taken)

            ## Track the column with the maximum satisfied clients
            if satisfied_count > np.count_nonzero(taken == 1):
                selected_columns.append(col)  # Reset and add the new max column
        #print("selected columns:",indices[selected_columns]+1)
        while len(selected_columns)!=0:
            best_column=bc_from_sc(matrix,selected_columns,taken)
            
            if best_column is None:  # Stop if no valid best column is found
                break
            taken += matrix[:, best_column].astype(np.int32)
            ##taken += matrix[:, best_column].astype(np.int32).ravel()
            best_columns.append(best_column)
            selected_columns.remove(best_column)
            #print("Remaining Columns", indices[selected_columns]+1)
        #print("best columns",indices[best_columns] + 1)
        cweight[np.where(taken == 1)]-=1
        #print("Client weights",cweight)

        for r in np.where(taken == 1)[0]:
            for c in best_columns:
                matrix[r,c]=0
        #matrix.display()
        #remove satisfied clients
        matrix = np.delete(matrix, np.where(cweight == 0), axis=0)
        cweight = np.delete(cweight, np.where(cweight == 0), axis=0)

        #remove messages and indices that have no more clients
        indices = np.delete(indices, np.all(matrix == 0, axis=0))
        ## matrix.a = matrix.a[:, ~np.all(matrix.a == 0, axis=0)]
        matrix = np.delete(matrix, np.all(matrix == 0, axis=0), axis=1)
        #print(matrix)
        n,m = matrix.shape

        iterations+=1
        
    time_taken = time.time() - start
    return iterations,time_taken

def bc_from_sc(matrix,selected_columns,taken):        
# If we found any column, select the one with the maximum satisfied clients
    if selected_columns:
        # Calculate satisfaction counts for each column in `selected_columns`
        satisfaction_counts = [np.count_nonzero((matrix[:, col] + taken) == 1) for col in selected_columns]
        #print("Satisfaction counts:", satisfaction_counts)
        
        # Find the index of the column with the maximum satisfied clients in `selected_columns`
        max_index = np.argmax(satisfaction_counts)
        max_satisfaction_count = satisfaction_counts[max_index]
        best_column = selected_columns[max_index]

        # Check the satisfaction count condition
        if max_satisfaction_count <= np.count_nonzero(taken == 1):
            return None
        
        return best_column

    return None         
#########################

def matrix_sort(matrix):
        n, m = matrix.shape
        available = [True]*n
        # loop for sorting the messages by effectve degree
        for first_message in range(m):
            # pick 1st message with maximum effective degree
            message = matrix.T.dot(available).argmax()
            # update available clients(those clients which are not effective clients of any message)
            if matrix.T.dot(available).max().round().astype(int) == 0:
                break
            available = np.multiply(
                available, np.logical_not(matrix[:, message]))
            # swap maximum effective degree message column with first unsorted message column
            temp =matrix[:, first_message].copy()
            matrix[:, first_message] = matrix[:, message].copy()
            matrix[:, message] = temp
        # sort clients in lexicographic order, so grouping is easier
        matrix = matrix[np.lexsort(np.rot90(matrix))]
        matrix = np.flip(matrix, axis=0)


#n=200
#m=100
#w=0.6
#t=10
#d=50
#p = (((1-w)*n*t+m*d*w))/(m*n)
#A = np.random.uniform(0, 1, size=(n, m))
#print(A)
#B = p*np.ones(shape=(n, m))
#print(B)
#matrix = (A < B).astype(int)
#print(matrix)
#matrix = np.delete(matrix, [i for i, tf in enumerate(np.sum(matrix, axis=1) < [
#                           t]*n) if tf], axis=0)
#print(matrix)
#for row in matrix:
#    charrow = row.astype(str)
#    for presence in charrow:
#        print('@' if presence == '1' else '.', end=' ')
#    print('')


# def generate_bernoulli_matrix(n, m, p):
#     """
#     Generates an n x m binary matrix with entries drawn from Bernoulli(p)
    
#     Parameters:
#     n (int): number of rows
#     m (int): number of columns
#     p (float): probability of 1 in Bernoulli distribution (0 <= p <= 1)
    
#     Returns:
#     np.ndarray: n x m binary matrix
#     """
#     return np.random.binomial(1, p, size=(n, m))

# # Example usage
# n = 200
# m = 200
# p = 0.8

# t=1
# matrix = generate_bernoulli_matrix(n, m, p)
# #print(matrix)


# print(GrCovTgreedy(matrix, False, t))
# #print(GrCovTgreedy(matrix, True, t))