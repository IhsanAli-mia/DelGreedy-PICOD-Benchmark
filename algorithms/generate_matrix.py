import numpy as np

class Matrix:
    
    np.random.seed(42)
    
    dimentions = np.array([0, 0])
    counter = 0
    
    def __init__(self, n, m, t, delta, w, fixP=False):
        """Initialize matrix
        n: number of vertices
        m: number of hyperedges
        t: minimum vertex degree
        delta: maximum vertex degree
        w: weight parameter for random matrix generation
        fixP: whether to use fixed probability
        """
        if not fixP:
            self.a = self.random4(n, m, t, delta, w)
        else:
            self.a = self.randomP(n, m, t, delta, w)
        self.unique()
        self.dimentions = self.dimentions + self.a.shape
        self.counter += 1
        
    def unique(self):
        self.a = np.unique(self.a, axis=0)  # remove duplicate rows
        self.a = np.unique(self.a, axis=1)  # remove duplicate columns
        if self.a[0,].sum() == 0:
            self.a = self.a[1:,]
            
    def random4(self, n, m, t, d, w):
        # w=0.6
        # nt<<md
        p = (((1-w)*n*t+m*d*w))/(m*n)
        A = np.random.uniform(0, 1, size=(n, m))
        B = p*np.ones(shape=(n, m))
        matrix = (A < B).astype(int)
        # matrix = np.delete(matrix, [i for i, tf in enumerate(np.sum(matrix, axis=1) < [t]*n) if tf], axis=0)
        return matrix
        
    def randomP(self, n, m, t, d, p):
        A = np.random.uniform(0, 1, size=(n, m))
        B = p*np.ones(shape=(n, m))
        matrix = (A < B).astype(int)
        # matrix = np.delete(matrix, [i for i, tf in enumerate(np.sum(matrix, axis=1) < [t]*n) if tf], axis=0)
        return matrix
        
    def matrix_sort(self):
        n, m = self.a.shape
        available = [True]*n
        # loop for sorting the messages by effectve degree
        for first_message in range(m):
            # pick 1st message with maximum effective degree
            message = self.a.T.dot(available).argmax()
            # update available clients
            if self.a.T.dot(available).max().round().astype(int) == 0:
                break
            available = np.multiply(available, np.logical_not(self.a[:, message]))
            # swap maximum effective degree message column with first unsorted message column
            temp = self.a[:, first_message].copy()
            self.a[:, first_message] = self.a[:, message].copy()
            self.a[:, message] = temp
        # sort clients in lexicographic order
        self.a = self.a[np.lexsort(np.rot90(self.a))]
        self.a = np.flip(self.a, axis=0)
        
    def display(self):
        for row in self.a:
            for presence in row:
                print('@' if presence == 1 else '.', end=' ')
            print('')
        print('-----------------')