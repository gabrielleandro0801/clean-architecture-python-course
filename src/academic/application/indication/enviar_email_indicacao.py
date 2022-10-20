from abc import abstractmethod, ABC

from src.academic.domain.aluno.student import Student


class EnviarEmailIndicacao(ABC):

    @abstractmethod
    def enviar_para(self, indicado: Student) -> None:
        pass
