from typing import List

from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener


class Publisher:
    __listeners: List[Listener] = []

    def add(self, listener: Listener) -> None:
        self.__listeners.append(listener)

    def publish(self, event: Event):
        print(f"{__class__.__name__} | Publishing event\n")
        for listener in self.__listeners:
            listener.process(event)
        print(f"{__class__.__name__} | All listeners listened to the event")
