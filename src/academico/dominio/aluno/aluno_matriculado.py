from datetime import datetime

from src.shared.domain.cpf import CPF
from src.shared.domain.event.event import Event
from src.shared.domain.event.event_type import EventType


class AlunoMatriculado(Event):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__momento: str = datetime.utcnow().isoformat()

    def moment(self) -> str:
        return self.__momento

    def busca_cpf_do_aluno(self) -> str:
        return self.__cpf.number

    def type(self) -> EventType:
        return EventType.ALUNO_MATRICULADO

    def information(self) -> dict:
        return {
            "cpf": self.__cpf
        }
