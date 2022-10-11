from src.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDTO
from src.dominio.aluno.aluno import Aluno
from src.dominio.aluno.repositorio_de_alunos import RepositorioDeAlunos


class MatricularAluno:

    def __init__(self, repositorio: RepositorioDeAlunos) -> None:
        self.__repositorio: RepositorioDeAlunos = repositorio

    def matricular(self, dados: MatricularAlunoDTO):
        aluno: Aluno = dados.criar_aluno()
        self.__repositorio.matricular(aluno)
