## What are bridges & articulation points? ([660]())
>- A **bridge / cut edge** is any edge in a graph whose removal increases the number of connected components.
>- An **articulation point / cut vertex** is any node in a graph whose removal increases the number of connected components.
>- Bridges and articulation points are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph. Therefore, it’s important to be able to quickly find/detect when and where these occur
>- Both problems are related so we will develop an algorithm to find bridges and then modify it slightly to find articulation points.

## Bridges algorithm
> Start at any node and do a Depth First Search (DFS) traversal labeling nodes with an increasing id value as you go. Keep track the id of each node and the smallest lowlink value. During the DFS, bridges will be found where the id of the node your edge is coming from is less than the low link value of the node your edge is going to.
>
>**NOTE:** The low-link value of a node is
defined as the smallest [lowest] id
reachable from that node when doing a DFS
(including itself)