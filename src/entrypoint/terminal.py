from src.aplicacao.aluno.matricular.matricular_aluno import MatricularAluno
from src.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDTO
from src.dominio.aluno.log_de_aluno_matriculado import LogDeAlunoMatriculado
from src.dominio.publicador_de_eventos import PublicadorDeEventos
from src.infra.aluno.repositorio_em_memoria import RepositorioDeAlunosEmMemoria


def execute():
    nome: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    publicador_de_eventos: PublicadorDeEventos = PublicadorDeEventos()
    publicador_de_eventos.adicionar(LogDeAlunoMatriculado())
    matricular_aluno: MatricularAluno = MatricularAluno(RepositorioDeAlunosEmMemoria(), publicador_de_eventos)
    matricular_aluno.matricular(MatricularAlunoDTO(nome, cpf, email))


if __name__ == '__main__':
    execute()
