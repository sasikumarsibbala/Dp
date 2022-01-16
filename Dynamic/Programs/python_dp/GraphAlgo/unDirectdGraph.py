from collections import defaultdict


def has_path(graph, src, des, visited=set()):
    if src in visited: return False
    if src == des: return True
    visited.add(src)
    for neg in graph[src]:
        if has_path(graph, neg, des):
            return True
    return False


def buldGraph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


ed = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
print(has_path(buldGraph(ed), 'j', 'm'))
