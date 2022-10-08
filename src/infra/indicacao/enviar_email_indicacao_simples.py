from src.aplicacao.indicacao.enviar_email_indicacao import EnviarEmailIndicacao
from src.dominio.aluno.aluno import Aluno


class EnviarEmailSimples(EnviarEmailIndicacao):

    def enviar_para(self, indicado: Aluno) -> None:
        pass
