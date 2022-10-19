from src.gamificacao.dominio.selo.repositorio_de_selo import RepositorioDeSelos
from src.gamificacao.dominio.selo.selo import Selo
from src.shared.domain.cpf import CPF
from src.shared.domain.evento.evento import Evento
from src.shared.domain.evento.ouvinte import Ouvinte
from src.shared.domain.evento.tipo_de_evento import TipoDeEvento


class GeraSeloAlunoNovato(Ouvinte):

    def __init__(self, repositorio):
        self.__repositorio: RepositorioDeSelos = repositorio

    def deve_processar(self, evento: Evento) -> bool:
        return evento.tipo() == TipoDeEvento.ALUNO_MATRICULADO

    def reage_ao(self, evento: Evento) -> None:
        cpf_do_aluno: CPF = evento.informacoes().get("cpf")
        novato: Selo = Selo("Novato", cpf_do_aluno)
        self.__repositorio.adicionar(novato)
