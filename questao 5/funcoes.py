def afundados(frota, tabuleiro):
    contador = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            afundou = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundou = False
            if afundou:
                contador += 1
    return contador