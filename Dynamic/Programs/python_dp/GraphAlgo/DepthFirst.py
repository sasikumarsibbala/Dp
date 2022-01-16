# depth first we will use stack
def depth_first(graph, source):
    arr = [source]
    while len(arr) > 0:
        current = arr.pop()
        print(current)
        for neig in graph[current]:
            arr.append(neig)


def dep_first_recur(graph, source):
    print(source)
    for neg in graph[source]:
        dep_first_recur(graph, neg)


a = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
depth_first(a, 'a')
print('@@@@@@@@')
dep_first_recur(a, 'a')
