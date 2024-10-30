class Tarefa:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

def escalonamento_guloso(tarefas):
    tarefas.sort(key=lambda x: x.fim)
    tarefas_selecionadas = []
    fim_atual = 0

    for tarefa in tarefas:
        if tarefa.inicio >= fim_atual:
            tarefas_selecionadas.append(tarefa)
            fim_atual = tarefa.fim

    return tarefas_selecionadas

tarefas = [
    Tarefa(1, 4),  #Tarefa 1 das 1h as 4h
    Tarefa(3, 5),  #Tarefa 2 das 3h as 5h
    Tarefa(0, 6),  #Tarefa 3 das 0h as 6h
    Tarefa(5, 7),  #Tarefa 4 das 5h as 7h
    Tarefa(3, 8),  #Tarefa 5 das 3h as 8h
    Tarefa(5, 9),  #Tarefa 6 das 5h as 9h
    Tarefa(6, 10), #Tarefa 7 das 6h as 10h
    Tarefa(8, 11), #Tarefa 8 das 8h as 11h
]

tarefas_selecionadas = escalonamento_guloso(tarefas)

print("Tarefas selecionadas para o escalonamento:")
for i, tarefa in enumerate(tarefas_selecionadas):
    print(f"Tarefa {i + 1}: Início = {tarefa.inicio}, Fim = {tarefa.fim}")
