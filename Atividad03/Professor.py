from Endereco import Endereco
from Disciplina import Disciplina


class Professor(Endereco, Disciplina):
    def __init__(self, matricula, nome, idade, rua, cidade, codigo, nome1, cargaHoraria, professor, matricula1):
        super().__init__(rua, cidade)
        super ().__init__ (codigo, nome1, cargaHoraria, professor, matricula1)
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_idade (self):
        return self.__idade

    def set_idade (self, idade):
        self.__idade= idade

    def exibir_professor(self):
        return f"Matrícula: {self.get_matricula()}, Nome: {self.get_nome()}, Idade: {self.get_idade()}, {self.exibir_endereco()}, {self.exibir_disciplina()}"
