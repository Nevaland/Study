def findShortest(graph_nodes, graph_from, graph_to, ids, val):
  graph = {}
  for start, end in zip(graph_from, graph_to):
    if not start in graph:
      graph.update({start:{'near': [], 'color': ids[start-1]}})
    if not end in graph:
      graph.update({end:{'near': [], 'color': ids[end-1]}})
    graph[start]['near'].append(end)
    graph[end]['near'].append(start)

  total_shortest_distance = -1
  for node in graph:
    if graph[node]['color'] == val:
      shortest_distance = getDisctanceOfNearestNode(graph, node, graph[node]['color'])
      if shortest_distance < total_shortest_distance or total_shortest_distance == -1:
        total_shortest_distance = shortest_distance

  return total_shortest_distance

from queue import Queue
def getDisctanceOfNearestNode(graph, node, color):
  queue = Queue()
  queue.put(node)
  checked = {key: False for key in graph}
  checked[node] = True
  depth = 0
  while not queue.empty():
    node = queue.get()
    depth += 1
    for near_node in graph[node]['near']:
      if not checked[near_node]:
        checked[near_node] = True
        queue.put(near_node)
        if graph[near_node]['color'] == color:
          return depth
  return -1


print(findShortest(5, [1,1,2,3], [2,3,4,5], [1,2,3,3,2], 2))
print(findShortest(5, [1,1,2,3], [2,3,4,5], [1,2,3,3,2], 2))
