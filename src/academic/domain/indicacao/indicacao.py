import datetime

from src.academic.domain.aluno.student import Student


class Indicacao:

    def __init__(self, indicado: Student, indicante: Student):
        self.__indicado: Student = indicado
        self.__indicante: Student = indicante
        self.__data = datetime.datetime.now()
