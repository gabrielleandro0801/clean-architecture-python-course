class InvalidEmailException(Exception):
    MESSAGE: str = "Invalid email"

    def __init__(self, email: str or None):
        self.__email: str = email

    def to_json(self) -> dict:
        return {
            "message": InvalidEmailException.MESSAGE,
            "email": self.__email
        }


class InvalidTelefoneException(Exception):
    MESSAGE: str = "Invalid telefone"

    def __init__(self, ddd: str, telefone: str or None):
        self.__ddd: str = ddd
        self.__telefone: str = telefone

    def to_json(self) -> dict:
        return {
            "message": InvalidEmailException.MESSAGE,
            "telefone": self.__telefone
        }