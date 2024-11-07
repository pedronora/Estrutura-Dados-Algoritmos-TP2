import random


def total_ímpares(lista_índices):
    total = 0
    for indice in lista_índices:
        if indice % 2 != 0:
            total += 1

    return total


if __name__ == '__main__':
    indices_livros = []
    for _ in range(15):
        indices_livros.append(random.randint(10000, 99999))

    print('Referências: ', indices_livros)
    print('Total de referências ímpares: ', total_ímpares(indices_livros))
