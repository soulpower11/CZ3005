import json

def ucs(graph, dist, src, dest):

    # create a priority queue
    queue = []

    # push the starting index and path
    queue.append([0, [src]])

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

        # get the current path
        cur_path = e[1]

        # set the current node to the last node in the path
        cur_node = cur_path[-1]

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return cur_path, cur_dist

        # check for the non visited nodes
        if cur_node not in visited:
            for neighbour in graph[cur_node]:
            
                # clone current path to a new path to 
                # prevent appending to the current path
                newPath = cur_path[:]
                # append the adjacent node to the new path
                newPath.append(neighbour)

                # calculate the new distance
                # new distance is multiplied by -1 so that
                # least priority is at the top
                newDist = (cur_dist + dist[f"{cur_node},{neighbour}"]) * -1

                # push adjacent node with it's distance and path into priority queue
                queue.append([newDist, newPath])

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

    # set source node
    src = '1'

    # set destination node
    dest = '50'

    # find shortest distance from source to destination node
    path, shortest_dist = ucs(graph, dist, src, dest)

    # print the shortest path
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")