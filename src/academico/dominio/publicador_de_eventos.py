from typing import List

from src.academico.dominio.evento import Evento
from src.academico.dominio.ouvinte import Ouvinte


class PublicadorDeEventos:
    __ouvintes: List[Ouvinte] = []

    def adicionar(self, ouvinte: Ouvinte) -> None:
        self.__ouvintes.append(ouvinte)

    def publicar(self, evento: Evento):
        for ouvinte in self.__ouvintes:
            ouvinte.processa(evento)
