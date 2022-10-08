from abc import abstractmethod, ABC

from src.dominio.aluno.aluno import Aluno


class EnviarEmailIndicacao(ABC):

    @abstractmethod
    def enviar_para(self, indicado: Aluno) -> None:
        pass
