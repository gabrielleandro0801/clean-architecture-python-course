from datetime import datetime

from src.dominio.aluno.cpf import CPF
from src.dominio.evento import Evento


class AlunoMatriculado(Evento):

    def __init__(self, cpf: CPF):
        self.__cpf: CPF = cpf
        self.__momento: str = datetime.utcnow().isoformat()

    def momento(self) -> str:
        return self.__momento

    def busca_cpf_do_aluno(self) -> str:
        return self.__cpf.numero
