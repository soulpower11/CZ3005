import json
import math
from queue import PriorityQueue

def dijkstra_with_budget(graph, dist, cost, src, dest, max_energy_cost):

    # create a priority queue
    queue = PriorityQueue()

    # push the starting index and path
    queue.put([0, 0, [src]])

    # dictionary to keep track of visited node
    visited = {}

    # dictionary to keep track of the node distance
    # for checking if there's another shortest path
    distance = {src: math.inf}

    # dictionary to keep track of the node energy cost
    # for checking if there's another lower energy cost
    energy = {src: math.inf}

    # while the queue is not empty
    while queue:

        # pop the element with the highest priority
        e = queue.get()

        # get the current distance
        cur_dist = e[0]

        # get the current energy cost
        cur_cost = e[1]

        # get the current path
        cur_path = e[2]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        # mark current ndoe as visited
        visited[cur_node] = 1

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return cur_path, cur_dist, cur_cost

        # check for adjacent node
        for neighbour in graph[cur_node]:
            
            # if the distance for this not is not initialized
            if neighbour not in distance:
                # initialized the node distance
                distance[neighbour] = math.inf
            
            # if the energy for this not is not initialized
            if neighbour not in energy:
                # initialized the node energy cost
                energy[neighbour] = math.inf
            
            # clone current path to a new path to 
            # prevent appending to the current path
            newPath = cur_path[:]
            # append the adjacent node to the new path
            newPath.append(neighbour)

            # calculcate the new cost
            newCost = cur_cost + cost[f"{cur_node},{neighbour}"]

            # calculate the new distance
            newDist = cur_dist + dist[f"{cur_node},{neighbour}"]

            # if adjacent node is not in visted and if the new distance smaller than the old distance
            # or if the new energy cost is smaller than the old energy cost
            if neighbour not in visited and distance[neighbour] > newDist or energy[neighbour] > newCost:
                # check if new cost is within the budget
                if newCost <= max_energy_cost:
                    # push adjacent node with it's distance and path into priority queue
                    queue.put([newDist, newCost, newPath])
                    # update the distance of the node
                    distance[neighbour] = newDist
                    # update the distance of the node
                    energy[neighbour] = newCost

# main function
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

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # set max energy cost
    max_energy_cost = 287932

    # find shortest distance from source to destination node
    path, shortest_dist, total_energy_cost = dijkstra_with_budget(graph, dist, cost, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.")
