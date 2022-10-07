from abc import abstractmethod, ABC
from typing import List

from src.dominio.aluno.aluno import Aluno
from src.dominio.aluno.cpf import CPF


class RepositorioDeAlunos(ABC):

    @abstractmethod
    def matricular(self, aluno: Aluno) -> None:
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: CPF) -> Aluno:
        pass

    @abstractmethod
    def listar_todos_alunos_matriculados(self) -> List[Aluno]:
        pass
