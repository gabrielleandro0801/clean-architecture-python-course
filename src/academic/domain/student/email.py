import re

from src.academic.domain.exceptions import InvalidEmailException

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Email:

    def __init__(self, address: str):
        if not is_valid(address):
            raise InvalidEmailException(address)
        self.__address: str = address


def is_valid(address: str) -> bool:
    return address is not None and bool(re.fullmatch(regex, address))
