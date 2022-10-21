import datetime

from src.academic.domain.student.student import Student


class Indication:

    def __init__(self, indicated: Student, indicator: Student):
        self.__indicated: Student = indicated
        self.__indicator: Student = indicator
        self.__date = datetime.datetime.now()
