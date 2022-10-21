from src.academic.application.student.enroll.enroll_student_dto import EnrollStudentDTO
from src.academic.domain.student.student import Student
from src.academic.domain.student.enrolled_student_event import EnrolledStudentEvent
from src.academic.domain.student.student_repository import StudentRepository
from src.shared.domain.event.event import Event
from src.shared.domain.event.publisher import Publisher


class EnrollStudent:

    def __init__(self, repository: StudentRepository, publisher: Publisher) -> None:
        self.__repository: StudentRepository = repository
        self.__publisher: Publisher = publisher

    def enroll(self, student_dto: EnrollStudentDTO):
        print(f"{__class__.__name__} | Enrolling student")
        student: Student = student_dto.create_student()
        self.__repository.enroll(student)

        event: Event = EnrolledStudentEvent(student.cpf)
        self.__publisher.publish(event)
