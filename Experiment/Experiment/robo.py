

class Robo:
    def __init__(self):
        self.coordenador = None
        self.subplano = []

    def receber_subplano(self, plano, coordenador):
      self.subplano = plano
      self.coordenador = coordenador
      self.executar_plano()

    def executar_plano(self):
        while self.subplano:
            acao = self.subplano.pop(0)
            executou = self.executar_tarefa(acao)
            continuar = self.coordenador.mensagem(executou)
            if not continuar:
                 return False
        return True
    
    def executar_tarefa(self, action):
      raise NotImplementedError("This method should be implemented by the subclass")
