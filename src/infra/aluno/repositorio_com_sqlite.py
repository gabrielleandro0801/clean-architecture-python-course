from typing import List

from src.dominio.aluno.aluno import Aluno
from src.dominio.aluno.cpf import CPF
from src.dominio.aluno.repositorio_de_alunos import RepositorioDeAlunos


class RepositorioDeAlunosComSQLite(RepositorioDeAlunos):

    def __init__(self, connection):
        self.__connection = connection

    def buscar_por_cpf(self, cpf: CPF) -> Aluno:
        pass

    def listar_todos_alunos_matriculados(self) -> List[Aluno]:
        pass

    def matricular(self, aluno: Aluno) -> None:
        pass