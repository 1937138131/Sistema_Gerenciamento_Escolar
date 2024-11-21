from project.models.Aluno import Aluno
from project.models.Pessoa import Pessoa
from project.models.Professor import Professor
from project.models.Turma import Turma

professor = Professor("João Silva", "40", "Matemática")
turma = Turma("8º Ano", professor)

aluno1 = Aluno("Maria", 13)
aluno2 = Aluno("Pedro", 14)

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

professor.adicionar_nota(aluno1, 9.5)
professor.adicionar_nota(aluno1, 8.0)
professor.adicionar_nota(aluno2, 7.0)


turma.listar_alunos()
professor.exibir_informações()
aluno1.exibir_informações()
aluno2.exibir_informações()
