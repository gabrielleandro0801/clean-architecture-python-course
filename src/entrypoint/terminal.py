from src.aplicacao.aluno.matricular.matricular_aluno import MatricularAluno
from src.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDTO
from src.infra.aluno.repositorio_em_memoria import RepositorioDeAlunosEmMemoria


def execute():
    nome: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    matricular_aluno: MatricularAluno = MatricularAluno(RepositorioDeAlunosEmMemoria())
    matricular_aluno.matricular(MatricularAlunoDTO(nome, cpf, email))


if __name__ == '__main__':
    execute()
