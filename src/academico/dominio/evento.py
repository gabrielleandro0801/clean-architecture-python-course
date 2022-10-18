from abc import ABC, abstractmethod


class Evento(ABC):

    @abstractmethod
    def momento(self) -> str:
        pass
