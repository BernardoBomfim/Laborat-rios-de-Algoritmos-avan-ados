N = 8

movimentos_x = [2, 1, -1, -2, -2, -1, 1, 2]
movimentos_y = [1, 2, 2, 1, -1, -2, -2, -1]

def eh_valido(x, y, tabuleiro):
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1

def resolver_cavalo(tabuleiro, pos_x, pos_y, movimento_num):
    if movimento_num == N * N:
        return True

    for i in range(8):
        novo_x = pos_x + movimentos_x[i]
        novo_y = pos_y + movimentos_y[i]

        if eh_valido(novo_x, novo_y, tabuleiro):
            tabuleiro[novo_x][novo_y] = movimento_num
            if resolver_cavalo(tabuleiro, novo_x, novo_y, movimento_num + 1):
                return True
            tabuleiro[novo_x][novo_y] = -1

    return False

def problema_cavalo():
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]

    tabuleiro[0][0] = 0

    if not resolver_cavalo(tabuleiro, 0, 0, 1):
        print("Solução não encontrada")
    else:
        imprimir_tabuleiro(tabuleiro)

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            print(f"{valor:2}", end=' ')
        print()

if __name__ == "__main__":
    problema_cavalo()