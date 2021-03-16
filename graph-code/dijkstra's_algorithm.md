># What is Dijkstra’s algorithm?
>* Dijkstra’s algorithm is a **Single Source Shortest Path (SSSP)** 
>algorithm for graphs with **non-negative** edge weights.  
>*  Depending on how the algorithm is implemented and what data structures are 
>used the time complexity is typically **O(E*log(V))** which is competitive 
>against other shortest path algorithms.

**Algorithm prerequisites:**  
  * One constraint for Dijkstra’s algorithm is
    that the graph **must only contain non-negative
    edge weights**. This constraint is imposed to
    ensure that once a node has been visited its
    optimal distance cannot be improved.

        This is property is especially important because it enables Dijkstra’s algorithm to act in a greedy manner by always selecting the next most promising node.

**Outline:**
The goal of this slide deck is for you to understand how to implement 
Dijkstra’s algorithm and implement it efficiently.
* Lazy Dijkstra’s pseudo-code   
* Finding SP + stopping early optimization
* Using indexed priority queue + decreaseKey to reduce space and increase 
* performance.
* Eager Dijkstra’s animation
* Eager Dijkstra’s pseudo-code
* Heap optimization with D-ary heap

># Quick Algorithm Overview ([page 443]())
>2. Maintain a PQ of key-value pairs of (node index, distance) pairs which tell 
you which node to visit next based on sorted min value.
>3. Insert (s, 0) into the PQ and loop while PQ is not empty pulling out the 
next most promising (node index, distance) pair.
>4. Iterate over all edges outwards from the current node and relax each edge 
appending a new (node index, distance) key-value pair to the PQ for every 
relaxation.

---

## Optimal distance to a particular node 
  ```python
  # Runs Dijkstra’s algorithm and returns an array that contains
  # the shortest distance to every node from the start node s.
  # g - adjacency list of weighted graph
  # n - the number of nodes in the graph
  # s - the index of the starting node (0 ≤ s < n)
  def dijkstra(g, n, s):
    visited = [false, false, … , false] # size n
    dist = [∞, ∞, … ∞, ∞] # size n
    dist[s] = 0
    pq = empty priority queue
    pq.insert((s, 0))
    while pq.size() != 0:
      index, minValue = pq.poll()
      visited[index] = true
      for (edge : g[index]):
        if visited[edge.to]: continue
        newDist = dist[index] + edge.cost
        if newDist < dist[edge.to]:
          dist[edge.to] = newDist
          pq.insert((edge.to, newDist))
    return dist
  ```
    In practice most standard libraries do not support the decrease key operation for PQs. A way to get around this is to add a ne (node index, best distance) pair every time we update the distance to a node.

    As a result, it is possible to have duplicate node indices in the PQ. This is not ideal, but inserting a new key-value pair in O(log(n)) is much faster than searching for the key in the PQ which takes O(n)

    A neat optimization we can do which ignores stale (index, dist) pairs in our PQ is to skip nodes where we already found a better path routing through others nodes before we got to processing this node.

---

## Finding the optimal path
    If you wish to not only find the optimal distance to a particular node butalso what sequence of nodes were taken to get there you need to track some additional information.

```python

# Finds the shortest path between two nodes.
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 ≤ s < n)
# e - the index of the end node (0 ≤ e < n)
def findShortestPath(g, n, s, e):
  dist, prev = dijkstra(g, n, s)
  path = []
  if (dist[e] == ∞): return path
  at = e
  while at:
    at = prev[at]
    path.add(at)
    path.reverse()
  return path

# Runs Dijkstra’s algorithm and returns an array that contains
# the shortest distance to every node from the start node s and
# the prev array to reconstruct the shortest path itself
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 ≤ s < n)
def dijkstra(g, n, s):
  vis = [False]*n # size n
  prev = [None]*n# size n
  dist = [∞]*n # size n
  dist[s] = 0
  pq # empty priority queue
  pq.insert((s, 0))
  while pq.size() != 0:
    index, minValue = pq.poll()
    vis[index] = true
    if dist[index] < minValue: continue
    for edge in g[index]:
      if vis[edge.to]: continue
      newDist = dist[index] + edge.cost
      if newDist < dist[edge.to]:
        prev[edge.to] = index
        dist[edge.to] = newDist
        pq.insert((edge.to, newDist))
  return (dist, prev)
```

---

## Stopping Early
    Q: Suppose you know the destination node you’re trying to reach is ‘e’ and you start at node ’s’ do you still have to visit every node in the graph?  
    A: Yes, in the worst case. However, it is possible to stop early once you have finished visiting the destination node.

>The main idea for stopping early is that Dijkstra’s algorithm processes each next most promising node in order. So if the destination node has been visited, its shortest distance will not change as more future nodes are visited.

```python
# Runs Dijkstra’s algorithm and returns an array that contains
# the shortest distance to every node from the start node s and
# the prev array to reconstruct the shortest path itself
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 ≤ s < n)
def dijkstra(g, n, s, e):
  vis = [False]*n # size n
  prev = [None]*n# size n
  dist = [∞]*n # size n
  dist[s] = 0
  pq # empty priority queue
  pq.insert((s, 0))
  while pq.size() != 0:
    index, minValue = pq.poll()
    vis[index] = true
    if dist[index] < minValue: continue
    for edge in g[index]:
      if vis[edge.to]: continue
      newDist = dist[index] + edge.cost
      if newDist < dist[edge.to]:
        prev[edge.to] = index
        dist[edge.to] = newDist
        pq.insert((edge.to, newDist))
    if index == e:
      return dist[e] 
  return (dist, prev)
```

---

## Eager Dijkstra’s using an Indexed Priority Queue
> Our current lazy implementation of Dijkstra’s inserts **duplicate key-value pairs** (keys being the node index and the value being the shortest distance to get to that node) in our PQ because it’s more efficient to insert a new key-value pair in **O(log(n))** than it is to update an existing key’s value in **O(n)**.  
   
    This approach is inefficient for dense graphs because we end up with several stale outdated key-value pairs in our PQ. The eager version of Dijkstra’s avoids duplicate key-value pairs and supports efficient value updates in O(log(n)) by using an Indexed Priority Queue (IPQ)

```python
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
```