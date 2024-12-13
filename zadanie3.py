import heapq

def dijkstra(graph, start):

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

start_vertex = 'A'
distances, predecessors = dijkstra(graph, start_vertex)

print("Najkrótsze odległości od wierzchołka startowego:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")

print("\nPoprzednicy na najkrótszych ścieżkach:")
for vertex, predecessor in predecessors.items():
    print(f"{vertex}: {predecessor}")
