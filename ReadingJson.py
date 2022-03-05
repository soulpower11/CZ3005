# # Adjascency List representation in Python

import json 

def uniform_cost_search(start, goal):

    f = open("G.json")
    f1 = open("Dis.json")

    graph = json.load(f)
    dist = json.load(f1)

    start = str(start)
    goal = str(goal)
    parent = {}
    final_cost = 0
    visited = []

    pq = []
    pq_node = [0, start, "-1"]

    pq.append(pq_node)
    while (len(pq) > 0):
        pq.sort()
        current_pq_node = pq.pop(0)
        cost_to_this_node = current_pq_node[0]
        node_index = current_pq_node[1]
        parent_node_index = current_pq_node[2]

        if (node_index == goal):
            final_cost = cost_to_this_node
            parent[node_index] = parent_node_index
            get_path(parent, start, goal)
            print("\ncost to travel =", final_cost)
            return
        elif (node_index not in visited):
            visited.append(node_index)
            parent[node_index] = parent_node_index

            for child in graph[node_index]:

                string_param = node_index+','+child
                cost_to_child = dist[string_param] + cost_to_this_node

                pq_node = [cost_to_child, child, node_index]
                pq.append(pq_node)

def get_path(parent, start, goal):
        temp = goal
        print("T <-", end=" ")
        print(goal, "<-", end="")
        while parent[temp] != start:
            print(parent[temp], "<-", end="")
            temp = parent[temp]
        print(start, end="")
        print(" <- S", end=" ")
