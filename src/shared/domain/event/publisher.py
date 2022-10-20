from typing import List

from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener


class Publisher:
    __listeners: List[Listener] = []

    def add(self, listener: Listener) -> None:
        self.__listeners.append(listener)

    def publish(self, event: Event):
        for listener in self.__listeners:
            listener.process(event)
