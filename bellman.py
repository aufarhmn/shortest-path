def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Negative weight cycle detected")

    return distances

graph = {
    'START': {'A': 67, 'B': 120},
    'A': {'B': 102, 'J': 260},
    'B': {'D':16, 'E': 52},
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
    'R': {'Q': 67, 'S':55},
    'S': {'U': 60},
    'T': {'END': 55},
    'U': {'END': 7},
    'V': {'T': 16},
    'W': {'T': 10},
    'END': {}
}

distances = bellman_ford(graph, 'START')
print(distances)