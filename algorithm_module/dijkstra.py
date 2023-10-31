#!/usr/bin/python3
"""
This module contains classess that sets up a weighted graph data structure
"""
import heapq


class Graph:
    """
    Weighted undirected Graph
    """
    def __init__(self):
        """
        sets vertices to empty set
        and edges to empty dictionary
        """
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, vertex):
        """
        adds a vertex which is a node
        for our graph
        """
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, start, end, weight):
        """
        adds an edge
        """
        self.edges[start].append((end, weight))
        self.edges[end].append((start, weight))


class Dijkstra:
    """
    implementantion of dijkstras algo
    """
    def __init__(self, graph):
        """sets graphs, distances and previous node"""
        self.graph = graph
        self.distances = {}
        self.previous = {}

    def calculate_shortest_distances(self, start_vertex):
        queue = [(0, start_vertex)]
        self.distances[start_vertex] = 0

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > self.distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.edges[current_vertex]:
                distance = current_distance + weight

                if neighbor not in self.distances or \
                        distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

    def get_shortest_path(self, target_vertex):
        path = []
        while target_vertex:
            path.insert(0, target_vertex)
            target_vertex = self.previous.get(target_vertex)
        return path
