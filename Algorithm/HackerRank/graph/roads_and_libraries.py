def roadsAndLibraries(n, c_lib, c_road, cities):
  if c_lib < c_road:
    return c_lib * n

  cost = 0
  graph = {}
  for load in cities:
    u, v = load
    if u not in graph:
      graph.update({u : []})
    if v not in graph:
      graph.update({v : []})
    graph[u].append(v)
    graph[v].append(u)
  visited = {key: False for key in graph}

  cost = 0
  if len(graph) < n:
    cost += (n-len(graph)) * c_lib

  for node in graph:
    if not visited[node]:
      visited[node] = True
      cost += c_lib
      cost += getCostAndBuildRoad(node, graph, visited, c_road)

  return cost

def getCostAndBuildRoad(node, graph, visited, c_road):
  cost = 0
  for near_node in graph[node]:
    if not visited[near_node]:
      visited[near_node] = True
      cost += c_road
      cost += getCostAndBuildRoad(near_node, graph, visited, c_road)
  return cost

print(roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]))
print(roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]))
print(roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]))
