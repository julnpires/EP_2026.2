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


navios = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1],
}

frota = {}

for nome in navios:
    quantidade = navios[nome][0]
    tamanho = navios[nome][1]

    for i in range(quantidade):
        valida = False
        while not valida:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}.")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = 'horizontal'
            else:
                opcao = int(input('[1] Vertical [2] Horizontal >'))
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print("Esta posição não está válida!")
print(frota)
