import json
import math

def dijkstra(graph, dist, src, dest):

    # create a priority queue
    queue = []

    # push the starting index and path
    queue.append([0, [src]])

    # dictionary to keep track of visited node
    visited = {}

    # dictionary to keep track of the node distance
    # for checking if there's another shortest path
    distance = {src: math.inf}

    # while the queue is not empty
    while queue:

        # sort the queue so that the element with the highest priority is the last element
        queue = sorted(queue)
        e = queue[-1]

        # pop the element with the highest priority
        del queue[-1]

        # get the current distance
        cur_dist = e[0] * -1

        # get the current path
        cur_path = e[1]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        # mark current ndoe as visited
        visited[cur_node] = 1

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return cur_path, cur_dist

        # check for adjacent node
        for neighbour in graph[cur_node]:
            
            # if the distance for this not is not initialized
            if neighbour not in distance:
                # initialized the node distance
                distance[neighbour] = math.inf
            
            # clone current path to a new path to 
            # prevent appending to the current path
            newPath = cur_path[:]
            # append the adjacent node to the new path
            newPath.append(neighbour)

            # calculate the new distance
            newDist = cur_dist + dist[f"{cur_node},{neighbour}"]

            # if adjacent node is not in visted and if the new distance smaller than the old distance
            if neighbour not in visited and distance[neighbour] > newDist:
                # push adjacent node with it's distance and path into priority queue
                # new distance is multiplied by -1 so that
                # least priority is at the top
                queue.append([newDist*-1, newPath])
                # update the distance of the node
                distance[neighbour] = newDist
        
# main function
if __name__ == '__main__':

    # load graph from JSON
    g = open("G.json")
    graph = json.load(g)
    
    # load distance from JSON
    d = open("Dist.json")
    dist = json.load(d)

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # find shortest distance from source to destination node
    path, shortest_dist = dijkstra(graph, dist, src, dest)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")