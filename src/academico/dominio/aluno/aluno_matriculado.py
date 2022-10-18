from datetime import datetime

from src.shared.domain.cpf import CPF
from src.shared.domain.evento.evento import Evento
from src.shared.domain.evento.tipo_de_evento import TipoDeEvento


class AlunoMatriculado(Evento):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__momento: str = datetime.utcnow().isoformat()

    def momento(self) -> str:
        return self.__momento

    def busca_cpf_do_aluno(self) -> str:
        return self.__cpf.numero

    def tipo(self) -> TipoDeEvento:
        return TipoDeEvento.ALUNO_MATRICULADO

    def informacoes(self) -> dict:
        return {
            "cpf": self.__cpf
        }
