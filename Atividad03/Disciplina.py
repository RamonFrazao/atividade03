from Professor import Professor

class Disciplina(Professor):
    def __init__(self, codigo, nome, cargaHoraria, professor, matricula, nome1, idade, rua, cidade):
        super().__init__(matricula, nome1, idade, rua, cidade)
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__professor = professor

    def get_codigo (self):
        return self.__codigo

    def set_codigo (self, codigo):
        self.__codigo = codigo

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_cargaHoraria (self):
        return self.__cargaHoraria

    def set_cargaHoraria (self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def get_professor (self):
        return self.__professor

    def set_professor (self, professor):
        self.__professor = professor

    def exibir_disciplina(self):
        return f"Disciplina: {self.get_nome()} (Código: {self.get_codigo()}), Carga Horária: {self.get_cargaHoraria()} horas, Professor: {self.exibir_professor()}"
