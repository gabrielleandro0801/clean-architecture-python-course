from typing import List

from src.shared.domain.event.event import Event
from src.shared.domain.event.ouvinte import Ouvinte


class PublicadorDeEventos:
    __ouvintes: List[Ouvinte] = []

    def adicionar(self, ouvinte: Ouvinte) -> None:
        self.__ouvintes.append(ouvinte)

    def publicar(self, evento: Event):
        for ouvinte in self.__ouvintes:
            ouvinte.processa(evento)
