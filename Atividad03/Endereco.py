class Endereco:
    def __init__(self, rua, cidade):
        self.__rua = rua
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua

    def set_rua(self, rua):
        self.__rua = rua

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def exibir_endereco(self):
        return f"Endereço: {self.get_rua()}, {self.get_cidade()}"
