## What else can DFS do?
  We can augment the DFS algorithm to:

    • Compute a graph’s minimum spanning tree.  
    • Detect and find cycles in a graph.  
    • Check if a graph is bipartite.  
    • Find strongly connected components.  
    • Topologically sort the nodes of a graph.  
    • Find bridges and articulation points.  
    • Find augmenting paths in a flow network.  
    • Generate mazes.
___

# Topological Sort 
  > A topological ordering is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B in the ordering.
  
  
  
  __NOTE:__  

    1. Topological orderings are NOT unique.
    2. Not every graph can have a topological ordering. A graph which contains a cycle cannot have a valid ordering:
    3. The topological sort algorithm can find a topological ordering in O(V+E) time!



## Directed Acyclic Graphs(DAG) 
  >The only type of graph which has a valid topological ordering is a Directed AcyclicGraph (DAG). These are graphs with directed edges and no cycles.

    Q: How do I verify that my graph does not contain a directed cycle?  
    A: One method is to use Tarjan’s strongly connected component algorithm which can be used to find these cycles.

## Topological Sort Algorithm
    1. Pick an unvisited node
    2. Beginning with the selected node, do a Depth First Search (DFS) exploring only unvisited nodes.
    3. On the recursive callback of the DFS, add the current node to the topological ordering in reverse order. 




Topological sort **pseudo code** 
```python
"""Topological sort pseudo code"""
n # number of nodes graph
g # adjacency list represent of graph
visited = [False] * n # size n
def fuc_topologicalSort():
    ordering = [0] * n # size n
    i = n - 1 # index for ordering in array
    for at = 0 in range(0, n):
        if not visited[at]:
            visitedNodes = []
            dfs(at, visitedNodes)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i = i - 1
    return ordering

# Execute Depth First Search (DFS) 
def dfs(at, visitedNodes):
    visited[at] = True
    neighbors = g[at]
    for to in neighbors:
        if not visited[to]:
            dfs(to, visitedNodes)
    visitedNodes.append(at)
```

Topological sort **Optimization**
```python
"""Topological sort Optimization"""
n # number of nodes graph
g # adjacency list represent of graph
visited = [False] * n # size n
def fuc_topologicalSort():
    ordering = [0] * n # size n
    i = n - 1 # index for ordering in array
    for at = 0 in range(0, n):
        if not visited[at]:
            visitedNodes = []
            dfs(i, at, ordering, visitedNodes)
            # for nodeId in visitedNodes:
            #     ordering[i] = nodeId
            #     i = i - 1
    return ordering

# Execute Depth First Search (DFS) 
def dfs(i, at, ordering, visitedNodes):
    visited[at] = True
    neighbors = g[at]
    for to in neighbors:
        if not visited[to]:
            i = dfs(i, to, ordering, visitedNodes)
    ordering[i] = at
    return i - 1
```