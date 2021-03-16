class FindComponents:
    n #number of nodes in the graph
    g = [] # adjacency list representing graph
    count = 0
    components # empty integer array size n
    visited = [False]*n # size n
    def find_components():
        for i in Range(0, n):
            if !visited[i]:
                count += 1
                dfs(i)
        return (count, components)

    def dfs(at):
        visited[at] = True
        neighbours = g[at]
        components[at] = count;
        for to in neighbours:
            if !visited[at]:
                dfs(to)

