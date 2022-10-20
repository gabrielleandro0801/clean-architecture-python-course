from abc import ABC, abstractmethod

from src.shared.domain.event.event_type import EventType


class Event(ABC):

    @abstractmethod
    def moment(self) -> str:
        pass

    @abstractmethod
    def type(self) -> EventType:
        pass

    @abstractmethod
    def information(self) -> dict:
        pass
