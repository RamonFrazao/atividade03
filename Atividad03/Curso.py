class Curso:
    def __init__(self, codigo, nome, cargaHoraia):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraia

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nome (self):
        return self.__nome

    def set_nome (self, nome):
        self.__nome = nome

    def get_cargaHoraria (self):
        return self.__cargaHoraria

    def set_codigo (self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def exibir_curso(self):
        return f"Curso: {self.get_nome()} (Código: {self.get_codigo()}), Carga Horária: {self.get_cargaHoraria()} horas"
