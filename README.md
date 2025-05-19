# DelGreedy vs. SOTA PICOD Algorithms Benchmark

A comparative evaluation of DelGreedy against state-of-the-art algorithms for PICOD-1 (t=1) and PICOD-t (t>1) problems.

## Overview

This repository contains implementations and benchmarking code for multiple algorithms solving the PICOD (Pliable Index Coding) problem:


<ul>
  <li><b>DelGreedy</b> (Our proposed algorithm)</li>
  <li><b>Algorithm 1</b> From <a href='https://arxiv.org/abs/2208.10389'>paper</a></li>
  <li><b>BinGreedy</b> From <a href='https://arxiv.org/abs/1601.05516'>paper</a></li>
  <li><b>GRCOV</b> From <a href='https://ieeexplore.ieee.org/document/7254174'>paper</a></li>
  <li><b>ImpGrCov</b> From <a href='https://ieeexplore.ieee.org/document/10313405'>paper</a></li>
</ul>

The goal is to compare DelGreedy's performance (average time taken and average number of transmissions) against existing approaches in both:

<ul>
  <li><b>PICOD-1</b> (Single round case, t = 1)</li>
  <li><b>PICOD-t</b> (Multi round case, t > 1)</li>
</ul>

## Setup and Installation

1.Clone the repo:

```bash
https://github.com/IhsanAli-mia/DelGreedy-PICOD-Benchmark.git
cd DelGreedy-PICOD-Benchmark
```
2. Install dependencies:
```bash
pip install numpy
```
3. Run benchmarks:
```bash
python benchmark_picod1.py  # For t=1 case  
python benchmark_picodt.py   # For t>1 case
```

## Repository Structure
```bash
├── algorithms/  
│   ├── picod1/                  # Algorithms for PICOD-1 (t=1)  
│   │   ├── algorithm1.py  
│   │   ├── bingreedy.py  
│   │   ├── delgreedy.py         
│   │   ├── generate_matrix.py  
│   │   ├── Grow_greedy.py  
│   │   └── lGrCov.py  
│   │  
│   └── picodt/                  # Algorithms for PICOD-t (t>1)  
│       ├── bingreedy.py  
│       ├── delgreedy.py  
│       ├── generate_matrix.py  
│       ├── Grow_greedy.py  
│       └── lGrCov.py  
│  
├── benchmarks/  
│   ├── benchmark_picod1.py       # Benchmark script for PICOD-1  
│   └── benchmark_picodt.py       # Benchmark script for PICOD-t  
│  
├── example.py                   # Example usage or demo  
├── README.md                    # Project documentation  
└── .gitignore                   # Ignore files (e.g., __pycache__)  
```

