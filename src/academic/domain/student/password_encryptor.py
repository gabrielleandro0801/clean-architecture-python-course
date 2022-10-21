from abc import abstractmethod, ABC


class PasswordEncryptor(ABC):

    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

    @abstractmethod
    def validate_encrypted_password(self, encrypted: str, password: str) -> bool:
        pass
