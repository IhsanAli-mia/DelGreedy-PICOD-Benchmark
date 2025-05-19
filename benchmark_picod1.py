from algorithms_picod1.generate_matrix import Matrix
from algorithms_picod1.algorithm1 import algorithm1_picod
from algorithms_picod1.bingreedy import bingreedy
from algorithms_picod1.delgreedy import delgreedy
from  algorithms_picod1.Grcov_greedy import GrCovTgreedy
from algorithms_picod1.IGrCov import ImpGrCov

import numpy as np
import copy
# import time
import random

def sample(n,m,delta,w=0.6,fixP=False,num_samples=3):
    
    transmissions = {
        'algorithm1': 0,
        'bingreedy':0,
        'delgreedy':0,
        'grcov':0,
        'igrcov':0
    }
    times = {
        'algorithm1': 0,
        'bingreedy':0,
        'delgreedy':0,
        'grcov':0,
        'igrcov':0
    }
    
    for i in range(num_samples):
    
        matrix = Matrix(n, m, 1, delta, w, fixP=fixP)

        matrix2 = copy.deepcopy(matrix)
        matrix3 = copy.deepcopy(matrix)
        matrix4 = copy.deepcopy(matrix)
        matrix5 = copy.deepcopy(matrix)
        
        actual_max_degree = np.max(np.sum(matrix.a, axis=0))
        algorithm_transmissions, algorithm_time = algorithm1_picod(matrix.a, actual_max_degree)
        transmissions['algorithm1'] += algorithm_transmissions
        times['algorithm1'] += algorithm_time

        bingreedy_transmissions,bingreedy_time = bingreedy(matrix2)
        transmissions['bingreedy'] += bingreedy_transmissions
        times['bingreedy'] += bingreedy_time

        delgreedy_transmissions, delgreedy_time = delgreedy(matrix3)
        transmissions['delgreedy'] += delgreedy_transmissions
        times['delgreedy'] += delgreedy_time

        grcov_transmissions,grcov_time = GrCovTgreedy(matrix4.a, False, 1)
        transmissions['grcov'] += grcov_transmissions
        times['grcov'] += grcov_time

        igrcov_transmissions,igrcov_time = ImpGrCov(matrix5.a,matrix5.a.shape[0],matrix5.a.shape[1],1)
        transmissions['igrcov'] += igrcov_transmissions
        times['igrcov'] += igrcov_time
        
    for t in transmissions:
        transmissions[t] /= num_samples
        times[t] /= num_samples
        
    return transmissions,times
        
    
def vary_n(m,d):
    file_name = f'vary_n_t=1_m={m},d={d}.txt'
    file_writer = open(file_name,"w")
    
    num_samples = 10
    x = range(60,561,10)

    file_writer.write(f'm = {m} and delta = {d}'+'\n')
    file_writer.write('delta'+'\n')
    file_writer.write('average size of code'+'\n')

    file_writer.write('5'+'\n')
    file_writer.write('Algorithm [17]'+'\n')
    file_writer.write('BinGreedy [4]'+'\n')
    file_writer.write('DelGreedy'+'\n')
    file_writer.write('GrCov'+'\n')
    file_writer.write('GrCovNew'+'\n')
    
    for n in x:
        file_writer.write(str(n)+',')
    file_writer.write('\n')
    
    for n in x:
        print(f"n={n}")
        transmissions,time = sample(n,m,d,d/n,fixP=True,num_samples=num_samples)
        file_writer.write(f"n = {n}\n")
        file_writer.write(f"Average Transmission Lengths\n")
        for t in transmissions:
            file_writer.write(f"{transmissions[t]},")
        file_writer.write('\n')
        for t in time:
            file_writer.write(f"{time[t]},")
        file_writer.write('\n')

def vary_delta(n,m):
    file_name = f'vary_delta_t=1_n={n},m={m}.txt'
    file_writer = open(file_name,"w")
    
    num_samples = 10
    x = range(20,201,4)
    
    file_writer.write(f'n = {n} and m = {m}'+'\n')
    file_writer.write('delta'+'\n')
    file_writer.write('average size of code'+'\n')

    file_writer.write('5'+'\n')
    file_writer.write('Algorithm [17]'+'\n')
    file_writer.write('BinGreedy [4]'+'\n')
    file_writer.write('DelGreedy'+'\n')
    file_writer.write('GrCov'+'\n')
    file_writer.write('GrCovNew'+'\n')
    
    for delta in x:
        file_writer.write(str(delta)+',')
    file_writer.write('\n')
    
    for delta in x:
        print(f'delta,delta/n={delta},{delta/n}')
        transmissions,time = sample(n,m,delta,delta/n,fixP=True,num_samples=num_samples)
        # print(transmissions)
        # print(time)
        file_writer.write(f"Delta = {delta}\n")
        file_writer.write("Average Transmission Lengths\n")
        for t in transmissions:
            file_writer.write(f"{transmissions[t]},")
        file_writer.write('\n')
        for t in time:
            file_writer.write(f"{time[t]},")
        file_writer.write('\n')
        
        
def vary_p(n,m):
    file_name = f'vary_p_t=1_n={n},m={m}.txt'
    file_writer = open(file_name,"w")
    
    num_samples = 10
    x = range(2,32,2)
    
    file_writer.write(f'n = {n} and m = {m}'+'\n')
    file_writer.write('p'+'\n')
    file_writer.write('average size of code'+'\n')

    file_writer.write('5'+'\n')
    file_writer.write('BinGreedy [4]'+'\n')
    file_writer.write('Algorithm [17]'+'\n')
    file_writer.write('DelGreedy'+'\n')
    file_writer.write('GrCov'+'\n')
    file_writer.write('GrCovNew'+'\n')
    
    for delta in x:
        delta = delta/100
        file_writer.write(str(delta)+',')
    file_writer.write('\n')
    
    for delta in x:
        transmissions,time = sample(n,m,delta,delta/100,fixP=True,num_samples=num_samples)
        file_writer.write(f"p = {delta/100}\n")
        file_writer.write("Average Transmission Lengths\n")
        for t in transmissions:
            file_writer.write(f"{transmissions[t]},")
        file_writer.write('\n')
        for t in time:
            file_writer.write(f"{time[t]},")
        file_writer.write('\n')
        
# vary_n(100,40)
vary_delta(250,100)
# vary_p(200,100)
    
# n=20
# m=6
# # # # Generate incidence matrix
# matrix = Matrix(n, m, t, delta, w=.3, fixP=True)
# # print("Generated Incidence Matrix:")
# matrix.display()

# # matrix2 = copy.deepcopy(matrix)
# matrix3 = copy.deepcopy(matrix)
# # matrix4 = copy.deepcopy(matrix)
# # matrix5 = copy.deepcopy(matrix)

# actual_max_degree = np.max(np.sum(matrix.a, axis=0))
# algorithm_transmissions, algorithm_time = algorithm1_picod(matrix.a, actual_max_degree)

# # bingreedy_transmissions,bingreedy_time = bingreedy(matrix2)

# delgreedy_transmissions, delgreedy_time = delgreedy(matrix3)

# # grcov_transmissions,grcov_time = GrCovTgreedy(matrix4.a, False, 1)

# # igrcov_transmissions,igrcov_time = ImpGrCov(matrix5.a,matrix5.a.shape[0],matrix5.a.shape[1],1)

# print(algorithm_transmissions,delgreedy_transmissions,)

# print(transmissions)
