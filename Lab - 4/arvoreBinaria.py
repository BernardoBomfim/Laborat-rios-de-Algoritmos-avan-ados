class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir(no_atual.direita, valor)

    def percurso_em_ordem(self):
        self._percurso_em_ordem(self.raiz)

    def _percurso_em_ordem(self, no_atual):
        if no_atual is not None:
            self._percurso_em_ordem(no_atual.esquerda)
            print(no_atual.valor, end=' ')
            self._percurso_em_ordem(no_atual.direita)
