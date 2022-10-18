from abc import abstractmethod, ABC
from typing import List

from src.shared.domain.cpf import CPF
from src.gamificacao.dominio.selo.selo import Selo


class RepositorioDeSelos(ABC):

    @abstractmethod
    def adicionar(self, selo: Selo) -> None:
        pass

    @abstractmethod
    def selos_do_aluno(self, cpf: CPF) -> List[Selo]:
        pass
