from abc import ABC, abstractmethod

from src.academico.dominio.evento import Evento


class Ouvinte(ABC):

    def processa(self, evento: Evento) -> None:
        if self.deve_processar(evento):
            self.reage_ao(evento)

    @abstractmethod
    def deve_processar(self, evento: Evento) -> bool:
        pass

    @abstractmethod
    def reage_ao(self, evento: Evento) -> bool:
        pass
