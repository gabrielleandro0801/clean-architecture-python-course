from src.gamificacao.dominio.selo.repositorio_de_selo import RepositorioDeSelos
from src.gamificacao.dominio.selo.selo import Selo
from src.shared.domain.cpf import CPF
from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener
from src.shared.domain.event.event_type import EventType


class GeraSeloAlunoNovato(Listener):

    def __init__(self, repositorio):
        self.__repositorio: RepositorioDeSelos = repositorio

    def must_process(self, evento: Event) -> bool:
        return evento.type() == EventType.ALUNO_MATRICULADO

    def reacts(self, evento: Event) -> None:
        cpf_do_aluno: CPF = evento.information().get("cpf")
        novato: Selo = Selo("Novato", cpf_do_aluno)
        self.__repositorio.adicionar(novato)
