from Endereco import Endereco
from Curso import Curso


class Aluno(Endereco, Curso):
    def __init__(self, matricula, nome, idade, rua, cidade, codigo_curso):
        Endereco.__init__(self, rua, cidade)
        Curso.__init__ (self, codigo_curso, "Nome do Curso", 0)
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def exibir_aluno(self):
        return f"Matrícula: {self.get_matricula()}, Nome: {self.get_nome()}, Idade: {self.get_idade()}, {self.exibir_endereco()}, {self.exibir_curso()}"
