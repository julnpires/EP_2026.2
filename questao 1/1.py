def define_posicoes (linha, coluna, orientacao, tam):
    posi = []
    for i in range(tam):
        if orientacao == 'vertical':
            posi.append([linha + i, coluna])
        else: posi.append([linha, coluna + i])
    return posi