from src.academic.application.student.enroll.enroll_student import EnrollStudent
from src.academic.application.student.enroll.enroll_student_dto import EnrollStudentDTO
from src.academic.domain.student.log_enrolled_student_event_listener import LogEnrolledStudentEventListener
from src.gamification.application.create_tag_new_student_event_listener import CreateTagForNewStudentEventListener
from src.gamification.infra.tag.memory_tag_repository import MemoryTagRepository
from src.shared.domain.event.publisher import Publisher
from src.academic.infra.student.memory_repository import MemoryStudentRepository


def execute():
    name: str = "Gabriel"
    cpf: str = "44697109899"
    email: str = "gabriel@email.com"

    publisher: Publisher = Publisher()
    publisher.add(LogEnrolledStudentEventListener())
    publisher.add(CreateTagForNewStudentEventListener(MemoryTagRepository()))

    enroll_student: EnrollStudent = EnrollStudent(MemoryStudentRepository(), publisher)
    enroll_student.enroll(EnrollStudentDTO(name, cpf, email))


if __name__ == '__main__':
    execute()
