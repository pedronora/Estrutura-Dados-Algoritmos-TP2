class TabelaHash:
    def __init__(self, tamanho_inicial=11):
        self.tamanho_inicial = tamanho_inicial
        self.tabela = [[] for _ in range(tamanho_inicial)]
        self.tamanho = 0

    def hash(self, chave):
        return hash(chave) % self.tamanho_inicial

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return

        self.tabela[indice].append([chave, valor])
        self. tamanho += 1

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                self.tamanho -= 1
                return True
        return False

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"


if __name__ == '__main__':
    hash_table = TabelaHash()
    hash_table.inserir("nome", "Alice")
    hash_table.inserir("cidade", "São Paulo")
    hash_table.inserir("pais", "Brasil")

    print("Chaves e valores armazenados na Table Hash: ", hash_table)
    print("Para a chave 'nome', há o valor: ", hash_table.buscar("nome"))
    hash_table.remover("nome")
    print("Removida a chave nome: ", hash_table)
