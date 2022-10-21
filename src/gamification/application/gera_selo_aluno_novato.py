from src.gamification.domain.tag.tag_repository import TagRepository
from src.gamification.domain.tag.tag import Tag
from src.shared.domain.cpf import CPF
from src.shared.domain.event.event import Event
from src.shared.domain.event.listener import Listener
from src.shared.domain.event.event_type import EventType


class GeraSeloAlunoNovato(Listener):

    def __init__(self, repository: TagRepository):
        self.__repository: TagRepository = repository

    def must_process(self, event: Event) -> bool:
        return event.type() == EventType.ENROLLED_STUDENT

    def reacts(self, event: Event) -> None:
        student_cpf: CPF = event.information().get("cpf")
        new: Tag = Tag("New", student_cpf)
        self.__repository.add(new)
