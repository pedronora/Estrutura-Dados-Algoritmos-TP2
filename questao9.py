import random


def ordenar(lista):
    size = len(lista)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if lista[min_index] > lista[j]:
                min_index = j

        lista[min_index], lista[i] = lista[i], lista[min_index]


if __name__ == '__main__':

    lista = [random.randint(1, 100) for _ in range(20)]

    print('Lista desordenada: ',  lista)
    
    ordenar(lista)

    print('Lista ordenada: ', lista)
