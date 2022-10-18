from abc import abstractmethod, ABC
from typing import List

from src.academico.dominio.aluno.aluno import Aluno
from src.shared.domain.cpf import CPF


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
