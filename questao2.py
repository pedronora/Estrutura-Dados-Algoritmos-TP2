import numpy as np
import timeit

def mergesort(lista, inicio=0, fim=None):
    if fim == None:
        fim = len(lista)

    if (fim - inicio) > 1:
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]

    topo_esq = topo_dir = 0
    for k in range(inicio, fim):
        if topo_esq >= len(esquerda):
            lista[k] = direita[topo_dir]
            topo_dir += 1
        elif topo_dir >= len(direita):
            lista[k] = esquerda[topo_esq]
            topo_esq += 1
        elif esquerda[topo_esq] < direita[topo_dir]:
            lista[k] = esquerda[topo_esq]
            topo_esq += 1
        else:
            lista[k] = direita[topo_dir]
            topo_dir += 1


if __name__ == '__main__':

    lista = np.random.randint(1, 1_000_000, size=5_000_000).tolist()

    print(f'Criada lista aleatória com {len(lista):,} elementos.\n'.replace(',','.'))

    tempo_de_execucao = timeit.timeit(lambda: mergesort(lista), number=1)
    print(f'O tempo para a ordenação foi de {tempo_de_execucao:.4f} segundos.')
    print('Os 10 primeiros elementos ordenados são: ')
    print(lista[:10])
    print(f'\nOs 10 últimos elementos ordenados são: ')
    print(lista[-10:])
