import random

class AntColony:
    def __init__(self, graph, n_ants, n_iterations, evaporation_rate, alpha, beta):
        self.graph = graph
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.pheromones = {(node, edge): 1 for node in graph for edge in graph[node]}

    def find_shortest_path(self, start, end):
        best_path = None
        best_distance = float('inf')

        for _ in range(self.n_iterations):
            ants_paths = [self.ant_walk(start, end) for _ in range(self.n_ants)]
            for path, distance in ants_paths:
                if distance < best_distance:
                    best_distance = distance
                    best_path = path
            self.update_pheromones(ants_paths)

        return best_path, best_distance

    def ant_walk(self, start, end):
        path = [start]
        distance = 0

        while path[-1] != end:
            node = path[-1]
            neighbors = list(self.graph[node].keys())
            probabilities = [self.pheromones[(node, neighbor)]**self.alpha *
                             (1 / self.graph[node][neighbor])**self.beta
                             for neighbor in neighbors]

            total_probability = sum(probabilities)
            probabilities = [p / total_probability for p in probabilities]

            next_node = random.choices(neighbors, probabilities)[0]
            path.append(next_node)
            distance += self.graph[node][next_node]

        return path, distance

    def update_pheromones(self, ants_paths):
        for node in self.graph:
            for edge in self.graph[node]:
                self.pheromones[(node, edge)] *= (1 - self.evaporation_rate)

        for path, distance in ants_paths:
            for i in range(len(path) - 1):
                self.pheromones[(path[i], path[i + 1])] += 1 / distance

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

ant_colony = AntColony(graph, n_ants=10, n_iterations=5000, evaporation_rate=0.1, alpha=1, beta=5)
shortest_path, shortest_distance = ant_colony.find_shortest_path('START', 'END')
print("Shortest path:", shortest_path)
print("Shortest path distance:", shortest_distance)