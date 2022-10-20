from src.academic.domain.aluno.aluno import Aluno
from src.academic.domain.aluno.email import Email
from src.shared.domain.cpf import CPF


class MatricularAlunoDTO:
    __nome: str
    __cpf: str
    __email: str

    def __init__(self, nome, cpf, email) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email

    def criar_aluno(self) -> Aluno:
        return Aluno(
            nome=self.__nome,
            cpf=CPF(self.__cpf),
            email=Email(self.__email)
        )
