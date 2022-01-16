# breath first use Queue
from queue import Queue


def breath_first(graph, source):
    q = Queue()
    q.put(source)
    while q.qsize() > 0:
        current = q.get()
        print(current)
        for neg in graph[current]:
            q.put(neg)


a = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
breath_first(a, 'a')
