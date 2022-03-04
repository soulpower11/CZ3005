# BFS algorithm in Python


import collections
import json

# BFS algorithm
def bfs(graph, src, dst):

    visited, queue = set(), collections.deque([src])
    visited.add(src)

    # Path vector to store the current path
    path = []
    path.append(src)

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        
        path.append(vertex)

        if vertex in path:
            path = path[:path.index(vertex)+1]
            
        #print(str(vertex) + " ", end="")

        # last = visited[len(visited) - 1]

        if(int(vertex) == dst):
            print(queue)
            print(visited)
            print(path)
            break


        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[str(vertex)]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    f = open("G.json")
    graph = json.load(f)
    # graph = {"0": [1, 2], "1": [2], "2": [3], "3": [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 1, 2)
    # bfs(graph, 0, 3)