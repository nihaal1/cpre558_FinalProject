#!/usr/bin/env python

import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # Assuming an undirected graph

def dijkstra(graph, start):
    distances = [float('inf')] * graph.vertices
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Simulate CPU-intensive task
        cpu_intensive_task(current_vertex)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def cpu_intensive_task(vertex):
    # Simulate CPU-intensive task
    for _ in range(1000000):
        _ = vertex * vertex

if __name__ == "__main__":
    # Create a sample graph
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 7)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 1)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 3, 6)
    
    start_vertex = 0
    for i in range(3):
        result = dijkstra(g, start_vertex)
        print(f"Shortest distances from vertex {start_vertex}: {result}")

