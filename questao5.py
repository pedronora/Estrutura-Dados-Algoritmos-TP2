class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)


def tarefa_no_topo(pilha_de_tarefas):
    size = len(pilha_de_tarefas.itens)
    topo = pilha_de_tarefas.itens[size - 1]
    return 'Tarefa do topo: ' + topo


if __name__ == '__main__':
    tarefas = ['correr', 'enviar email',
               'fazer compras', 'telefonar', 'reunião']

    pilha_de_tarefas = Pilha()

    for tarefa in tarefas:
        pilha_de_tarefas.push(tarefa)
        
    print('Pilha de tarefas: ', pilha_de_tarefas.itens )
    print(tarefa_no_topo(pilha_de_tarefas))
