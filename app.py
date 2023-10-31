#!/usr/bin/python3
"""
This module assumess the source to be
Dedza and Destination Nkhotakota
"""
from algorithm_module.dijkstra import Graph, Dijkstra


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("Dedza")
    graph.add_vertex("Salima")
    graph.add_vertex("Nkhotakota")
    graph.add_vertex("Ntcheu")
    graph.add_vertex("Lilongwe")
    graph.add_vertex("Dowa")
    graph.add_vertex("Ntchisi")
    graph.add_vertex("Kasungu")
    graph.add_vertex("Mchinji")

    graph.add_edge("Ntcheu", "Dedza", 74)
    graph.add_edge("Dedza", "Salima", 96)
    graph.add_edge("Dedza", "Lilongwe", 92)
    graph.add_edge("Lilongwe", "Dowa", 55)
    graph.add_edge("Lilongwe", "Mchinji", 109)
    graph.add_edge("Mchinji", "Kasungu", 141)
    graph.add_edge("Kasungu", "Dowa", 117)
    graph.add_edge("Kasungu", "Ntchisi", 66)
    graph.add_edge("Dowa", "Ntchisi", 38)
    graph.add_edge("Dowa", "Salima", 67)
    graph.add_edge("Ntchisi", "Nkhotakota", 66)
    graph.add_edge("Nkhotakota", "Salima", 112)

    dijkstra = Dijkstra(graph)
    dijkstra.calculate_shortest_distances("Dedza")

    target_vertex = "Nkhotakota"
    shortest_path = dijkstra.get_shortest_path(target_vertex)

    if target_vertex in shortest_path:
        print(f"Shortest path from 'Dedza' to 'Nkhotakota' is: \n[{', '.join(shortest_path)}]")
        print(f"Path Cost: {dijkstra.distances[target_vertex]}")
    else:
        print(f"No path from 'Dedza' to '{target_vertex}'")
