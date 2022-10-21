from src.academic.application.student.enroll.enroll_student import EnrollStudent
from src.academic.application.student.enroll.enroll_student_dto import EnrollStudentDTO
from src.academic.domain.student.log_de_aluno_matriculado import LogDeAlunoMatriculado
from src.gamification.application.gera_selo_aluno_novato import GeraSeloAlunoNovato
from src.gamification.infra.tag.memory_tag_repository import MemoryTagRepository
from src.shared.domain.event.publisher import Publisher
from src.academic.infra.student.memory_repository import MemoryStudentRepository


def execute():
    name: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    publisher: Publisher = Publisher()
    publisher.add(LogDeAlunoMatriculado())
    publisher.add(GeraSeloAlunoNovato(MemoryTagRepository()))

    enroll_student: EnrollStudent = EnrollStudent(MemoryStudentRepository(), publisher)
    enroll_student.enroll(EnrollStudentDTO(name, cpf, email))


if __name__ == '__main__':
    execute()
