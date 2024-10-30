n = 5
matriz_adj_dir = [[0 for _ in range(n)] for _ in range(n)]

arestas_direcionadas = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

for u, v in arestas_direcionadas:
    matriz_adj_dir[u][v] = 1

print("Grafo direcionado sem pesos:")
for linha in matriz_adj_dir:
    print(linha)
