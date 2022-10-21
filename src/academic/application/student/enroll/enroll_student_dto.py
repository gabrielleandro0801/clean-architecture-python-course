from src.academic.domain.student.student import Student
from src.academic.domain.student.email import Email
from src.shared.domain.cpf import CPF


class EnrollStudentDTO:
    __name: str
    __cpf: str
    __email: str

    def __init__(self, name: str, cpf: str, email: str) -> None:
        self.__name: str = name
        self.__cpf: str = cpf
        self.__email: str = email

    def create_student(self) -> Student:
        return Student(
            name=self.__name,
            cpf=CPF(self.__cpf),
            email=Email(self.__email)
        )
