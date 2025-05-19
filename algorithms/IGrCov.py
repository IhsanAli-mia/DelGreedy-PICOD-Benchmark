import numpy as np
from math import floor, ceil
import pandas as pd
import time
#import matplotlib.pyplot as plt
#from generate import Matrix

def SRD(B, G, H, j, m):
    T = np.zeros(m, dtype=int)
    B_j = [k for k in B if G[j][k] == 1]

    for k in B_j:
        T[H[j][k]] += 1

    I = [k for k in range(m) if T[k] % 2 == 1]

    if len(I) == 1:
        i = min(I)
        T_set = {k for k in range(m) if H[j][k] == i}
        return T_set
    return set()

def RepUpdate(B, G, H, n, m):
    for j in range(n):
        T = np.zeros(m, dtype=int)
        B_j = [k for k in B if G[j][k] == 1]

        for k in B_j:
            T[H[j][k]] += 1

        I_j = [k for k in range(m) if T[k] % 2 == 1]

        if len(I_j) == 2:
            i1 = min(I_j)
            i2 = max(I_j)
            T_set = [k for k in range(m) if H[j][k] == i2]
            for k in T_set:
                H[j][k] = i1
    return H

def ImpGrCov(Matrix, n, m, t):
    start = time.time()
    
    W = [min(t, sum(Matrix[j])) for j in range(n)]
    # print(W)
    H = np.zeros((n, m), dtype=int)
    for j in range(n):
        for l in range(m):
            H[j][l] = l
    #print(H)
    C = set()
    U = set(range(n))
    #print(U)
    iterations=0
    while U:
        #iterations+=1
        B = set()
        delta = 0
        Flag = True
        S = [[set() for _ in range(m)] for _ in range(n)]
        #print(S)
        while Flag:
            Delta = dict()
            for k in set(range(m)) - B:
                l=[]
                for j in U:
                    S[j][k] = SRD(B | {k}, Matrix, H, j, m)
                    l = [min(len(S[j][k]), W[j]) for j in range(n)]
            #Delta[k] = Delta.get(k, 0) + 2 ** (W[j] * (1 - 2 - l_jk))
                Delta[k] = sum(2 **W[j] - 2 **(W[j]- l[j]) for j in U)
            #print(Delta)
            #print(S)
            #print('_______________________')
            if Delta:
                max_k, max_val = max(Delta.items(), key=lambda item: item[1])
                #print(max_k)
                #print(max_val)
                if max_val > delta:
                    delta = max_val
                    B.add(max_k)
                    S1=S
                    #print(S1)
                    k_star=max_k
                else:
                    Flag = False
            else:
                Flag = False
            #print(B)
        C = C.union(B)
        iterations=iterations+1
        #print("iterations=",iterations)
        #print(S1)
        for j in list(U):
            #print(S1)
            l_jk_star = len(S1[j][k_star])
            #print(l_jk_star)
            #print("befor",W[j])
            W[j] -= l_jk_star
            #print("after", W[j])
            #W[j]-=l[j]
        
            if W[j] <= 0:
                U.remove(j)
        #print("W=",W)
        #print("U", U)
        for j in range(n):
            for l in S1[j][k_star]:
                Matrix[j][l] = 0
        #print(Matrix)
        H = RepUpdate(B, Matrix, H, n, m)
    # print(iterations)
    
    time_taken = time.time() - start
    
    return iterations , time_taken
    
#matrix=np.array([[1,0,0,0,1,0],
#                [1,0,0,0,0,1], 
#               [1,1,0,0,0,0], 
#                [0,1,0,0,1,0], 
#                [0,1,0,0,0,1], 
#                [0,0,1,0,1,1], 
#                [0,0,1,1,0,0], 
#                [1,0,1,1,1,0]])
#n,m=matrix.shape
#t=3




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
# n = 100
# m = 100
# p = 0.5

# t=20
# matrix = generate_bernoulli_matrix(n, m, p)
# #print(matrix)
# print(ImpGrCov(matrix, n,m, t))
