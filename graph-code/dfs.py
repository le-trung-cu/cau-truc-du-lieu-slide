class DFS():
    n #number of nodes in the graph
    g #adjacency list representing graph
    visited =[False] * n #size n

    def fun_dfs(self, at):
        if visited[at]: 
            return
        visited[at] = True
        neighbours = g[at]
        for to in neighbours:
            fun_dfs(to)

