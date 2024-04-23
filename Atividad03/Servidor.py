from Endereco import Endereco

class Servidor(Endereco):
    def __init__(self, matricula, nome, idade, rua, cidade):
        super().__init__(rua, cidade)
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade

    def get_matricula (self):
        return self.__matricula

    def set_matricula (self, matricula):
        self.__matricula = matricula

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_idade (self):
        return self.__idade

    def set_idade (self, idade):
        self.__idade = idade

    def exibir_servidor(self):
        return f"Matrícula: {self.get_matricula()}, Nome: {self.get_nome()}, Idade: {self.get_idade()}, {self.exibir_endereco()}"
