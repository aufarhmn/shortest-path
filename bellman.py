def bellman_ford(graph, start):
    distance = {}
    predecessor = {}

    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None

    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                new_distance = distance[node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    predecessor[neighbor] = node

    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Negative cycle detected")

    return distance, predecessor

def get_shortest_path(graph, start, end):
    distance, predecessor = bellman_ford(graph, start)

    path = [end]
    while path[-1] != start:
        path.append(predecessor[path[-1]])
    path.reverse()

    return path, distance[end]

graph = {
    'START': {'A': 67, 'B': 120},
    'A': {'B': 102, 'J': 260},
    'B': {'D': 16, 'E': 52},
    'C': {'O': 68, 'L': 49},
    'D': {'F': 52},
    'E': {'F': 19, 'G': 16},
    'F': {'I': 17, 'H': 11},
    'G': {'H': 20, 'J': 70},
    'H': {'K': 69},
    'I': {'M': 78},
    'J': {'L': 55},
    'K': {'M': 29, 'C': 10},
    'L': {'N': 69, 'Q': 100, 'C': 49},
    'M': {'O': 44},
    'N': {'P': 56},
    'O': {'R': 37},
    'P': {'Q': 110},
    'Q': {'V': 11},
    'R': {'Q': 67, 'S': 55},
    'S': {'U': 60},
    'T': {'END': 55},
    'U': {'END': 7},
    'V': {'T': 16},
    'W': {'T': 10},
    'END': {}
}

path, distance = get_shortest_path(graph, 'START', 'END')
print("Shortest path:", path)
print("Shortest path distance:", distance)