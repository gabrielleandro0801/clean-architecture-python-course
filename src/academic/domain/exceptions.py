class InvalidEmailException(Exception):
    MESSAGE: str = "Invalid email"

    def __init__(self, email: str or None):
        self.__email: str = email

    def to_json(self) -> dict:
        return {
            "message": self.MESSAGE,
            "email": self.__email
        }


class InvalidPhoneException(Exception):
    MESSAGE: str = "Invalid phone"

    def __init__(self, ddd: str, phone: str or None):
        self.__ddd: str = ddd
        self.__phone: str = phone

    def to_json(self) -> dict:
        return {
            "message": self.MESSAGE,
            "ddd": self.__ddd,
            "phone": self.__phone
        }


class UnableToAddPhoneException(Exception):
    MESSAGE: str = "Unable to add phone"

    def __init__(self, ddd: str, phone: str or None):
        self.__ddd: str = ddd
        self.__phone: str = phone

    def to_json(self) -> dict:
        return {
            "message": self.MESSAGE,
            "ddd": self.__ddd,
            "phone": self.__phone
        }
