from typing import Any

from src.academico.dominio.aluno.aluno_matriculado import AlunoMatriculado
from src.shared.domain.event.event import Event
from src.shared.domain.event.ouvinte import Ouvinte


class LogDeAlunoMatriculado(Ouvinte):

    def deve_processar(self, evento: Event) -> bool:
        return isinstance(evento, AlunoMatriculado)

    def reage_ao(self, evento: Any) -> None:
        print(f"Aluno com CPF {evento.busca_cpf_do_aluno()} matriculado em {evento.moment()}")
