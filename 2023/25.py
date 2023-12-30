#!/usr/bin/python3
import networkx as nx
from math import prod
g = nx.Graph()
lines = open('25.txt').read().strip().split('\n')
for l in lines:
    head,tail = l.split(': ')
    for t in tail.split(' '):
        g.add_edge(head,t)

for edge in nx.minimum_edge_cut(g):
    g.remove_edge(*edge)

segments = nx.connected_components(g)
print(prod([len(x) for x in list(segments)]))
