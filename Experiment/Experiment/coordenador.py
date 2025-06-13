
from pyhop import hop
class Coordenador:
    def __init__(self, replanejamento):
        self.estado = None
        self.missao = None
        self.robo = None
        self.replanejamento = replanejamento


    def executar_missao(self, missao, robo):
        self.missao = missao
        self.robo = robo
        print("planejando")
        plano = self.planejar()
        robo.receber_subplano(plano, self)
        self.verificar_missao_completa()


    def planejar(self):
        return hop.plan(self.estado, [(self.missao.task, self.missao.goal)], hop.get_operators(), hop.get_methods(), verbose=0)


    def monitorar_ambiente(self):
        raise NotImplementedError("This method should be implemented by the subclass")

    def mensagem(self, mensagem):
        raise NotImplementedError("This method should be implemented by the subclass")

    def replanejar(self):
            print('O coordenador esta replanejando!')
            plano = self.planejar()
            self.robo.receber_subplano(plano, self)
    
        
    def verificar_missao_completa():
        raise NotImplementedError("This method should be implemented by the subclass")