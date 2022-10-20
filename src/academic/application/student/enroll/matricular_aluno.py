from src.academic.application.student.enroll.matricular_aluno_dto import MatricularAlunoDTO
from src.academic.domain.aluno.aluno import Aluno
from src.academic.domain.aluno.aluno_matriculado import AlunoMatriculado
from src.academic.domain.aluno.repositorio_de_alunos import RepositorioDeAlunos
from src.shared.domain.event.event import Event
from src.shared.domain.event.publisher import Publisher


class MatricularAluno:

    def __init__(self, repositorio: RepositorioDeAlunos, publicador: Publisher) -> None:
        self.__repositorio: RepositorioDeAlunos = repositorio
        self.__publicador: Publisher = publicador

    def matricular(self, dados: MatricularAlunoDTO):
        aluno: Aluno = dados.criar_aluno()
        self.__repositorio.matricular(aluno)

        evento: Event = AlunoMatriculado(aluno.cpf)
        self.__publicador.publish(evento)
