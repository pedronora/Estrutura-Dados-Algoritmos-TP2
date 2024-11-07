class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            print('A fila está vazia.')
            return None
        return self.itens.pop(0)

    def size(self):
        return len(self.itens)

    def display(self):
        print('Fila: ', self.itens)


def inveter_fila(fila):
    size = fila.size()
    pacientes = []
    while not fila.is_empty():
        pacientes.append(fila.dequeue())

    for n in range(size - 1, -1, -1):
        fila.enqueue(pacientes[n])

    return fila.itens


if __name__ == '__main__':
    pacientes = [
        "Ana Silva",
        "Carlos Oliveira",
        "Beatriz Souza",
        "Fernando Costa",
        "Juliana Santos",
        "Marcos Pereira",
        "Patrícia Almeida",
        "Renato Lima",
        "Sara Mendes",
        "Vinícius Ramos"
    ]

    fila_de_pacientes = Fila()

    for paciente in pacientes:
        fila_de_pacientes.enqueue(paciente)

    fila_de_pacientes.display()
    print('Fila invertida: ', inveter_fila(fila_de_pacientes))
