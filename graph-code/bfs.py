from collections import deque

class bfs:
    n # number of nodes in graph
    g # adjacent list represent of graph

    def func_bfs(__self, s, e):
        # Do a BFS starting at node s
        prev = __self.solve(s)
        
        # Return reconstructed path from s -> e 
        return __self.reconstructPath(s,e, prev)

    def solve(__self, s):
        q = deque()
        q.append(s)
        visited = [False]*n # size n
        visited[at] = True

        prev = [None] * n

        # collections in python are false when them empty
        while q:
            at = q.popleft()
            neighbours = g[at]
            for to in neighbours:
                if !visited[to]:
                    queue.append(to)
                    visited[to] = True
                    prev[to] = at
        return prev

    def reconstructPath(__self, s, e, prev):
        # Reconstruct path going backwards from e
        path = []
        at = e
        while at not None:
            path.append(at)
            at = prev[at]
        
        path.reverse()
        if path[0] == s:
            return path
        return []


