import json
from math import sqrt
from queue import PriorityQueue

def heuristic(dest, neighbour, coord):
    (x1, y1) = coord[dest]
    (x2, y2) = coord[neighbour]
    # find the straight line distance between two ndoes
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    
def a_star_search(graph, dist, cost, coord, src, dest, max_energy_cost):

    # create a priority queue
    queue = PriorityQueue()

    # push the starting index and path
    queue.put([0, 0, 0, [src]])

    # dictionary to keep track of visited node
    visited = {}

    # while the queue is not empty
    while not queue.empty():

        # pop the element with the highest priority
        e = queue.get()
        
        # get the current distance
        cur_dist = e[1]

        # get the current energy cost
        cur_cost = e[2]

        # get the current path
        cur_path = e[3]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return cur_path, cur_dist, cur_cost

        # check for the non visited nodes
        for neighbour in graph[cur_node]:

            # clone current path to a new path to
            # prevent appending to the current path
            newPath = cur_path[:]

            # append the adjacent node to the new path
            newPath.append(neighbour)

            # calculcate the new cost
            newCost = cur_cost + cost[f"{cur_node},{neighbour}"]

            # calculate the new distance
            newDist = cur_dist + dist[f"{cur_node},{neighbour}"]

            if neighbour not in visited or newDist < cur_dist:
                # check if new cost is less than the max energy cost
                if newCost <= max_energy_cost:
                    # calculate the new priority
                    priority = newDist + heuristic(dest, neighbour, coord)
                    
                    # push adjacent node with it's priority, distance and path into priority queue
                    queue.put([priority, newDist, newCost, newPath])

        # mark current ndoe as visited
        visited[cur_node] = 1

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

    # load coord from JSON
    cd = open("coord.json")
    coord = json.load(cd)

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # set max energy cost
    max_energy_cost = 287932

    # find shortest distance from source to destination node
    path, shortest_dist, total_energy_cost = a_star_search(graph, dist, cost, coord, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.")