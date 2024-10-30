class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v, capacidade):
        self.grafo[u][v] = capacidade

    def dfs(self, grafo_residual, origem, destino, caminho):
        visitados = [False] * self.vertices
        fila = [origem]
        caminho[origem] = -1

        while fila:
            u = fila.pop()

            for v, capacidade in enumerate(grafo_residual[u]):
                if not visitados[v] and capacidade > 0:
                    fila.append(v)
                    caminho[v] = u
                    visitados[v] = True
                    if v == destino:
                        return True

        return False

    def ford_fulkerson(self, fonte, destino):
        grafo_residual = [linha[:] for linha in self.grafo]
        caminho = [-1] * self.vertices 
        fluxo_maximo = 0

        while self.dfs(grafo_residual, fonte, destino, caminho):
            fluxo_caminho = float('Inf')
            v = destino
            while v != fonte:
                u = caminho[v]
                fluxo_caminho = min(fluxo_caminho, grafo_residual[u][v])
                v = u
            v = destino

            while v != fonte:
                u = caminho[v]
                grafo_residual[u][v] -= fluxo_caminho
                grafo_residual[v][u] += fluxo_caminho
                v = u

            fluxo_maximo += fluxo_caminho

        return fluxo_maximo

    def exibir_grafo(self):
        print("Representação do Grafo (Capacidades):")
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] > 0:
                    print(f"{i} -> {j} (Capacidade: {self.grafo[i][j]})")


def main():
    vertices = 6
    grafo = Grafo(vertices)
    grafo.adicionar_aresta(0, 1, 16)
    grafo.adicionar_aresta(0, 2, 13)
    grafo.adicionar_aresta(1, 2, 10)
    grafo.adicionar_aresta(1, 3, 12)
    grafo.adicionar_aresta(2, 1, 4)
    grafo.adicionar_aresta(2, 4, 14)
    grafo.adicionar_aresta(3, 2, 9)
    grafo.adicionar_aresta(3, 5, 20)
    grafo.adicionar_aresta(4, 3, 7)
    grafo.adicionar_aresta(4, 5, 4)

    grafo.exibir_grafo()

    fonte = 0
    destino = 5
    fluxo_maximo = grafo.ford_fulkerson(fonte, destino)

    print(f"\nFluxo máximo entre {fonte} e {destino}: {fluxo_maximo}")


if __name__ == "__main__":
    main()
