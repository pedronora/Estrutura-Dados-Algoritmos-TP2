class FilaAtendimento:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def atender_cliente(self):
        if self.tamanho_fila() > 0:
            return self.clientes.pop(0)
        return 'Fila vazia.'

    def tamanho_fila(self):
        return len(self.clientes)


if __name__ == '__main__':
    clientes = [
        "Ana Clara Silva",
        "João Pedro Santos",
        "Maria Fernanda Oliveira",
        "Gabriel Costa Lima",
        "Juliana Pereira Rocha",
        "Lucas Mendes Cardoso",
        "Beatriz Ferreira Souza",
        "Rafael Alves Martins",
        "Larissa Barbosa Torres",
        "Rodrigo Nogueira Ramos",
        "Fernanda Silva Gomes",
        "Carlos Eduardo Farias",
        "Marcela Lopes Alves",
        "Felipe Araújo Santana",
        "Bruna Reis Carvalho"
    ]

    fila_de_atentimento = FilaAtendimento()

    for cliente in clientes:
        fila_de_atentimento.adicionar_cliente(cliente)

    print('Tamanho inicial da fila: ', fila_de_atentimento.tamanho_fila())
    print('Atender 1º Cliente: ', fila_de_atentimento.atender_cliente())
    print('Tamanho atual da fila: ', fila_de_atentimento.tamanho_fila())
