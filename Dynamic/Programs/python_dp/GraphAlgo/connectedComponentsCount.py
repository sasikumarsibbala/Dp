from collections import defaultdict


def connectd_component_count(graph):
    visited = set()
    count = 0
    for nod in graph:
        if explore(graph, nod, visited):
            count += 1
    return count


def explore(graph, current, visited):
    if str(current) in visited: return False
    visited.add(str(current))
    for neg in graph[current]:
        explore(graph, neg, visited)
    return True


ed = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def buldGraph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


# print(connectd_component_count(buldGraph(ed)))
print(connectd_component_count(graph1))
