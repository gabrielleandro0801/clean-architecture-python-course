from typing import List

from src.academic.domain.exceptions import UnableToAddPhoneException
from src.shared.domain.cpf import CPF
from src.academic.domain.student.email import Email
from src.academic.domain.student.phone import Phone


class Student:

    __phones: List[Phone] = []

    def __init__(self, **kwargs):
        self.__name: str = kwargs.get("name")
        self.__cpf: CPF = kwargs.get("cpf")
        self.__email: Email = kwargs.get("email")

    def add_phone(self, ddd: str, number: str):
        if len(self.__phones) == 2:
            raise UnableToAddPhoneException(ddd, number)
        self.__phones.append(Phone(ddd, number))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cpf(self) -> CPF:
        return self.__cpf
