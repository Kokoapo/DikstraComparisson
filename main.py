import time
from graph import read_graph, plot_and_save_all
from djikstra import djikstra_heap, djikstra_list

N_ITERS = 100 # Quantas vezes cada valor de entrada vai ser testado

inputs = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 650, 800, 1000, 1500]

n_s = []
h_s = []
l_s = []

for n in inputs:
    time_h = 0
    time_l = 0
    
    for i in range(N_ITERS):
        graph = read_graph(n)

        start = time.time()
        h = djikstra_heap(graph)
        time_h += time.time() - start

        start = time.time()
        l = djikstra_list(graph)
        time_l += time.time() - start

    time_h = time_h/N_ITERS
    time_l = time_l/N_ITERS

    n_s.append(n)
    h_s.append(time_h)
    l_s.append(time_l)

    print(f'Entrada {n}: HeapMin = {time_h:.6f}s, Lista = {time_l:.6f}s')
    '''if h==l:
        print("As distâncias alcançadas por ambos métodos são iguais")
    else:
        print("As distâncias alcançadas pelos métodos diferem")'''

plot_and_save_all(n_s, h_s, l_s, 'Comparativo')