from abc import ABC, abstractmethod

from src.shared.domain.event.event import Event


class Ouvinte(ABC):

    def processa(self, evento: Event) -> None:
        if self.deve_processar(evento):
            self.reage_ao(evento)

    @abstractmethod
    def deve_processar(self, evento: Event) -> bool:
        pass

    @abstractmethod
    def reage_ao(self, evento: Event):
        pass
