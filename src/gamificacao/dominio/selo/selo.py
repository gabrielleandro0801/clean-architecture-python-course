from src.shared.domain.cpf import CPF


class Selo:

    def __init__(self, nome: str, cpf: CPF):
        self.__nome: str = nome
        self.__cpf_do_aluno: CPF = cpf

    @property
    def nome(self) -> str:
        return self.__nome
