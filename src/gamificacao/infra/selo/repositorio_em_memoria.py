from typing import List

from src.shared.domain.cpf import CPF
from src.gamificacao.dominio.selo.repositorio_de_selo import RepositorioDeSelos
from src.gamificacao.dominio.selo.selo import Selo


class RepositorioDeSelosEmMemoria(RepositorioDeSelos):
    __selos: List[Selo] = []

    def selos_do_aluno(self, cpf: CPF) -> List[Selo]:
        return list(filter(lambda selo: selo.cpf == cpf.numero, self.__selos))

    def adicionar(self, selo: Selo) -> None:
        self.__selos.append(selo)
