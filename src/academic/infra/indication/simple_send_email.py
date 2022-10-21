from src.academic.application.indication.send_email import SendEmailIndication
from src.academic.domain.student.student import Student


class SimpleSendEmail(SendEmailIndication):

    def send_to(self, indicated: Student) -> None:
        print(f"Sending email to student {indicated.name}...")
        print(f"Email sent!")
