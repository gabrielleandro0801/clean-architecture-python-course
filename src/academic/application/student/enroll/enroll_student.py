from src.academic.application.student.enroll.enroll_student_dto import EnrollStudentDTO
from src.academic.domain.aluno.student import Student
from src.academic.domain.aluno.aluno_matriculado import AlunoMatriculado
from src.academic.domain.aluno.student_repository import StudentRepository
from src.shared.domain.event.event import Event
from src.shared.domain.event.publisher import Publisher


class EnrollStudent:

    def __init__(self, repository: StudentRepository, publisher: Publisher) -> None:
        self.__repositorio: StudentRepository = repository
        self.__publicador: Publisher = publisher

    def enroll(self, dados: EnrollStudentDTO):
        aluno: Student = dados.create_student()
        self.__repositorio.enroll(aluno)

        evento: Event = AlunoMatriculado(aluno.cpf)
        self.__publicador.publish(evento)
