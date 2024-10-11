from arvoreBinaria import ArvoreBinariaBusca

def main():
    arvore = ArvoreBinariaBusca()

    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arvore.inserir(valor)

    print("Percurso em ordem (ordem traversal):")
    arvore.percurso_em_ordem()

if __name__ == "__main__":
    main()
