from typing import List

from src.academic.domain.student.student import Student
from src.shared.domain.cpf import CPF
from src.academic.domain.student.student_repository import StudentRepository


class MemoryStudentRepository(StudentRepository):

    __students: List[Student] = []

    def find_by_cpf(self, cpf: CPF) -> Student:
        students_found: List = list(filter(lambda student: student.cpf == cpf, self.__students))
        if not len(students_found):
            raise Exception("Student not found")
        return students_found[0]

    def list_all(self) -> List[Student]:
        return self.__students

    def enroll(self, aluno: Student) -> None:
        print(f"{__class__.__name__} | Saving student in memory")
        self.__students.append(aluno)
