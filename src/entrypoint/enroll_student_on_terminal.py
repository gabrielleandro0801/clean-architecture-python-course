from src.academic.application.student.enroll.matricular_aluno import MatricularAluno
from src.academic.application.student.enroll.matricular_aluno_dto import MatricularAlunoDTO
from src.academic.domain.aluno.log_de_aluno_matriculado import LogDeAlunoMatriculado
from src.gamificacao.aplicacao.gera_selo_aluno_novato import GeraSeloAlunoNovato
from src.gamificacao.infra.selo.repositorio_em_memoria import RepositorioDeSelosEmMemoria
from src.shared.domain.event.publisher import Publisher
from src.academic.infra.aluno.repositorio_em_memoria import RepositorioDeAlunosEmMemoria


def execute():
    name: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    publisher: Publisher = Publisher()
    publisher.add(LogDeAlunoMatriculado())
    publisher.add(GeraSeloAlunoNovato(RepositorioDeSelosEmMemoria()))

    matricular_aluno: MatricularAluno = MatricularAluno(RepositorioDeAlunosEmMemoria(), publisher)
    matricular_aluno.matricular(MatricularAlunoDTO(name, cpf, email))


if __name__ == '__main__':
    execute()
