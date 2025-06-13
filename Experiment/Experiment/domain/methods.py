from pyhop import hop

#--------MÉTODOS
def metodo_viajar(estado, destino):
    atual = estado.localizacao['robo']

    if atual == destino:
        return []


    for prox in estado.conexoes[atual]:
        if estado.livre[prox]:
            return [('mover_robo', prox), ('viajar', destino)]
        else:
            return [('retirar_pedra', prox), ('viajar', destino)]
    return False


hop.declare_methods('viajar', metodo_viajar)