import collections
import json

def bfs(graph, src, dst):

    visited, queue = set(), collections.deque([src])
    visited.add(src)

    while queue:
        # Dequeue a vertex from queue
        path = queue.popleft()

        vertex = path[-1]

        if(vertex == dst):
            print("Shortest path: ", end="")
            print(*path, sep=" -> ", end=".\n")
            break

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                newPath = list(path)
                newPath.append(neighbour)
                queue.append(newPath)
                visited.add(neighbour)

if __name__ == '__main__':
    f = open("G.json")
    graph = json.load(f)

    bfs(graph, '1', '50')