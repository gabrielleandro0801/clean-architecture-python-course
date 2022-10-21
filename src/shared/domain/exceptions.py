class InvalidCPFException(Exception):
    MESSAGE: str = "Invalid CPF"

    def __init__(self, cpf: str or None):
        self.__cpf: str = cpf

    def to_json(self) -> dict:
        return {
            "message": self.MESSAGE,
            "cpf": self.__cpf
        }
