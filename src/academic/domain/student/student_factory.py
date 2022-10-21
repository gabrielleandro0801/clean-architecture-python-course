from src.academic.domain.student.student import Student
from src.shared.domain.cpf import CPF
from email import Email


class StudentFactory:
    __student: Student

    def with_name_cpf_and_email(self, name: str, cpf: str, email: str):
        self.__student = Student(
            name=name,
            cpf=CPF(cpf),
            email=Email(email)
        )
        return self

    def with_phone(self, ddd: str, number: str):
        self.__student.add_phone(ddd, number)
        return self

    def criar(self) -> Student:
        return self.__student
