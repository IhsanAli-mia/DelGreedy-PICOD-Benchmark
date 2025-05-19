from itertools import combinations
import numpy as np
from algorithms_picod1.generate_matrix import Matrix
from algorithms.generate_matrix import Matrix as Matrix_multiple
import copy

from algorithms_picod1.algorithm1 import algorithm1_picod
from algorithms_picod1.bingreedy import bingreedy
from algorithms_picod1.delgreedy import delgreedy
from  algorithms_picod1.Grcov_greedy import GrCovTgreedy
from algorithms_picod1.IGrCov import ImpGrCov

from algorithms_picodt.bingreedy import bingreedy as bingreedy_multiple
from algorithms_picodt.delgreedy import delgreedy as delreedy_multiple
from  algorithms_picodt.Grcov_greedy import GrCovTgreedy as GrCovTgreedy_multiple
from algorithms_picodt.IGrCov import ImpGrCov as ImpGrCov_multiple

## CASE 1: m = 8, d = 1,2,6,7

# m = 8

# set_degrees = [1,2,6,7]

# matrix = Matrix(80, m, 1, 0.4, w=.3, fixP=True)

# placeholder = []

# for d in set_degrees:
#     for r in combinations(range(m), d):
#         row = []
#         for i in range(m):
#             if i in r:
#                 row.append(1)
#             else:
#                 row.append(0)
#         placeholder.append(row)

# matrix.a = np.array(placeholder)
# matrix.display()


# matrix2 = copy.deepcopy(matrix)
# matrix3 = copy.deepcopy(matrix)
# matrix4 = copy.deepcopy(matrix)
# matrix5 = copy.deepcopy(matrix)


# actual_max_degree = np.max(np.sum(matrix.a, axis=0))
# algorithm_transmissions, algorithm_time = algorithm1_picod(matrix.a, actual_max_degree)

# bingreedy_transmissions,bingreedy_time = bingreedy(matrix2)

# delgreedy_transmissions, delgreedy_time = delgreedy(matrix3)

# grcov_transmissions,grcov_time = GrCovTgreedy(matrix4.a, False, 1)

# igrcov_transmissions,igrcov_time = ImpGrCov(matrix5.a,matrix5.a.shape[0],matrix5.a.shape[1],1)

# print("Algorithm1 transmissions:", algorithm_transmissions, " time:", algorithm_time)
# print("Bingreedy transmissions:", bingreedy_transmissions, " time:", bingreedy_time)
# print("Delgreedy transmissions:", delgreedy_transmissions, " time:", delgreedy_time)
# print("GrCov transmissions:", grcov_transmissions, " time:", grcov_time)
# print("IGrCov transmissions:", igrcov_transmissions, " time:", igrcov_time)


## CASE 2: m = 6, d = 1,4,5,6

# m = 6

# set_degrees = [1,4,5,6]

# print("m = 6, d = 1,4,5,6")

# matrix = Matrix(80, m, 1, 0.4, w=.3, fixP=True)

# placeholder = []
# for d in set_degrees:
#     for r in combinations(range(m), d):
#         row = []
#         for i in range(m):
#             if i in r:
#                 row.append(1)
#             else:
#                 row.append(0)
#         placeholder.append(row)
        
# matrix.a = np.array(placeholder)
# # matrix.display()
# print(matrix.a.shape)

# matrix2 = copy.deepcopy(matrix)
# matrix3 = copy.deepcopy(matrix)
# matrix4 = copy.deepcopy(matrix)
# matrix5 = copy.deepcopy(matrix)

# actual_max_degree = np.max(np.sum(matrix.a, axis=0))
# algorithm_transmissions, algorithm_time = algorithm1_picod(matrix.a, actual_max_degree)

# bingreedy_transmissions,bingreedy_time = bingreedy(matrix2)

# delgreedy_transmissions, delgreedy_time = delgreedy(matrix3)

# grcov_transmissions,grcov_time = GrCovTgreedy(matrix4.a, False, 1)

# igrcov_transmissions,igrcov_time = ImpGrCov(matrix5.a,matrix5.a.shape[0],matrix5.a.shape[1],1)

# print(f"t = {1}")
# print("Algorithm1 transmissions:", algorithm_transmissions, " time:", algorithm_time)
# print("Bingreedy transmissions:", bingreedy_transmissions, " time:", bingreedy_time)
# print("Delgreedy transmissions:", delgreedy_transmissions, " time:", delgreedy_time)
# print("GrCov transmissions:", grcov_transmissions, " time:", grcov_time)
# print("IGrCov transmissions:", igrcov_transmissions, " time:", igrcov_time)
# print("------------------------------------------------------")

## CASE 3: m = 6, d = 2,3

# m = 6

# set_degrees = [2,3]

# print("m = 6, d = 2,3")

# for t in range(1,4):
    
#     print(f"t={t}")

#     matrix = Matrix_multiple(80, m, 1, 0.4, w=.3, fixP=True)

#     placeholder = []
#     for d in set_degrees:
#         for r in combinations(range(m), d):
#             row = []
#             for i in range(m):
#                 if i in r:
#                     row.append(1)
#                 else:
#                     row.append(0)
#             placeholder.append(row)

#     matrix.a = np.array(placeholder)
#     n,m = matrix.a.shape
    
#     # matrix.display()
#     print(matrix.a.shape)

#     matrix2 = copy.deepcopy(matrix)
#     matrix3 = copy.deepcopy(matrix)
#     matrix4 = copy.deepcopy(matrix)
#     matrix5 = copy.deepcopy(matrix)

#     bingreedy_transmissions, bingreedy_time = bingreedy_multiple(matrix,t)
#     delgreedy_transmissions, delgreedy_time = delreedy_multiple(matrix2,t)
#     grcov_transmissions, grcov_time = GrCovTgreedy_multiple(matrix3.a,False,t)
#     igrcov_transmissions,igrcov_time = ImpGrCov_multiple(matrix4.a,n,m,t)
    
#     print("Bingreedy transmissions:", bingreedy_transmissions, " time:", bingreedy_time)
#     print("Delgreedy transmissions:", delgreedy_transmissions, " time:", delgreedy_time)
#     print("GrCov transmissions:", grcov_transmissions, " time:", grcov_time)
#     print("IGrCov transmissions:", igrcov_transmissions, " time:", igrcov_time)
#     print("------------------------------------------------------")
    
# matrix = Matrix_multiple(80, 5, 1, 0.4, w=.3, fixP=True)
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
    
# print(bingreedy(matrix))

# matrix = Matrix_multiple(80, 5, 1, 0.4, w=.3, fixP=True)
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
# print(bingreedy_multiple(matrix,1))
