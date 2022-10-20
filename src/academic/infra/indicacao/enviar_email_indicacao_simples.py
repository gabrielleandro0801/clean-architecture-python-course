from src.academic.application.indication.enviar_email_indicacao import EnviarEmailIndicacao
from src.academic.domain.aluno.aluno import Aluno


class EnviarEmailSimples(EnviarEmailIndicacao):

    def enviar_para(self, indicado: Aluno) -> None:
        pass
