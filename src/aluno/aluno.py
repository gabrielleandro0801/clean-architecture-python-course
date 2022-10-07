from typing import List

from cpf import CPF
from email import Email
from telefone import Telefone


class Aluno:

    __telefone: List[Telefone] = []

    def __init__(self, **kwargs):
        self.__nome: str = kwargs.get("nome")
        self.__cpf: CPF = kwargs.get("cpf")
        self.__email: Email = kwargs.get("email")

    def adiciona_telefone(self, ddd: str, numero: str):
        self.__telefone.append(Telefone(ddd, numero))
