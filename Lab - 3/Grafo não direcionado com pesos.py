n = 5
matriz_adj_pesos = [[0 for _ in range(n)] for _ in range(n)]

arestas_com_pesos = [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 4), (3, 4, 1)]

for u, v, peso in arestas_com_pesos:
    matriz_adj_pesos[u][v] = peso
    matriz_adj_pesos[v][u] = peso

print("Grafo não direcionado com pesos:")
for linha in matriz_adj_pesos:
    print(linha)
