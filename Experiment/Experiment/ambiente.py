from pyhop import hop
import random
from problem.state import criar_estado_Inicial
class Ambiente:
    def __init__(self, erro):
        self.ambiente = criar_estado_Inicial()
        self.chance_pedra = erro
        if random.random() < self.chance_pedra:
            self.ambiente.livre['A'] = False
            print(f'[Simulação] Pedra foi colocada em A no início da execução.')

    

    def executar_tarefa(self, acao):
        if acao[0] == 'mover_robo':
          # Verifica se o destino está livre
          if not self.ambiente.livre[acao[1]]:
                print(f'O robo encontrou uma pedra em {acao[1]}!')
                print(f'O robo não executou a ação {acao}!')
                return ("Pedra_encontrada", acao[1])
          else:
              self.ambiente.localizacao = {'robo': acao[1]}

        elif acao[0] == 'retirar_pedra':
          self.ambiente.livre[acao[1]] = True

        print(f'O robo executou a ação {acao[0]} {acao[1]} com sucesso!')
        return (acao)
    
    def monitorar_ambiente(self):
        return self.ambiente