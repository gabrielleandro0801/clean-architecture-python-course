from abc import ABC, abstractmethod

from src.shared.domain.event.tipo_de_evento import TipoDeEvento


class Event(ABC):

    @abstractmethod
    def moment(self) -> str:
        pass

    @abstractmethod
    def type(self) -> TipoDeEvento:
        pass

    @abstractmethod
    def information(self) -> dict:
        pass
