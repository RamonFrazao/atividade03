class Sala:
    def __init__(self, numero, capacidade):
        self.__numero = numero
        self.__capacidade = capacidade

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_capacidade (self):
        return self.__capacidade

    def set_capacidade (self, capacidade):
        self.__capacidade = capacidade
    def exibir_sala(self):
        return f"Sala: {self.get_numero()}, Capacidade: {self.get_capacidade()}"
