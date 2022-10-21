from src.academic.application.student.enroll.enroll_student import EnrollStudent
from src.academic.application.student.enroll.enroll_student_dto import EnrollStudentDTO
from src.academic.domain.student.log_de_aluno_matriculado import LogDeAlunoMatriculado
from src.gamificacao.aplicacao.gera_selo_aluno_novato import GeraSeloAlunoNovato
from src.gamificacao.infra.selo.repositorio_em_memoria import RepositorioDeSelosEmMemoria
from src.shared.domain.event.publisher import Publisher
from src.academic.infra.student.memory_repository import MemoryStudentRepository


def execute():
    name: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    publisher: Publisher = Publisher()
    publisher.add(LogDeAlunoMatriculado())
    publisher.add(GeraSeloAlunoNovato(RepositorioDeSelosEmMemoria()))

    matricular_aluno: EnrollStudent = EnrollStudent(MemoryStudentRepository(), publisher)
    matricular_aluno.enroll(EnrollStudentDTO(name, cpf, email))


if __name__ == '__main__':
    execute()
