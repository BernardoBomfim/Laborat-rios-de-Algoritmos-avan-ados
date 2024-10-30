class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = {i: [] for i in range(vertices)}

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def dfs(self, inicio):
        visitados = [False] * self.vertices
        resultado = []
        self._dfs_util(inicio, visitados, resultado)
        return resultado

    def _dfs_util(self, v, visitados, resultado):
        visitados[v] = True
        resultado.append(v)

        for vizinho in self.grafo[v]:
            if not visitados[vizinho]:
                self._dfs_util(vizinho, visitados, resultado)

    def bfs(self, inicio):
        visitados = [False] * self.vertices
        fila = [inicio]
        visitados[inicio] = True
        resultado = []

        while fila:
            v = fila.pop(0)
            resultado.append(v)

            for vizinho in self.grafo[v]:
                if not visitados[vizinho]:
                    fila.append(vizinho)
                    visitados[vizinho] = True

        return resultado

    def exibir_grafo(self):
        print("Representação do Grafo:")
        for vertice in self.grafo:
            print(f"{vertice} -> {', '.join(map(str, self.grafo[vertice]))}")

def main():
    n = 6
    grafo = Grafo(n)

    arestas = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
    for u, v in arestas:
        grafo.adicionar_aresta(u, v)

    grafo.exibir_grafo()

    print("\nBusca em Profundidade (DFS) a partir do vértice 0:")
    dfs_resultado = grafo.dfs(0)
    print(" -> ".join(map(str, dfs_resultado)))

    print("\nBusca em Largura (BFS) a partir do vértice 0:")
    bfs_resultado = grafo.bfs(0)
    print(" -> ".join(map(str, bfs_resultado)))

if __name__ == "__main__":
    main()
