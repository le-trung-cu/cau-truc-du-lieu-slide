# Bellman-Ford Algorithm ([page 545]())
## BF algorithm overview
  - In graph theory, the **Bellman-Ford (BF)** algorithm is a **Single Source Shortest Path(SSSP)** algorithm. This means it can find the shortest path from one node to any other node.

  - However, BF is not ideal for most SSSP problems because it has a time complexity of **O(EV)**. It is better to use Dijkstra’s algorithm which is much faster. It is on the order of **Θ((E+V)log(V))** when using a binary heap priority queue.

  - However, Dijkstra’s algorithm can fail when the graph has negative edge weights. This is when BF becomes really handy because it can be used to detect **negative cycles** and **determine where they occur**.

  - Finding negative cycles can be useful in many types of applications. One particularly neat application arises in finance when performing an **arbitrage** between two or more markets.

>## BF Algorithm Steps ([page 559]())
>  - E be the number of edges.
>  - Let V be the number of vertices.
>  - Let S be the id of the starting node.
>  - Let D be an array of size V that tracks the best distance from S to each node.
> ---
>1. Set every entry in D to +∞
>2. Set D[S] = 0
>3. Relax each edge V-1 times:

```python
for i in range(V - 1):
  for edge in graph.edges:
  # Relax edge (update D with shorter path)
  if (D[edge.from] + edge.cost < D[edge.to])
  D[edge.to] = D[edge.from] + edge.cost
  #Repeat to find nodes caught in a negative cycle
  for i in range(V - 1):
    for edge in graph.edges:
      if (D[edge.from] + edge.cost < D[edge.to])
        D[edge.to] = -
```