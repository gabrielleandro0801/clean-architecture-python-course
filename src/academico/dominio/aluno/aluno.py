from typing import List

from src.shared.domain.cpf import CPF
from src.academico.dominio.aluno.email import Email
from src.academico.dominio.aluno.telefone import Telefone
from src.academico.dominio.exceptions import UnableToAddTelefoneException


class Aluno:

    __telefone: List[Telefone] = []

    def __init__(self, **kwargs):
        self.__nome: str = kwargs.get("nome")
        self.__cpf: CPF = kwargs.get("cpf")
        self.__email: Email = kwargs.get("email")

    def adiciona_telefone(self, ddd: str, numero: str):
        if len(self.__telefone) == 2:
            raise UnableToAddTelefoneException(ddd, numero)
        self.__telefone.append(Telefone(ddd, numero))

    @property
    def cpf(self) -> CPF:
        return self.__cpf
