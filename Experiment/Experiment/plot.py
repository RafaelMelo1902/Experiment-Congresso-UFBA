import matplotlib.pyplot as plt
import random
import numpy as np
import time
from  coordenador_experiment import Coordenador_experiment
from robo_experiment import Robo_experiment
from ambiente import  Ambiente
from missao import Missao
from pyhop import hop
from pyhop import helpers
from domain import actions
from domain import methods
import os
import json

# Cores para os resultados
CORES = {
    'sucesso_direto': '#1f77b4',  # azul
    'falha': '#d62728',           # vermelho
    'recuperado': '#ff7f0e'       # laranja
}

os.makedirs("graficos", exist_ok=True)
os.makedirs("dados", exist_ok=True)
def rodar_experimento(coordenador_classe, taxa_pedra):
    print(f"--------- EXPERIMENTO COM {taxa_pedra} ------------")
    resultados = []
    duracoes = []
    for _ in range(30):
        ambiente = Ambiente(taxa_pedra)
        coord = Coordenador_experiment(coordenador_classe, ambiente)
        robo = Robo_experiment(ambiente)
        missao1 = Missao('viajar', 'Base')
        inicio = time.perf_counter()
        coord.executar_missao(missao1, robo)
        fim = time.perf_counter()
        duracao = fim - inicio
        duracoes.append(duracao)

        if coord.estado.localizacao['robo'] == missao1.goal:
            if coord.replanejou:
                resultados.append('recuperado')  # sucesso com replanejamento
            else:
                resultados.append('sucesso_direto')  # sucesso direto
        else:
            resultados.append('falha')
    salvar_resultados_em_arquivo(f"{coordenador_classe}_{taxa_pedra}", resultados, duracoes)
    return resultados, duracoes

def salvar_resultados_em_arquivo(nome_arquivo, resultados, duracoes):
    with open(f"dados/{nome_arquivo}_resultados.json", "w") as f:
        json.dump(resultados, f)
    with open(f"dados/{nome_arquivo}_duracoes.json", "w") as f:
        json.dump(duracoes, f)

def carregar_resultados_de_arquivo(nome_arquivo):
    with open(f"{nome_arquivo}_resultados.json", "r") as f:
        resultados = json.load(f)
    with open(f"{nome_arquivo}_duracoes.json", "r") as f:
        duracoes = json.load(f)
    return resultados, duracoes
def plot_resultados(todos_resultados, titulo):
      
      os.makedirs("graficos", exist_ok=True)
      cores = [CORES['sucesso_direto'], CORES['recuperado'], CORES['falha']]
      labels = ['Sucesso Direto', 'Recuperado', 'Falha']

      data = []
      for linha in todos_resultados:
          azul = linha.count('sucesso_direto')
          laranja = linha.count('recuperado')
          vermelho = linha.count('falha')
          data.append([azul, laranja, vermelho])

      data = list(reversed(data))  # para alinhar de cima para baixo como a imagem

      fig, ax = plt.subplots()
      left = [0]*len(data)
      for i in range(3):
          valores = [linha[i] for linha in data]
          ax.barh(range(len(data)), valores, left=left, color=cores[i], label=labels[i])
          left = [left[j] + valores[j] for j in range(len(data))]

      ax.set_yticks(range(len(taxas)))
      ax.set_yticklabels([f'{int(t*100)}%' for t in reversed(taxas)])
      ax.set_xlabel('Execuções')
      ax.set_title(titulo)
      ax.set_xlim(0, 30)
      ax.legend()
      plt.tight_layout()
      plt.savefig(f"graficos/{titulo}.png")
      plt.show()

def plot_tempos(duracoes_por_taxa, titulo):
    plt.figure(figsize=(9, 4))

    for i, duracoes in enumerate(duracoes_por_taxa):
        # Converte as durações para milissegundos
        duracoes_ms = [d * 1000 for d in duracoes]
        plt.plot(range(1, 31), duracoes_ms, marker='', linestyle='-', linewidth=2,
                 label=f'{int(taxas[i]*100)}%')

    plt.title(f'Tempo de Execução {titulo.lower()} (ms)')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (ms)')

    # Zoom no eixo Y: calcula o menor e maior valor e define uma margem pequena
    min_tempo = min(min(d) for d in duracoes_por_taxa) * 1000  # Converter para milissegundos
    max_tempo = max(max(d) for d in duracoes_por_taxa) * 1000  # Converter para milissegundos
    margem = (max_tempo - min_tempo) * 0.2  # margem de 20% da diferença

    plt.ylim(min_tempo - margem, max_tempo + margem)

    # Definir o eixo X para exibir de 1 a 30
    plt.xticks(range(1, 31))  # Aqui você define explicitamente o eixo X

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Taxa de Obstáculos')
    plt.tight_layout()
    plt.savefig(f"graficos/{titulo}.png")
    plt.show()


taxas = [0, 0.3, 0.5, 0.7,1]
# Sem replanejamento
print('SEM REPLAN')
resultados_sem_e_duracoes = [rodar_experimento(False, taxa) for taxa in taxas]
resultados_sem = [res[0] for res in resultados_sem_e_duracoes]  # Separa os resultados
duracoes_sem = [res[1] for res in resultados_sem_e_duracoes]  # Separa as durações
plot_resultados(resultados_sem, 'Sem Replanejamento')
plot_tempos(duracoes_sem, 'Duração sem replan')


#Com replanejamento
print("COM REPLAN")
resultados_com_e_duracoes = [rodar_experimento(True, taxa) for taxa in taxas]
resultados_com = [res[0] for res in resultados_com_e_duracoes]
duracoes_com = [res[1] for res in resultados_com_e_duracoes]
plot_resultados(resultados_com, 'Com Replanejamento')
plot_tempos(duracoes_com, 'Duração com replan')