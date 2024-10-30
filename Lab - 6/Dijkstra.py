import heapq

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = {i: [] for i in range(vertices)}
        self.pesos = {}

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def adicionar_aresta_com_peso(self, u, v, peso):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        self.pesos[(u, v)] = peso
        self.pesos[(v, u)] = peso 

    def bfs(self, inicio, destino):
        visitados = [False] * self.vertices
        distancias = [-1] * self.vertices
        fila = [inicio]
        visitados[inicio] = True
        distancias[inicio] = 0

        while fila:
            atual = fila.pop(0)

            if atual == destino:
                return distancias[atual]

            for vizinho in self.grafo[atual]:
                if not visitados[vizinho]:
                    fila.append(vizinho)
                    visitados[vizinho] = True
                    distancias[vizinho] = distancias[atual] + 1

        return -1

    def dijkstra(self, inicio, destino):
        distancias = {v: float('inf') for v in range(self.vertices)}
        distancias[inicio] = 0
        pq = [(0, inicio)]

        while pq:
            distancia_atual, vertice_atual = heapq.heappop(pq)

            if vertice_atual == destino:
                return distancias[vertice_atual]

            for vizinho in self.grafo[vertice_atual]:
                peso = self.pesos.get((vertice_atual, vizinho), 1)
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(pq, (nova_distancia, vizinho))

        return float('inf')

    def exibir_grafo(self):
        print("Representação do Grafo:")
        for vertice in self.grafo:
            print(f"{vertice} -> {', '.join(map(str, self.grafo[vertice]))}")

def main():
    n = 6
    grafo = Grafo(n)

    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2)
    grafo.adicionar_aresta(1, 3)
    grafo.adicionar_aresta(1, 4)
    grafo.adicionar_aresta(2, 4)
    grafo.adicionar_aresta(3, 5)
    grafo.adicionar_aresta(4, 5)

    print("Grafo sem pesos:")
    grafo.exibir_grafo()

    inicio = 0
    destino = 5
    print(f"\nDistância mínima entre {inicio} e {destino} usando BFS: {grafo.bfs(inicio, destino)}")

    grafo_com_pesos = Grafo(n)
    grafo_com_pesos.adicionar_aresta_com_peso(0, 1, 2)
    grafo_com_pesos.adicionar_aresta_com_peso(0, 2, 4)
    grafo_com_pesos.adicionar_aresta_com_peso(1, 3, 1)
    grafo_com_pesos.adicionar_aresta_com_peso(1, 4, 7)
    grafo_com_pesos.adicionar_aresta_com_peso(2, 4, 3)
    grafo_com_pesos.adicionar_aresta_com_peso(3, 5, 1)
    grafo_com_pesos.adicionar_aresta_com_peso(4, 5, 2)

    print("\nGrafo com pesos:")
    grafo_com_pesos.exibir_grafo()

    print(f"\nDistância mínima entre {inicio} e {destino} usando Dijkstra: {grafo_com_pesos.dijkstra(inicio, destino)}")

if __name__ == "__main__":
    main()