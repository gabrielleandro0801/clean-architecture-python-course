from typing import Any

from src.academico.dominio.aluno.aluno_matriculado import AlunoMatriculado
from src.academico.dominio.evento import Evento
from src.academico.dominio.ouvinte import Ouvinte


class LogDeAlunoMatriculado(Ouvinte):

    def deve_processar(self, evento: Evento) -> bool:
        return isinstance(evento, AlunoMatriculado)

    def reage_ao(self, evento: Any) -> None:
        print(f"Aluno com CPF {evento.busca_cpf_do_aluno()} matriculado em {evento.momento()}")
