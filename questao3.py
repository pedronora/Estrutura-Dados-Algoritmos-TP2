import numpy as np
import timeit


def verificar_duplicados_bruta(lista):
    duplicados = []
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])

    return duplicados


def verificar_duplicados_hashtable(lista):
    contagem = dict()
    duplicados = []

    for n in lista:
        if n in contagem:
            contagem[n] += 1
        else:
            contagem[n] = 1

    for k in contagem:
        if contagem[k] > 1:
            duplicados.append(k)

    return duplicados


if __name__ == '__main__':
    lista = np.random.randint(1, 1_000, size=100_000_000).tolist()
    print(f'O tamanho da lista a ser verificada é de {len(lista):,} elementos.'.replace(',', '.'))

    tempo_de_execução_forca = timeit.timeit(lambda: verificar_duplicados_bruta(lista), number=1)
    print(f'O algoritmo com força bruta teve o tempo de execução de {tempo_de_execução_forca} segundos.')
    tempo_de_execução_hashtable = timeit.timeit(lambda: verificar_duplicados_hashtable(lista), number=1)
    print(f'O algoritmo com hashtable teve o tempo de execução de {tempo_de_execução_hashtable} segundos.')
