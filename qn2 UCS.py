import json

def ucs(graph, dist, cost, src, dest, max_energy_cost):

    # create a priority queue
    queue = []

    # push the starting index
    queue.append([0, 0, [src]])

    # dictionary to keep track of visited node
    visited = {}

    # while the queue is not empty
    while queue:

        # sort the queue so that the element with the highest priority is the last element
        queue = sorted(queue)
        e = queue[-1]

        # pop the element with the highest priority
        del queue[-1]

        # get the current distance
        cur_dist = e[0] * -1

        # get the current energy cost
        cur_cost = e[1]

        # get the current path
        cur_path = e[2]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return cur_path, cur_dist, cur_cost

        # check for the non visited nodes
        if cur_node not in visited:
            for i in range(len(graph[str(cur_node)])):

                # clone current path to a new path to
                # prevent appending to the current path
                newPath = cur_path[:]

                # append the adjacent node to the new path
                newPath.append(graph[str(cur_node)][i])

                # calculcate the new cost
                newCost = cur_cost + cost[f"{cur_node},{graph[str(cur_node)][i]}"]

                # calculate the new distance
                # new distance is multiplied by -1 so that
                # least priority is at the top
                newDist = (cur_dist + dist[f"{cur_node},{graph[str(cur_node)][i]}"]) * -1

                # check if new cost is less than the max energy cost
                if newCost <= max_energy_cost:
                    # push adjacent node with it's distance and path into priority queue
                    queue.append([newDist, newCost, newPath])

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

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # set max energy cost
    max_energy_cost = 287932

    # find shortest distance from source to destination node
    path, shortest_dist, total_energy_cost = ucs(graph, dist, cost, src, dest, max_energy_cost)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")

    # print the total energy cost
    print(f"Total energy cost: {total_energy_cost}.")
