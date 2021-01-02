import sys
from queue import Queue
sys.setrecursionlimit(10**8)

graph = dict()
N, M, V = map(int, sys.stdin.readline().split())

for _ in range(M):
    x1, x2 = map(int, sys.stdin.readline().split())
    if x1 not in graph:
        graph.update({x1 : []})
    if x2 not in graph:
        graph.update({x2 : []})
    graph[x1].append(x2)
    graph[x2].append(x1)

for key in graph:
    graph[key] = sorted(graph[key])

# DFS
def dfs(node):
    checked[node] = True
    seq.append(node)
    if node in graph:
        for near_node in graph[node]:
            if not checked[near_node]:
                dfs(near_node)

checked = {key: False for key in graph}
seq = list()
dfs(V)
print(' '.join(map(str, seq)))

# BFS
queue = Queue()
checked = {key: False for key in graph}
seq = list()

def check(node):
    queue.put(node)
    checked[node] = True
    seq.append(node)

check(V)
while not queue.empty():
    node = queue.get()
    if node in graph:
        for near_node in graph[node]:
            if not checked[near_node]:
                check(near_node)

print(' '.join(map(str, seq)))
