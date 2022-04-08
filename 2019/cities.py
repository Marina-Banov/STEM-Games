class Graph:
    def __init__(self, m):
        self.m = m
        self.adj = [[] for _ in range(self.m)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def remove_edge(self, v, w):
        self.adj[v].remove(w)
        self.adj[w].remove(v)

    def connected_components(self):
        visited = [False] * self.m
        count = 0

        for v in range(self.m):
            if not visited[v]:
                self.dfs(v, visited)
                count += 1

        return count

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.dfs(i, visited)


def main(m, routes, destroyed):
    g = Graph(m)
    for r1, r2 in routes:
        g.add_edge(r1, r2)
    res = g.connected_components()

    for d in destroyed:
        r1, r2 = routes[d]
        g.remove_edge(r1, r2)
        res += g.connected_components()

    return round(res / (len(destroyed)+1), 2)


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    routes = []
    destroyed = []
    for i in range(n):
        routes.append(tuple(map(int, input().split())))
    for i in range(k):
        destroyed.append(int(input()))
    print(main(m, routes, destroyed))
