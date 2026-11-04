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


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        l = posicao[0]
        c = posicao[1]
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False
        for nome_navio in frota:
            for navio in frota[nome_navio]:
                for ocupada in navio:
                    if ocupada == posicao:
                        return False
    return True
