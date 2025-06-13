import json
import matplotlib.pyplot as plt
import os

CORES = {
    'sucesso_direto': '#1f77b4',
    'falha': '#d62728',
    'recuperado': '#ff7f0e'
}

taxas = [0, 0.3, 0.5, 0.7, 1]

os.makedirs("graficos2", exist_ok=True)
def carregar_resultados(tipo_replan):
    resultados = []
    duracoes = []
    for taxa in taxas:
        nome = f"dados/{tipo_replan}_{taxa}"
        with open(f"{nome}_resultados.json") as f:
            resultados.append(json.load(f))
        with open(f"{nome}_duracoes.json") as f:
            duracoes.append(json.load(f))
    return resultados, duracoes

def plot_resultados(todos_resultados, titulo, nome_arquivo):
    cores = [CORES['sucesso_direto'], CORES['recuperado'], CORES['falha']]
    labels = ['Sucesso Direto', 'Recuperado', 'Falha']

    data = []
    for linha in todos_resultados:
        azul = linha.count('sucesso_direto')
        laranja = linha.count('recuperado')
        vermelho = linha.count('falha')
        data.append([azul, laranja, vermelho])

    data = list(reversed(data))

    fig, ax = plt.subplots()
    left = [0] * len(data)
    for i in range(3):
        valores = [linha[i] for linha in data]
        ax.barh(range(len(data)), valores, left=left, color=cores[i], label=labels[i])
        left = [left[j] + valores[j] for j in range(len(data))]

    ax.set_yticks(range(len(taxas)))
    ax.set_yticklabels([f'{int(t * 100)}%' for t in reversed(taxas)])
    ax.set_xlabel('Execuções')
    ax.set_title(titulo)
    ax.set_xlim(0, 30)
    ax.legend()
    plt.tight_layout()
    plt.savefig(f"graficos2/{nome_arquivo}.png")
    plt.close()

def plot_tempos(duracoes_por_taxa, titulo, nome_arquivo):
    plt.figure(figsize=(9, 4))

    for i, duracoes in enumerate(duracoes_por_taxa):
        duracoes_ms = [d * 1000 for d in duracoes]
        plt.plot(range(1, 31), duracoes_ms, marker='', linestyle='-', linewidth=2,
                 label=f'{int(taxas[i] * 100)}%')

    plt.title(f'Tempo de Execução {titulo.lower()} (ms)')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (ms)')

    min_tempo = min(min(d) for d in duracoes_por_taxa) * 1000
    max_tempo = max(max(d) for d in duracoes_por_taxa) * 1000
    margem = (max_tempo - min_tempo) * 0.2

    plt.ylim(min_tempo - margem, max_tempo + margem)
    plt.xticks(range(1, 31))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Taxa de Obstáculos')
    plt.tight_layout()
    plt.savefig(f"graficos2/{nome_arquivo}.png")
    plt.close()


resultados_sem, duracoes_sem = carregar_resultados('False')
plot_resultados(resultados_sem, 'Sem Replanejamento', 'sem_replan_resultados')
plot_tempos(duracoes_sem, 'Sem Replanejamento', 'sem_replan_tempos')

resultados_com, duracoes_com = carregar_resultados('True')
plot_resultados(resultados_com, 'Com Replanejamento', 'com_replan_resultados')
plot_tempos(duracoes_com, 'Com Replanejamento', 'com_replan_tempos')

