from algorithms.generate_matrix import Matrix
from algorithms.bingreedy import bingreedy
from algorithms.delgreedy import delgreedy
from  algorithms.Grcov_greedy import GrCovTgreedy
from algorithms.IGrCov import ImpGrCov

import numpy as np
import copy
import time
import random


# def vary_n(m,d):
#     file_name = f'vary_n_t=1_m={m},d={d}.txt'
#     file_writer = open(file_name,"w")
    
#     num_samples = 10
#     x = range(60,561,10)

#     file_writer.write(f'm = {m} and delta = {d}'+'\n')
#     file_writer.write('delta'+'\n')
#     file_writer.write('average size of code'+'\n')

#     file_writer.write('5'+'\n')
#     file_writer.write('Algorithm [17]'+'\n')
#     file_writer.write('BinGreedy [4]'+'\n')
#     file_writer.write('DelGreedy'+'\n')
#     file_writer.write('GrCov'+'\n')
#     file_writer.write('GrCovNew'+'\n')
    
#     for n in x:
#         file_writer.write(str(n)+',')
#     file_writer.write('\n')
    
#     for n in x:
#         print(f"n={n}")
#         transmissions,time = sample(n,m,d,d/n,fixP=True,num_samples=num_samples)
#         file_writer.write(f"n = {n}\n")
#         file_writer.write(f"Average Transmission Lengths\n")
#         for t in transmissions:
#             file_writer.write(f"{transmissions[t]},")
#         file_writer.write('\n')
#         for t in time:
#             file_writer.write(f"{time[t]},")
#         file_writer.write('\n')

def sample(n,m,delta,t=1,w=0.6,fixP=False,num_samples=3):
    
    transmissions = {
        'bingreedy':0,
        'delgreedy':0,
        'grcov':0,
        'igrcov':0
    }
    times = {
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

        bingreedy_transmissions,bingreedy_time = bingreedy(matrix,t)
        transmissions['bingreedy'] += bingreedy_transmissions
        times['bingreedy'] += bingreedy_time

        delgreedy_transmissions, delgreedy_time = delgreedy(matrix2,t)
        transmissions['delgreedy'] += delgreedy_transmissions
        times['delgreedy'] += delgreedy_time

        grcov_transmissions,grcov_time = GrCovTgreedy(matrix3.a, False, t)
        transmissions['grcov'] += grcov_transmissions
        times['grcov'] += grcov_time

        igrcov_transmissions,igrcov_time = ImpGrCov(matrix4.a,matrix4.a.shape[0],matrix4.a.shape[1],t)
        transmissions['igrcov'] += igrcov_transmissions
        times['igrcov'] += igrcov_time
        
    for t in transmissions:
        transmissions[t] /= num_samples
        times[t] /= num_samples
        
    return transmissions,times

def vary_n(m,d):
    
    file_name = f'vary_n_t={3,7}_m={m}_d={d}.txt'
    file_writer = open(file_name,"w")
    
    num_samples = 3
    x = range(60,561,10)
    T = [3,7]
    
    file_writer.write(f'm = {m} and delta = {d}'+'\n')
    file_writer.write('delta'+'\n')
    file_writer.write('average size of code'+'\n')

    file_writer.write('4'+'\n')
    file_writer.write('BinGreedy [4]'+'\n')
    file_writer.write('DelGreedy'+'\n')
    file_writer.write('GrCov'+'\n')
    file_writer.write('GrCovNew'+'\n')
    
    for n in x:
        file_writer.write(str(n)+',')
    file_writer.write('\n')
    
    for t in T:
        file_writer.write(str(t)+',')
    file_writer.write('\n')
    
    for n in x:
        print(f'n={n}')
        file_writer.write(f"n = {n}\n")

        transmissions_across_t = []
        times_across_t = []
        
        for t in T:
            transmissions,times = sample(n,m,d,t,d/n,fixP=True,num_samples=num_samples)
            
            for k in transmissions:
                transmissions_across_t.append(transmissions[k])
            for k in times:
                times_across_t.append(times[k])
        
        file_writer.write(f"Average Transmission Lengths\n")
        for k in transmissions_across_t:
            file_writer.write(str(k)+',')
        file_writer.write('\n')
        
        file_writer.write(f"Average Times\n")
        for k in times_across_t:    
            file_writer.write(str(k)+',')
        file_writer.write('\n')
        
        print(transmissions_across_t)
        print(times_across_t)

def vary_delta(n,m):
    
    file_name = f'vary_delta_t={3,7}_n={n},m={m}.txt'
    file_writer = open(file_name,"w")
    
    num_samples = 3
    x = range(20,201,4)
    T = [3,7]
    
    file_writer.write(f'n = {n} and m = {m}'+'\n')
    file_writer.write('delta'+'\n')
    file_writer.write('average size of code'+'\n')

    file_writer.write('4'+'\n')
    file_writer.write('BinGreedy [4]'+'\n')
    file_writer.write('DelGreedy'+'\n')
    file_writer.write('GrCov'+'\n')
    file_writer.write('GrCovNew'+'\n')
    
    for d in x:
        file_writer.write(str(d)+',')
    file_writer.write('\n')
    
    for t in T:
        file_writer.write(str(t)+',')
    file_writer.write('\n')
    
    for d in x:
        print(f'd={d}, d/n = {d/n}')
        file_writer.write(f"d = {d}\n")

        transmissions_across_t = []
        times_across_t = []
        
        for t in T:
            transmissions,times = sample(n,m,d,t,d/n,fixP=True,num_samples=num_samples)
            
            for k in transmissions:
                transmissions_across_t.append(transmissions[k])
            for k in times:
                times_across_t.append(times[k])
        
        file_writer.write(f"Average Transmission Lengths\n")
        for k in transmissions_across_t:
            file_writer.write(str(k)+',')
        file_writer.write('\n')
        
        file_writer.write(f"Average Times\n")
        for k in times_across_t:    
            file_writer.write(str(k)+',')
        file_writer.write('\n')
        
        print(transmissions_across_t)
        print(times_across_t)
        
# vary_n(100,40)
vary_delta(250,100)