from coordenador import Coordenador
from pyhop import hop
from problem.state import criar_estado_Inicial

class Coordenador_experiment(Coordenador):
    def __init__(self, replanejamento, ambiente):
        super().__init__(replanejamento)
        self.estado = criar_estado_Inicial()
        self.ambiente = ambiente
        self.replanejou = False
    def verificar_missao_completa(self):
        if self.estado.localizacao['robo'] == self.missao.goal:
            print('A missao foi bem sucedida!')
            return True
        else:
            print('A missao falhou')
            return False
    
    def mensagem(self, mensagem):
        self.monitorar_ambiente()
        if mensagem[0] == "Pedra_encontrada":
            self.estado.livre[mensagem[1]] = False
            if self.replanejamento:
                self.replanejar()
                self.replanejou = True
                return True
            else:
                return False
        return True
    def monitorar_ambiente(self):
        novo_ambiente = self.ambiente.monitorar_ambiente()
        self.estado.localizacao = novo_ambiente.localizacao



