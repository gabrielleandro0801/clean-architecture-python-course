from abc import abstractmethod, ABC


class CifradorDeSenha(ABC):

    @abstractmethod
    def cifrar(self, senha: str) -> str:
        pass

    @abstractmethod
    def validar_senha_cifrada(self, cifrada: str, senha: str) -> bool:
        pass
