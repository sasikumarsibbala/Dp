# given graph and source and destination , we need to find wheter we
# create path
from queue import Queue


def has_path_depth_first(graph, src, des):
    if src == des:
        return True
    for neg in graph[src]:
        if has_path_depth_first(graph, neg, des):
            return True
    return False


def has_path_breath_first(graph, src, des):
    q = Queue()
    q.put(src)
    while q.qsize() > 0:
        current = q.get()
        if current == des: return True
        for ned in graph[current]:
            q.put(ned)


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}
print(has_path_depth_first(graph, 'f', 'k'))
print(has_path_breath_first(graph, 'f', 'k'))
