from abc import ABC, abstractmethod

from src.shared.domain.event.event import Event


class Listener(ABC):

    def process(self, event: Event) -> None:
        if self.must_process(event):
            self.reacts(event)

    @abstractmethod
    def must_process(self, event: Event) -> bool:
        pass

    @abstractmethod
    def reacts(self, event: Event):
        pass
