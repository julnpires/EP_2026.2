def define_posicoes(linha, coluna, orientacao, tam):
    posi = []
    for i in range(tam):
        if orientacao == 'vertical':
            posi.append([linha + i, coluna])
        else:
            posi.append([linha, coluna + i])
    return posi

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(navio)
    return frota