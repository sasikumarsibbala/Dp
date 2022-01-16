from collections import defaultdict
from queue import Queue

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


def get_graph(edg):
    graph1 = defaultdict(list)
    for edge in edg:
        a, b = edge[0], edge[1]
        graph1[a].append(b)
        graph1[b].append(a)
    return graph1


graph1 = get_graph(edges)


def shortest_path(graph, node1, node2):
    visited = set()
    visited.add(node1)
    q = Queue()
    q.put([node1, 0])
    while q.qsize() > 0:
        nod, dis = q.get()[0], q.get()[1]
        if nod == node2: return dis
        for neg in graph[nod]:
            if neg in visited == False:
                visited.add(neg)
                q.get(neg, dis + 1)
    return -1


print(shortest_path(graph1, 'w', 'z'))
# print(get_graph(edges))
