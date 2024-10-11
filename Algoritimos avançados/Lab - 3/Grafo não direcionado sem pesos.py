n = 5
matriz_adj = [[0 for _ in range(n)] for _ in range(n)]  

arestas = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4)] 

for u, v in arestas:
    matriz_adj[u][v] = 1
    matriz_adj[v][u] = 1

print("Grafo não direcionado sem pesos:")
for linha in matriz_adj:
    print(linha)
