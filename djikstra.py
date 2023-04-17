import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    previous_vertices = {vertex: None for vertex in graph}
    
    priority_queue = [(0, start)]
    
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex == end:
            path = []
            while previous_vertices[current_vertex] is not None:
                path.insert(0, current_vertex)
                current_vertex = previous_vertices[current_vertex]
            path.insert(0, start)
            return (distances[end], path)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return None

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
distance, path = dijkstra(graph, 'START', 'END')
print(f"Shortest distance: {distance}")
print(f"Shortest path: {' -> '.join(path)}")