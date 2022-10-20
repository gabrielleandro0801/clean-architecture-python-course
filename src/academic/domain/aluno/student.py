from typing import List

from src.shared.domain.cpf import CPF
from src.academic.domain.aluno.email import Email
from src.academic.domain.aluno.phone import Phone
from src.academic.domain.exceptions import UnableToAddTelefoneException


class Student:

    __phones: List[Phone] = []

    def __init__(self, **kwargs):
        self.__name: str = kwargs.get("name")
        self.__cpf: CPF = kwargs.get("cpf")
        self.__email: Email = kwargs.get("email")

    def add_phone(self, ddd: str, number: str):
        if len(self.__phones) == 2:
            raise UnableToAddTelefoneException(ddd, number)
        self.__phones.append(Phone(ddd, number))

    @property
    def cpf(self) -> CPF:
        return self.__cpf
