from datetime import datetime

from src.shared.domain.cpf import CPF
from src.shared.domain.event.event import Event
from src.shared.domain.event.event_type import EventType


class EnrolledStudentEvent(Event):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__moment: str = datetime.utcnow().isoformat()

    def moment(self) -> str:
        return self.__moment

    def retrieve_student_cpf(self) -> str:
        return self.__cpf.number

    def type(self) -> EventType:
        return EventType.ENROLLED_STUDENT

    def information(self) -> dict:
        return {
            "cpf": self.__cpf
        }
