import random

# Definição dos símbolos
VAZIO = 0
X = -1
O = 1

# Mapeamento das casas (1 a 9)
posicoes = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

# Função para verificar o vencedor
def verificar_vencedor(matriz):
    for i in range(3):
        if abs(sum(matriz[i])) == 3:  # Linhas
            return matriz[i][0]
        if abs(sum([matriz[j][i] for j in range(3)])) == 3:  # Colunas
            return matriz[0][i]

    # Diagonais
    if abs(matriz[0][0] + matriz[1][1] + matriz[2][2]) == 3:
        return matriz[1][1]
    if abs(matriz[0][2] + matriz[1][1] + matriz[2][0]) == 3:
        return matriz[1][1]

    return 0  # Nenhum vencedor ainda

# Função para verificar se o jogo empatou
def jogo_empatado(matriz):
    return all(matriz[i][j] != VAZIO for i in range(3) for j in range(3)) and verificar_vencedor(matriz) == 0

# Função Minimax
def minimax(matriz, profundidade, maximizar):
    vencedor = verificar_vencedor(matriz)
    
    if vencedor == O:  # IA venceu
        return 10 - profundidade
    if vencedor == X:  # Jogador venceu
        return profundidade - 10
    if jogo_empatado(matriz):  # Empate
        return 0

    if maximizar:
        melhor_valor = -float("inf")
        for casa, (i, j) in posicoes.items():
            if matriz[i][j] == VAZIO:
                matriz[i][j] = O
                valor = minimax(matriz, profundidade + 1, False)
                matriz[i][j] = VAZIO
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for casa, (i, j) in posicoes.items():
            if matriz[i][j] == VAZIO:
                matriz[i][j] = X
                valor = minimax(matriz, profundidade + 1, True)
                matriz[i][j] = VAZIO
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para a IA escolher a melhor jogada
def melhor_jogada_ia(matriz):
    melhor_valor = -float("inf")
    melhor_movimento = None

    for casa, (i, j) in posicoes.items():
        if matriz[i][j] == VAZIO:
            matriz[i][j] = O
            valor = minimax(matriz, 0, False)
            matriz[i][j] = VAZIO
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_movimento = casa

    return melhor_movimento