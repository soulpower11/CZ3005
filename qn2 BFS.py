import collections
import json

def bfs(graph, dist, cost, src, dest, max_energy_cost):

    visited, queue = set(), collections.deque()
    visited.add(src)

    queue.append([0, 0, [src]])

    while queue:

        # Dequeue a vertex from queue
        e = queue.popleft()

        # get the current distance
        cur_dist = e[0]

        # get the current energy cost
        cur_cost = e[1]

        # get the current path
        cur_path = e[2]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        if(cur_node == dest):
            return cur_path, cur_dist, cur_cost

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[cur_node]:
            if neighbour not in visited:
                visited.add(neighbour)

                newPath = cur_path[:]
                newPath.append(neighbour)

                # calculcate the new cost
                newCost = cur_cost + cost[f"{cur_node},{neighbour}"]

                # calculate the new distance
                newDist = cur_dist + dist[f"{cur_node},{neighbour}"]

                queue.append([newDist, newCost, newPath])

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

    path, shortest_dist, total_energy_cost = bfs(graph, dist, cost, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.")