"""class priority_queue:
  def contains(self, node):
    return True
  def insert(self, node):
    return"""

# Runs Dijkstra’s algorithm and returns an array that contains
# the shortest distance to every node from the start node s.
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 ≤ s < n)
def dijkstra(g, n, s):
  vis = [False]*n # size n
  dist = [∞] * n # size n
  dist[s] = 0
  ipq = priority_queue() #empty indexed priority queue
  ipq.insert(s, 0)
  while ipq.size() != 0:
    index, minValue = ipq.poll()
    vis[index] = true
    if dist[index] < minValue: continue
    for edge in g[index]:
      if vis[edge.to]: continue
      newDist = dist[index] + edge.cost
      if newDist < dist[edge.to]:
        dist[edge.to] = newDist
        if not ipq.contains(edge.to):
          ipq.insert(edge.to, newDist)
        else:
          ipq.decreaseKey(edge.to, newDist)
  return dist