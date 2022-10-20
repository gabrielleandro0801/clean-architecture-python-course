import re

from src.academic.domain.exceptions import InvalidEmailException

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Email:

    def __init__(self, endereco: str):
        if not is_valid(endereco):
            raise InvalidEmailException(endereco)
        self.__endereco: str = endereco


def is_valid(endereco: str) -> bool:
    return endereco is not None and bool(re.fullmatch(regex, endereco))
