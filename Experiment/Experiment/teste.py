from  coordenador_experiment import Coordenador_experiment
from robo_experiment import Robo_experiment
from ambiente import  Ambiente
from missao import Missao
from pyhop import hop
from pyhop import helpers
from domain import actions
from domain import methods

ambiente = Ambiente(100)

coord = Coordenador_experiment(False, ambiente)
robo = Robo_experiment(ambiente)
missao1 = Missao('viajar', 'Base')
coord.executar_missao(missao1, robo)