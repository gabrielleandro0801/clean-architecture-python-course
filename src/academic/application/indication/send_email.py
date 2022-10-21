from abc import abstractmethod, ABC

from src.academic.domain.student.student import Student


class SendEmailIndication(ABC):

    @abstractmethod
    def send_to(self, indicated: Student) -> None:
        pass
