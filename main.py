import json
from Task1 import dijkstra_without_budget 
from Task2 import dijkstra_with_budget 
from Task3 import a_star_search 

if __name__ == '__main__':

    # load graph from JSON
    g = open("G.json")
    graph = json.load(g)

    # load distance from JSON
    d = open("Dist.json")
    dist = json.load(d)

    # load cost from JSON
    c = open("Cost.json")
    cost = json.load(c)

    # load coord from JSON
    cd = open("coord.json")
    coord = json.load(cd)

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # set max energy cost
    max_energy_cost = 287932

    print("Task 1 - Uniform Cost Search to solve a relaxed version of the NYC instance where we do not have the energy constraint")

    # find shortest distance from source to destination node without energy budget using Uniform Cost Search
    path, shortest_dist = dijkstra_without_budget(graph, dist, src, dest)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.\n")

    print("Task 2 - Uniform Cost Search to solve the NYC instance")

    # find shortest distance from source to destination node with energy budget using Uniform Cost Search
    path, shortest_dist, total_energy_cost = dijkstra_with_budget(graph, dist, cost, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.\n")

    print("Task 3 - A* search algorithm to solve the NYC instance")

    # find shortest distance from source to destination node with energy budget using A* Search
    path, shortest_dist, total_energy_cost = a_star_search(graph, dist, cost, coord, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.\n")