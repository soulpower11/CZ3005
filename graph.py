#! /usr/bin/env python3

import json


# def get_edges(graph):
#     for d in json.loads(graph):
#         #node = d['data']
#         #yield node['source'], node['target']
#         print(d)


# def plot(graph, outfile='graph.txt'):
#     with open(outfile, 'w') as fout:
#         for src, dst in get_edges(graph):
#             fout.write('%s  %s\n' % (src, dst))


if __name__ == '__main__':
    f = open("G(1).json")
    data = json.load(f)
    for i in data:
         print(data[i])

    #plot(f)
    f.close()