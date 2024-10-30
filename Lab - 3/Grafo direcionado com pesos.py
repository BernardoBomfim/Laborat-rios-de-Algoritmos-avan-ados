n = 5
matriz_adj_dir_pesos = [[0 for _ in range(n)] for _ in range(n)]

arestas_dir_com_pesos = [(0, 1, 5), (0, 2, 3), (1, 3, 2), (2, 3, 4), (3, 4, 1)]

for u, v, peso in arestas_dir_com_pesos:
    matriz_adj_dir_pesos[u][v] = peso

print("Grafo direcionado com pesos:")
for linha in matriz_adj_dir_pesos:
    print(linha)
