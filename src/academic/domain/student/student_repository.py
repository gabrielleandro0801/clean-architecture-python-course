from abc import abstractmethod, ABC
from typing import List

from src.academic.domain.student.student import Student
from src.shared.domain.cpf import CPF


class StudentRepository(ABC):

    @abstractmethod
    def enroll(self, student: Student) -> None:
        pass

    @abstractmethod
    def find_by_cpf(self, cpf: CPF) -> Student:
        pass

    @abstractmethod
    def list_all(self) -> List[Student]:
        pass
