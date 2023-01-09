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
    return tabuleiro_aux

def verifica_se_nasce(linha, coluna, tabuleiro, tabuleiro_aux):
    if linha - 1 < 0:
        tabuleiro_aux = valida_nasce(linha+1, coluna, tabuleiro, tabuleiro_aux)
        if coluna + 1 < 4:
            tabuleiro_aux = valida_nasce(linha, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna+1, tabuleiro, tabuleiro_aux)
        if coluna - 1 >= 0:
            tabuleiro_aux = valida_nasce(linha, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna-1, tabuleiro, tabuleiro_aux)
    elif coluna + 1 > 4:
        tabuleiro_aux = valida_nasce(linha-1, coluna, tabuleiro, tabuleiro_aux)
        if coluna - 1 >= 0:
            tabuleiro_aux = valida_nasce(linha, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha-1, coluna-1, tabuleiro, tabuleiro_aux)
        if coluna + 1 < 9:
            tabuleiro_aux = valida_nasce(linha-1, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha, coluna+1, tabuleiro, tabuleiro_aux)
    else:
        if coluna - 1 < 0:
            tabuleiro_aux = valida_nasce(linha-1, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha-1, coluna, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna, tabuleiro, tabuleiro_aux)
        elif coluna + 1 > 4:
            tabuleiro_aux = valida_nasce(linha-1, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha-1, coluna, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1, coluna, tabuleiro, tabuleiro_aux)
        else:
            tabuleiro_aux = valida_nasce(linha-1, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha-1, coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha-1, coluna, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1 , coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1 , coluna-1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha+1 , coluna, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha, coluna+1, tabuleiro, tabuleiro_aux)
            tabuleiro_aux = valida_nasce(linha, coluna-1, tabuleiro, tabuleiro_aux)
    return tabuleiro_aux


def game_of_life(jogando, tabuleiro_anterior=[]):
    clear()
    if not jogando:
        tabuleiro = [
            '0000X00000',
            '0000X00000',
            '0000X00000',
            '0000000000',
            '0000000000',]
    else:
        tabuleiro = tabuleiro_anterior

    tabuleiro_aux = tabuleiro.copy()

    coluna = 0
    linha = 0
    for x in tabuleiro:
        for y in x:
            if y == 'X':
                vizinhos = conta_vizinho(linha, coluna, tabuleiro)
                if vizinhos <= 1 or vizinhos >=4:
                    tabuleiro_aux = mata_celula(linha, coluna, tabuleiro_aux)
                tabuleiro_aux = verifica_se_nasce(linha, coluna, tabuleiro, tabuleiro_aux)
            coluna += 1
        coluna = 0
        linha += 1
    
    tabuleiro = tabuleiro_aux
    for x in tabuleiro:
        print(x)
    time.sleep(2)
    clear()
    game_of_life(True, tabuleiro)


game_of_life(False,[])