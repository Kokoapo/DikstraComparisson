import matplotlib.pyplot as plt
import os

PATH_G = 'grafos'
PATH_R = 'resultados'

def read_graph(n):
    graph = []
    with open(os.path.join(PATH_G, f'Entrada {n}.txt')) as f:
        f.readline()
        for line in f:
            graph.append(list(map(int, line.split())))

    return graph

def plot_and_save_all(x, y_1, y_2, filename):
    plt.plot(x, y_1)
    plt.plot(x, y_2)
    
    plt.legend(['HeapMin', 'Lista'])
    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo (s)')
    plt.title(f'Djikstra {filename}')

    plt.savefig(os.path.join(PATH_R, f'{filename}.png'))
    plt.show()