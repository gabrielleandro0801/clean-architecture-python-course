from src.academic.application.indication.enviar_email_indicacao import EnviarEmailIndicacao
from src.academic.domain.aluno.student import Student


class EnviarEmailSimples(EnviarEmailIndicacao):

    def enviar_para(self, indicado: Student) -> None:
        pass
