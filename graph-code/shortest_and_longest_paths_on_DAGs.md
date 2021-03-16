># Directed Acyclic Graph (DAG)
>Recall that a Directed Acyclic Graph (DAG) is agraph with directed edges and no cycles.  
__NOTE:__ By definition this means all trees are automatically DAGs since they do not contain cycles.

># Shortest Path on DAG (SSSP on DAG)
>* The Single Source Shortest Path (SSSP) problem can be solved efficiently on a DAG in **O(V+E)** time.  
>* This is due to the fact that the nodes
can be ordered in a **[topological ordering](topological_sort.md)** via
[topological sort](topological_sort.md) and processed sequentially.
([406]())

># Longest path on DAG
>* What about the longest path? On a general graph this problem is **NP-Hard**, but on a DAG this problem is solvable in **O(V+E)!**   
>* **The trick is to multiply all edge values by -1** then find the shortest path and then multiply the edge values by -1 again!