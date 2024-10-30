import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent, rank = [], []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, root_u, root_v)
        
        return result

    def prim_mst(self):
        selected = [False] * self.V
        result = []
        edges = [(0, 0, 0)]

        while len(result) < self.V - 1:
            edges = sorted(edges, key=lambda x: x[0])
            cost, u, v = edges.pop(0)
            if not selected[v]:
                selected[v] = True
                result.append((u, v, cost))
                for u_next, v_next, cost_next in self.graph:
                    if v_next == v and not selected[u_next]:
                        edges.append((cost_next, u_next, v_next))
        
        return result

def draw_graph(graph, edges, title):
    G = nx.Graph()
    for u, v, w in graph:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}' for u, v, w in graph})

    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2.5)
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    kruskal_result = g.kruskal_mst()
    print("MST usando Kruskal:", kruskal_result)
    draw_graph(g.graph, kruskal_result, "MST usando Kruskal")

    prim_result = g.prim_mst()
    print("MST usando Prim:", prim_result)
    draw_graph(g.graph, prim_result, "MST usando Prim")