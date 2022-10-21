from src.academic.domain.student.password_encryptor import PasswordEncryptor
import hashlib


class MD5PasswordEncryptor(PasswordEncryptor):
    def encrypt(self, password: str) -> str:
        print(f"{__class__.__name__} | Hashing password in MD5")
        return hashlib.md5(password.encode()).hexdigest()

    def validate_encrypted_password(self, encrypted: str, password: str) -> bool:
        return encrypted == self.encrypt(password)
