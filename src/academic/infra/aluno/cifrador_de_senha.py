from src.academic.domain.student.password_encryptor import PasswordEncryptor
import hashlib


class CifradorDeSenhaMD5(PasswordEncryptor):
    def encrypt(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

    def validate_encrypted_password(self, encrypted: str, password: str) -> bool:
        return encrypted == self.encrypt(password)
