from typing import List

from src.dominio.aluno.aluno import Aluno
from src.dominio.aluno.cpf import CPF
from src.dominio.aluno.repositorio_de_alunos import RepositorioDeAlunos


class RepositorioDeAlunosEmMemoria(RepositorioDeAlunos):

    __alunos: List[Aluno] = []

    def __init__(self):
        pass

    def buscar_por_cpf(self, cpf: CPF) -> Aluno:
        qtd_alunos: List = list(filter(lambda aluno: aluno.cpf == cpf, self.__alunos))
        if not len(qtd_alunos):
            raise Exception("Aluno nao encontrado")
        return qtd_alunos[0]

    def listar_todos_alunos_matriculados(self) -> List[Aluno]:
        return self.__alunos

    def matricular(self, aluno: Aluno) -> None:
        self.__alunos.append(aluno)
