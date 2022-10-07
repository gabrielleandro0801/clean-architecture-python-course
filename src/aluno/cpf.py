import re

from exceptions import InvalidEmailException

regex = re.compile(r'\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}')


class CPF:

    def __init__(self, valor: str):
        if not is_valid(valor):
            raise InvalidEmailException(valor)
        self.__valor: str = valor


def is_valid(valor: str) -> bool:
    return valor is None or not re.fullmatch(regex, valor)
