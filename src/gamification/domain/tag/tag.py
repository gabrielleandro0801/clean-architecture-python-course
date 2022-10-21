from src.shared.domain.cpf import CPF


class Tag:

    def __init__(self, name: str, cpf: CPF):
        self.__name: str = name
        self.__student_cpf: CPF = cpf

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cpf(self) -> str:
        return self.__student_cpf.number
