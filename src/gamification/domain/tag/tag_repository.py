from abc import abstractmethod, ABC
from typing import List

from src.shared.domain.cpf import CPF
from src.gamification.domain.tag.tag import Tag


class TagRepository(ABC):

    @abstractmethod
    def add(self, tag: Tag) -> None:
        pass

    @abstractmethod
    def find_student_tags(self, cpf: CPF) -> List[Tag]:
        pass
