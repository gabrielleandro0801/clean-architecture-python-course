from src.academic.domain.exceptions import InvalidPhoneException


class Phone:

    def __init__(self, ddd: str, number: str):
        if not is_valid(ddd, number):
            raise InvalidPhoneException(ddd, number)
        self.__ddd = ddd
        self.__number = number


def is_valid(ddd: str, number: str):
    return None not in (ddd, number)
