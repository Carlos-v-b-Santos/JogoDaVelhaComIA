import numpy as np

def verificar_vencedor(matriz):
    """Verifica se há um vencedor no jogo."""
    for i in range(3):
        if abs(sum(matriz[i])) == 3:
            return matriz[i][0]
        if abs(sum(matriz[:, i])) == 3:
            return matriz[0][i]

    if abs(matriz[0, 0] + matriz[1, 1] + matriz[2, 2]) == 3:
        return matriz[1, 1]
    if abs(matriz[0, 2] + matriz[1, 1] + matriz[2, 0]) == 3:
        return matriz[1, 1]

    return 0  # Nenhum vencedor

def jogo_empatado(matriz):
    """Verifica se o jogo empatou."""
    return np.all(matriz != 0) and verificar_vencedor(matriz) == 0

def fazer_jogada(matriz, acao, jogador):
    """Executa a jogada e retorna o novo estado do tabuleiro."""
    matriz[acao] = jogador
    return matriz