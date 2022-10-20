from datetime import datetime

from src.shared.domain.cpf import CPF
from src.shared.domain.event.event import Event
from src.shared.domain.event.tipo_de_evento import TipoDeEvento


class AlunoMatriculado(Event):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__momento: str = datetime.utcnow().isoformat()

    def moment(self) -> str:
        return self.__momento

    def busca_cpf_do_aluno(self) -> str:
        return self.__cpf.number

    def type(self) -> TipoDeEvento:
        return TipoDeEvento.ALUNO_MATRICULADO

    def information(self) -> dict:
        return {
            "cpf": self.__cpf
        }
