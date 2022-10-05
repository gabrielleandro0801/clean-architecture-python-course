from aluno import Aluno


class Indicacao:

    def __init__(self, indicado: Aluno, indicante: Aluno):
        self.__indicado: Aluno = indicado
        self.__indicante: Aluno = indicante
