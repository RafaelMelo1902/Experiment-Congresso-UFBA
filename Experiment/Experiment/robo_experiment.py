from robo import Robo
import random
from ambiente import Ambiente

class Robo_experiment(Robo):
    def __init__(self, ambiente):
        super().__init__()
        self.ambiente = ambiente



    def executar_tarefa(self, acao):
      print('O robo está tentando executar', acao)
      return self.ambiente.executar_tarefa(acao)

      
