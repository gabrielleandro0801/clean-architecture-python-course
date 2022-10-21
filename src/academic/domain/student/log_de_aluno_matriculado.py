from typing import Any

from src.academic.domain.student.enrolled_student_event import EnrolledStudentEvent
from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener


class LogDeAlunoMatriculado(Listener):

    def must_process(self, evento: Event) -> bool:
        return isinstance(evento, EnrolledStudentEvent)

    def reacts(self, evento: Any) -> None:
        print(f"Student com CPF {evento.retrieve_student_cpf()} matriculado em {evento.moment()}")
