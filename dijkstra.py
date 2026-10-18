import heapq

def dijkstra(graph, start):

    distances = {}

    for node in graph:
        distances[node] = float('inf')

    distances[start] = 0

    pq = []

    heapq.heappush(pq, (0, start))

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                heapq.heappush(
                    pq,
                    (new_distance, neighbor)
                )

    return distances



graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2)],
    'C': [('A', 1), ('D', 3)],
    'D': [('B', 2), ('C', 3)]
}

answer = dijkstra(graph, 'A')

print(answer)
