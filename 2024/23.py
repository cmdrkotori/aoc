#!/usr/bin/python3
from collections import defaultdict
import networkx as nx
from copy import copy
with open('23.txt') as f:
    lines = f.read().strip().split('\n')

G = nx.Graph()
conn = defaultdict(lambda: [])
for l in lines:
    a,b = l.split('-')
    conn[a].append(b)
    conn[b].append(a)
    G.add_edge(a,b)

networks = set()
for k,v in conn.items():
    for u in v:
        for w in conn[u]:
            if k in conn[w]:
                n = tuple(sorted((k,u,w)))
                networks.add(n)

s = 0
for a,b,c in networks:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        s += 1
print(s)

cliques = list(nx.find_cliques(G))
print(','.join(sorted([x for x in cliques if len(x)==max(map(len,cliques))][0])))

