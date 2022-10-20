import re

from src.academic.domain.exceptions import InvalidEmailException

regex = re.compile(r'\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}')


class CPF:

    def __init__(self, value: str):
        if not is_valid(value):
            raise InvalidEmailException(value)
        self.__number: str = value

    @property
    def number(self) -> str:
        return self.__number


def is_valid(valor: str) -> bool:
    return valor is not None and re.fullmatch(regex, valor)
