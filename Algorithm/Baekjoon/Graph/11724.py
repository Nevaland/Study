import sys
sys.setrecursionlimit(10**6)
 
graph = dict()
N, M = map(int, sys.stdin.readline().split())

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph.update({u : []})
    if v not in graph:
        graph.update({v : []})
    graph[u].append(v)
    graph[v].append(u)

checked = {key: False for key in graph}

cc = 0
if len(graph) < N:
    cc += N-len(graph)

def dfs(node):
    for near_node in graph[node]:
        if not checked[near_node]:
            checked[near_node] = True
            dfs(near_node)
        
while False in checked.values():
    for node in graph:
        if not checked[node]:
            checked[node] = True
            cc += 1
            dfs(node)
        
print(cc)
