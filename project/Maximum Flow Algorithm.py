class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u][v] = w

    # Breadth-First Search (BFS) to find augmenting paths
    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v in range(self.V):
                if not visited[v] and self.adj[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    # Ford-Fulkerson algorithm to find maximum flow
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.adj[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.adj[u][v] -= path_flow
                self.adj[v][u] += path_flow
                v = parent[v]

        return max_flow


# Example usage
if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 15)
    graph.add_edge(1, 3, 10)
    graph.add_edge(2, 3, 10)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 10)
    graph.add_edge(3, 5, 15)
    graph.add_edge(4, 5, 10)

    source, sink = 0, 3
    max_flow = graph.ford_fulkerson(source, sink)
    print("Maximum Flow:", max_flow)
