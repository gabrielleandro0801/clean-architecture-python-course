from datetime import datetime

from src.academico.dominio.aluno.cpf import CPF
from src.academico.dominio.evento import Evento


class AlunoMatriculado(Evento):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__momento: str = datetime.utcnow().isoformat()

    def momento(self) -> str:
        return self.__momento

    def busca_cpf_do_aluno(self) -> str:
        return self.__cpf.numero
