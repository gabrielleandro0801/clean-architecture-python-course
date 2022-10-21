from typing import List

from src.academic.domain.student.student import Student
from src.shared.domain.cpf import CPF
from src.academic.domain.student.student_repository import StudentRepository


class RepositorioDeAlunosComSQLite(StudentRepository):

    def __init__(self, connection):
        self.__connection = connection

    def find_by_cpf(self, cpf: CPF) -> Student:
        pass

    def list_all(self) -> List[Student]:
        pass

    def enroll(self, aluno: Student) -> None:
        pass
