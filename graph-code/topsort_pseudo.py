n # number of nodes garaph
g # adjacency list repersent of graph
visited = [False] * n # size n
def fuc_topsort():
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

def dfs(at, visitedNodes):
    visited[at] = True
    neighbours = g[at]
    for to in neighbours:
        if not visited[to]:
            dfs(to, visitedNodes)
    visitedNodes.append(at)
