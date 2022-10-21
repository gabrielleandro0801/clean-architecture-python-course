from typing import List

from src.academic.domain.student.student import Student
from src.shared.domain.cpf import CPF
from src.academic.domain.student.student_repository import StudentRepository


class RepositorioDeAlunosEmMemoria(StudentRepository):

    __alunos: List[Student] = []

    def find_by_cpf(self, cpf: CPF) -> Student:
        qtd_alunos: List = list(filter(lambda aluno: aluno.cpf == cpf, self.__alunos))
        if not len(qtd_alunos):
            raise Exception("Student nao encontrado")
        return qtd_alunos[0]

    def list_all(self) -> List[Student]:
        return self.__alunos

    def enroll(self, aluno: Student) -> None:
        self.__alunos.append(aluno)
