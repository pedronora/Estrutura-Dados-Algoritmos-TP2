import random

# Pilha implementada em aula
class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        # Verifica se a pilha está vazia
        return len(self.itens) == 0

    def push(self, item):
        # Adiciona um item no topo da pilha
        self.itens.append(item)

    def pop(self):
        # Remove e retorna o item do topo da pilha
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        # Retorna o item do topo sem removê-lo
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        # Retorna o número de elementos na pilha
        return len(self.itens)

    def display(self):
        # Exibe o conteúdo da pilha
        print("Pilha:", self.itens)


def ordenar_pilha(pilha):
    pilha_auxiliar = Pilha()

    while not pilha.is_empty():
        item_atual = pilha.pop()

        while not pilha_auxiliar.is_empty() and pilha_auxiliar.peek() < item_atual:
            pilha.push(pilha_auxiliar.pop())

        pilha_auxiliar.push(item_atual)

    while not pilha_auxiliar.is_empty():
        pilha.push(pilha_auxiliar.pop())



if __name__ == '__main__':
    pilha = Pilha()
    
    for _ in range(20):
        pilha.push(random.randint(0, 10))

    pilha.display()

    ordenar_pilha(pilha)
    pilha.display()


