from src.academic.domain.aluno.student import Student
from src.shared.domain.cpf import CPF
from email import Email


class FabricaDeAluno:
    __aluno: Student

    def com_nome_cpf_e_email(self, nome: str, cpf: str, email: str):
        self.__aluno = Student(
            nome=nome,
            cpf=CPF(cpf),
            email=Email(email)
        )
        return self

    def com_telefone(self, ddd: str, numero: str):
        self.__aluno.add_phone(ddd, numero)
        return self

    def criar(self) -> Student:
        return self.__aluno
