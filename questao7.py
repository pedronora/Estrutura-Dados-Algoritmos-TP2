import random


class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)


def pares(pilha):
    total_pares = 0
    for pedido in pilha.itens:
        if pedido % 2 == 0:
            total_pares += 1

    return total_pares


if __name__ == '__main__':
    lista_pedidos = [random.randint(1000, 9999) for _ in range(15)]

    pilha_pedidos = Pilha()
    for pedido in lista_pedidos:
        pilha_pedidos.push(pedido)

    print('Pilha de pedidos: ', pilha_pedidos.itens)
    print('Total de pares: ', pares(pilha_pedidos))
