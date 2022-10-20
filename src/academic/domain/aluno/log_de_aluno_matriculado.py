from typing import Any

from src.academic.domain.aluno.aluno_matriculado import AlunoMatriculado
from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener


class LogDeAlunoMatriculado(Listener):

    def must_process(self, evento: Event) -> bool:
        return isinstance(evento, AlunoMatriculado)

    def reacts(self, evento: Any) -> None:
        print(f"Aluno com CPF {evento.busca_cpf_do_aluno()} matriculado em {evento.moment()}")
