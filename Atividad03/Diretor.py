from Servidor import Servidor


class Diretor(Servidor):
    def __init__(self, matricula, nome, idade, rua, cidade):
        super().__init__(matricula, nome, idade, rua, cidade)

    def exibir_diretor(self):
        return f"Diretor: {self.nome}, {self.exibir_servidor()}"
