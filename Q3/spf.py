import networkx as nx
import numpy as np

def dijkstra(A):
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    n = A.shape[0]
    path_1_to_n = nx.dijkstra_path(G, 0, n-1) # path from host 1 to host 2
    path_n_to_1 = nx.dijkstra_path(G, n-1, 0) # path from host 2 to host 1
    # printing path
    print(f"Path from 1 to {n} is: ", end='')
    for i in path_1_to_n:
        print(f's{i+1} ', end='')
    print()
    print(f"Path from {n} to 1 is: ", end='')
    for i in path_n_to_1:
        print(f's{i+1} ', end='')
    print()
    return path_1_to_n, path_n_to_1

    

if __name__=='__main__':
    A = np.array([
        [0, 2, 3, 4],
        [2, 0, 0, 1],
        [3, 0, 0, 0],
        [1, 1, 0, 0]
    ])
    dijkstra(A)