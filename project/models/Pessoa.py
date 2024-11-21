from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def exibir_informações(self):
        pass
        