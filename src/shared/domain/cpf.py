import re

from src.shared.domain.exceptions import InvalidCPFException

from validate_docbr import CPF as CPFValidator


class CPF:

    def __init__(self, value: str):
        if not is_valid(value):
            raise InvalidCPFException(value)
        self.__number: str = value

    @property
    def number(self) -> str:
        return self.__number


def is_valid(value: str) -> bool:
    cpf = CPFValidator()
    return value is not None and cpf.validate(value)
