from typing import Any

from src.academic.domain.student.enrolled_student_event import EnrolledStudentEvent
from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener


class LogEnrolledStudentEventListener(Listener):

    def must_process(self, event: Event) -> bool:
        return isinstance(event, EnrolledStudentEvent)

    def reacts(self, event: Any) -> None:
        print(f"{__class__.__name__} | Student with CPF {event.retrieve_student_cpf()} enrolled at {event.moment()}")
