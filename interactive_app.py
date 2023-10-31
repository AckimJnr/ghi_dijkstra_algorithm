#!/usr/bin/python3
"""
This module allows the user to select source and destination districts.
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

    district_mapping = {
        '1': 'Dedza',
        '2': 'Salima',
        '3': 'Nkhotakota',
        '4': 'Ntcheu',
        '5': 'Lilongwe',
        '6': 'Dowa',
        '7': 'Ntchisi',
        '8': 'Kasungu',
        '9': 'Mchinji',
    }

    for key, value in district_mapping.items():
        print("{}. {}".format(key, value))

    source_district = input("Enter the source district (1 - 9): ")
    destination_district = input("Enter the destination district (1 - 9): ")
    source = district_mapping.get(source_district)
    destination = district_mapping.get(destination_district)

    if source and destination:
        dijkstra.calculate_shortest_distances(source)
        shortest_path = dijkstra.get_shortest_path(destination)

        if destination in shortest_path:
            print(f"Shortest path from '{source}' to '{destination}' is: \n[{', '.join(shortest_path)}]")
            print(f"Path Cost: {dijkstra.distances[destination]}")
        else:
            print(f"No path from '{source}' to '{destination}'")
    else:
        print("Invalid district numbers. Please enter numbers from 1 to 9 for source and destination.")
