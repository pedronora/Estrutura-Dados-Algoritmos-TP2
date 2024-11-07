import random


class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)


def impares(pilha):
    total_impares = 0
    for pedido in pilha.itens:
        if pedido % 2 != 0:
            total_impares += 1

    return total_impares


if __name__ == '__main__':
    lista_pedidos = [random.randint(1000, 9999) for _ in range(15)]

    pilha_pedidos = Pilha()
    for pedido in lista_pedidos:
        pilha_pedidos.push(pedido)

    print('Pilha de pedidos: ', pilha_pedidos.itens)
    print('Total de ímpares: ', impares(pilha_pedidos))
