import heapq

def djikstra_heap(graph):
    distances = [float('inf') for _ in graph]

    distances[0] = 0
    priority_queue = [(0, 0)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)        
        
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(len(graph[current_vertex])):
            if graph[current_vertex][neighbor] == 0:
                continue
            distance = current_distance + graph[current_vertex][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def djikstra_list(graph):
    distances = [float('inf') for _ in graph]

    distances[0] = 0
    unvisited_list = list(i for i in range(len(graph)))

    
    while unvisited_list:
        current_vertex = min(unvisited_list, key=lambda x: distances[x])
        unvisited_list.remove(current_vertex)

        for neighbor in range(len(graph[current_vertex])):
            if graph[current_vertex][neighbor] == 0:
                continue
            current_distance = distances[current_vertex] + graph[current_vertex][neighbor]
            if current_distance < distances[neighbor]:
                distances[neighbor] = current_distance

    return distances