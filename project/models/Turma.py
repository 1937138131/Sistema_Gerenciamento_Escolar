class Turma:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            self.professor.alunos.append(aluno)
        else:
            print(f"Aluno {aluno.nome} já está na turma.")

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}")
