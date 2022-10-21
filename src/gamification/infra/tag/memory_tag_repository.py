from typing import List

from src.shared.domain.cpf import CPF
from src.gamification.domain.tag.tag_repository import TagRepository
from src.gamification.domain.tag.tag import Tag


class MemoryTagRepository(TagRepository):
    __tags: List[Tag] = []

    def find_student_tags(self, cpf: CPF) -> List[Tag]:
        return list(filter(lambda tag: tag.cpf == cpf.number, self.__tags))

    def add(self, tag: Tag) -> None:
        self.__tags.append(tag)
