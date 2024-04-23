from Servidor import Servidor
from Curso import Curso


class Coordenador(Servidor, Curso):
    def __init__(self, matricula, nome, idade, rua, cidade, codigo_curso):
        Servidor.__init__(self, matricula, nome, idade, rua, cidade)
        Curso.__init__ (self, codigo_curso, "Nome do Curso", 0)

    def exibir_coordenador(self):
        return f"Coordenador do Curso: {self.get_nome()}, {self.exibir_servidor()}, {self.exibir_curso()}"
