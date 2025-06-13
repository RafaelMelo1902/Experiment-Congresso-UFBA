
from pyhop import hop
def mover_robo(estado, destino):
    if destino in estado.conexoes[estado.localizacao['robo']]:
        estado.localizacao['robo'] = destino
        return estado
    return False

hop.declare_operators(mover_robo)

def retirar_pedra(estado, local):
    if not estado.livre[local]:
        estado.livre[local] = True
        return estado
    return False


hop.declare_operators(retirar_pedra)
