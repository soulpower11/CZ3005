 # Adjascency List representation in Python

import json

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        with open('graph.txt', 'w') as fout:
            for i in range(self.V):
                fout.write("Vertex " + str(i) + ":")
                temp = self.graph[i]
                while temp:
                    fout.write(" -> {} ".format(temp.vertex))
                    temp = temp.next
                fout.write(" \n")


if __name__ == "__main__":
    f = open("G.json")
    data = json.load(f)
    V = len(data)+1
    print("V: ", V)

    # Create graph and edges
    graph = Graph(V)

    for i in data:
        for d in data[i]:
            graph.add_edge(int(i) , int(d))

    graph.print_agraph()

    f.close()
