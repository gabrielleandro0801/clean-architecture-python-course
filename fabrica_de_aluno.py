from aluno import Aluno
from cpf import CPF
from email import Email


class FabricaDeAluno:
    __aluno: Aluno

    def com_nome_cpf_e_email(self, nome: str, cpf: str, email: str):
        self.__aluno = Aluno(
            nome=nome,
            cpf=CPF(cpf),
            email=Email(email)
        )
        return self

    def com_telefone(self, ddd: str, numero: str):
        self.__aluno.adiciona_telefone(ddd, numero)
        return self

    def criar(self) -> Aluno:
        return self.__aluno
