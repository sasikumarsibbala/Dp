graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def largest_component(gra):
    visited = set()
    longest = 0
    for nod in gra:
        size = explore(gra, nod, visited)
        if longest < size:
            longest = size

    return longest


def explore(gra, nod, visited):
    if nod in visited:
        return 0
    visited.add(nod)
    size = 1
    for neg in graph[nod]:
        size += explore(gra, neg, visited)
    return size


print(largest_component(graph))
