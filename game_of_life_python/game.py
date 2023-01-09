import time
import os
clear = lambda: os.system('clear')

def conta_vizinho(linha, coluna, tabuleiro):
        vizinhos = 0
        if linha - 1 < 0:
            if tabuleiro[linha][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha][coluna - 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha + 1][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha + 1][coluna - 1] == 'X':
                vizinhos += 1  
            if tabuleiro[linha + 1][coluna] == 'X':
                vizinhos += 1                    
        elif linha + 1 > 4:
            if tabuleiro[linha][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha][coluna - 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha - 1][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha - 1][coluna - 1] == 'X':
                vizinhos += 1  
            if tabuleiro[linha - 1][coluna] == 'X':
                vizinhos += 1
        else:
            if tabuleiro[linha][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha][coluna - 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha - 1][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha - 1][coluna - 1] == 'X':
                vizinhos += 1  
            if tabuleiro[linha - 1][coluna] == 'X':
                vizinhos += 1
            if tabuleiro[linha + 1][coluna + 1] == 'X':
                vizinhos += 1
            if tabuleiro[linha + 1][coluna - 1] == 'X':
                vizinhos += 1  
            if tabuleiro[linha + 1][coluna] == 'X':
                vizinhos += 1
        return vizinhos

def mata_celula(linha, coluna, tabuleiro):
    lista_aux = []
    linha_aux = ''
    for celula in tabuleiro[linha]:
        lista_aux.append(celula)
    lista_aux[coluna] = '0'
    for x in lista_aux:
        linha_aux += x
    tabuleiro[linha] = linha_aux
    return tabuleiro

def cria_celula(linha, coluna, tabuleiro):
    lista_aux = []
    linha_aux = ''
    for celula in tabuleiro[linha]:
        lista_aux.append(celula)
    lista_aux[coluna] = 'X'
    for x in lista_aux:
        linha_aux += x
    tabuleiro[linha] = linha_aux
    return tabuleiro

def valida_nasce(linha, coluna, tabuleiro, tabuleiro_aux):
    if not tabuleiro[linha][coluna] == 'X':
        vizinhos = conta_vizinho(linha, coluna, tabuleiro)
        if vizinhos == 3:
            tabuleiro_aux = cria_celula(linha, coluna, tabuleiro_aux)

def game_of_life():

    tabuleiro = [
        '0000X00000',
        '0000X00000',
        '0000X00000',
        '0000000000',
        '0000000000',]

    tabuleiro_aux = [
        '0000X00000',
        '0000X00000',
        '0000X00000',
        '0000000000',
        '0000000000',]

    coluna = 0
    linha = 0
    for x in tabuleiro:
        for y in x:
            if y == 'X':
                vizinhos = conta_vizinho(linha, coluna, tabuleiro)
                if vizinhos <= 1 or vizinhos >=4:
                    tabuleiro_aux = mata_celula(linha, coluna, tabuleiro_aux)
                if vizinhos == 8:
                    continue
                elif linha - 1 < 0:
                    if coluna + 1 < 4:
                        if not tabuleiro[linha][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha, coluna + 1, tabuleiro_aux)
                        if not tabuleiro[linha+1][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha+1, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha + 1, coluna + 1, tabuleiro_aux)
                    if not tabuleiro[linha+1][coluna] == 'X':
                            vizinhos = conta_vizinho(linha+1, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha + 1, coluna, tabuleiro_aux)
                    if coluna - 1 >= 0:
                        if not tabuleiro[linha][coluna-1] == 'X':
                            vizinhos = conta_vizinho(linha, coluna-1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha, coluna - 1, tabuleiro_aux)
                        if not tabuleiro[linha+1][coluna-1] == 'X':
                            vizinhos = conta_vizinho(linha+1, coluna-1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha + 1, coluna - 1, tabuleiro_aux)
                elif linha + 1 > 4:
                    if linha -1 >= 0:
                        if not tabuleiro[linha][coluna-1] == 'X':
                            vizinhos = conta_vizinho(linha, coluna-1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha, coluna - 1, tabuleiro_aux)
                        if not tabuleiro[linha-1][coluna-1] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna-1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha -1, coluna - 1, tabuleiro_aux)
                    if not tabuleiro[linha-1][coluna] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna, tabuleiro_aux)
                    if linha + 1 < 9:
                        if not tabuleiro[linha-1][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna + 1, tabuleiro_aux)
                        if not tabuleiro[linha][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha, coluna + 1, tabuleiro_aux)
                else:
                    if linha - 1 < 0:
                        if not tabuleiro[linha-1][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna + 1, tabuleiro_aux)
                        if not tabuleiro[linha-1][coluna] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna, tabuleiro_aux)
                        if not tabuleiro[linha][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha, coluna + 1, tabuleiro_aux)
                        if not tabuleiro[linha+1][coluna+1] == 'X':
                            vizinhos = conta_vizinho(linha+1, coluna+1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha + 1, coluna + 1, tabuleiro_aux)
                        if not tabuleiro[linha+1][coluna] == 'X':
                            vizinhos = conta_vizinho(linha+1, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha + 1, coluna, tabuleiro_aux)
                    elif linha + 1 > 9:
                        if not tabuleiro[linha-1][coluna-1] == 'X':
                            vizinhos = conta_vizinho(linha-1, coluna-1, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna - 1, tabuleiro_aux)
                        if not tabuleiro[linha-1][coluna] == 'X':
                            vizinhos = conta_vizinho(linha, coluna, tabuleiro)
                            if vizinhos == 3:
                                tabuleiro_aux = cria_celula(linha - 1, coluna, tabuleiro_aux)
                        

                    
                                

            coluna += 1
        coluna = 0
        linha += 1


game_of_life()