from src.academic.domain.aluno.cifrador_de_senha import CifradorDeSenha
import hashlib


class CifradorDeSenhaMD5(CifradorDeSenha):
    def cifrar(self, senha: str) -> str:
        return hashlib.md5(senha.encode()).hexdigest()

    def validar_senha_cifrada(self, cifrada: str, senha: str) -> bool:
        return cifrada == self.cifrar(senha)
