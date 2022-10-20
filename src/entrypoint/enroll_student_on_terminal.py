from src.academico.aplicacao.aluno.matricular.matricular_aluno import MatricularAluno
from src.academico.aplicacao.aluno.matricular.matricular_aluno_dto import MatricularAlunoDTO
from src.academico.dominio.aluno.log_de_aluno_matriculado import LogDeAlunoMatriculado
from src.gamificacao.aplicacao.gera_selo_aluno_novato import GeraSeloAlunoNovato
from src.gamificacao.infra.selo.repositorio_em_memoria import RepositorioDeSelosEmMemoria
from src.shared.domain.event.publicador_de_eventos import PublicadorDeEventos
from src.academico.infra.aluno.repositorio_em_memoria import RepositorioDeAlunosEmMemoria


def execute():
    nome: str = "Gabriel"
    cpf: str = "00000000000"
    email: str = "gabriel@email.com"

    publicador_de_eventos: PublicadorDeEventos = PublicadorDeEventos()
    publicador_de_eventos.adicionar(LogDeAlunoMatriculado())
    publicador_de_eventos.adicionar(GeraSeloAlunoNovato(RepositorioDeSelosEmMemoria()))

    matricular_aluno: MatricularAluno = MatricularAluno(RepositorioDeAlunosEmMemoria(), publicador_de_eventos)
    matricular_aluno.matricular(MatricularAlunoDTO(nome, cpf, email))


if __name__ == '__main__':
    execute()
