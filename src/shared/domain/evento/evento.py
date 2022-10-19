from abc import ABC, abstractmethod

from src.shared.domain.evento.tipo_de_evento import TipoDeEvento


class Evento(ABC):

    @abstractmethod
    def momento(self) -> str:
        pass

    @abstractmethod
    def tipo(self) -> TipoDeEvento:
        pass

    @abstractmethod
    def informacoes(self) -> dict:
        pass
