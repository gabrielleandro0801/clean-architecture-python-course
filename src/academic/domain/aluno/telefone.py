from src.academic.domain.exceptions import InvalidTelefoneException


class Telefone:

    def __init__(self, ddd: str, numero: str):
        if not is_valid(ddd, numero):
            raise InvalidTelefoneException(ddd, numero)
        self.__ddd = ddd
        self.__numero = numero


def is_valid(ddd: str, numero: str):
    return None not in (ddd, numero)
