from pyhop import hop

def criar_estado_Inicial():
    estado = hop.State('estado1')
    estado.localizacao = {'robo': 'C'}
    estado.conexoes = {
        'Base': ['A'],
        'A': ['Base', 'B'],
        'B': ['A', 'C'],
        'C': ['B']
    }
    estado.livre = {
        'Base': True,
        'A': True,
        'B': True,
        'C': True,
    }
    return estado


