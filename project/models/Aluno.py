from project.models.Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.notas = []
    
    #metodos
    def calcular_media(self):
        if self.notas:
            return sum(self.notas)/len(self.notas)
        return 0

    def exibir_informações(self):
        media = self.calcular_media()
        print(f"Aluno: {self.nome}, Idade: {self.idade}, Media: {media:.2f}")