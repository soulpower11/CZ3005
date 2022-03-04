import json

def uniform_cost_search(graph, dist, src, dest):

    # create a priority queue
    queue = []

    # create a path that starts with the starting node
    path = [src]
    
    # insert the starting index
    queue.append([0, path])

    # dictionary to keep track of visited node
    visited = {}

    # while the queue is not empty
    while queue:

        # sort the queue so that the element with the highest priority is the last element
        queue = sorted(queue)
        p = queue[-1]

        # pop the element with the highest priority
        del queue[-1]

        # get the original value
        p[0] *= -1

        # get the path
        path = p[1]

        # set the current node to the last node in the path
        cur_node = path[-1]

        # check if current node is the destination node
        if cur_node == dest:
            # return the path and the total distance from source to destination node
            return path, p[0]

        # check for the non visited nodes
        if cur_node not in visited:
            for i in range(len(graph[str(cur_node)])):

                # clone current path to a new path to 
                # prevent appending to the current path
                newPath = path[:]
                # append the adjacent node to the new path
                newPath.append(graph[str(cur_node)][i])

                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append(
                    [(p[0] + dist[f"{cur_node},{graph[str(cur_node)][i]}"]) * -1, newPath])

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
    path, shortest_dist,  = uniform_cost_search(graph, dist, src, dest)
    print("Shortest path: ", end="")
    print(*path, sep=" -> ", end=".\n")

    # print the shortest distance
    print(f"Shortest Distance: {shortest_dist}.")