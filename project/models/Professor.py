from project.models.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, idade: str, disciplina: str):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.alunos = []

    def adicionar_nota(self, aluno, nota):
        if aluno in self.alunos:
            self.alunos.append(nota)
        else:
            print(f"Aluno {aluno.nome} não está na lista do professor.")

    def exibir_informações(self):
        print(f"Professor: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}.")

