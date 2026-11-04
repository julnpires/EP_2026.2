def posiciona_frota(frota):
    grid = []
    for i in range(10):
        grid.append([0] * 10)
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                grid[posicao[0]][posicao[1]] = 1
    return grid