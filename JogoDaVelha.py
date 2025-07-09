import pygame
import random
import IA
import minimax

# Inicializando o Pygame antes de definir a fonte
pygame.init()

# Configuração da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
TAMANHO_CELULA = LARGURA_TELA // 3
pygame.init()
FONTE = pygame.font.Font(None, 80)

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

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

# Função para desenhar o tabuleiro
def desenhar_jogo(tela, matriz):
    tela.fill(BRANCO)

    # Desenhando as linhas do tabuleiro
    for i in range(1, 3):
        pygame.draw.line(tela, PRETO, (i * TAMANHO_CELULA, 0), (i * TAMANHO_CELULA, ALTURA_TELA), 5)
        pygame.draw.line(tela, PRETO, (0, i * TAMANHO_CELULA), (LARGURA_TELA, i * TAMANHO_CELULA), 5)

    # Desenhando os X e O
    for casa, (linha, coluna) in posicoes.items():
        centro_x = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2
        centro_y = linha * TAMANHO_CELULA + TAMANHO_CELULA // 2

        if matriz[linha][coluna] == X:
            pygame.draw.line(tela, VERMELHO, (centro_x - 50, centro_y - 50), (centro_x + 50, centro_y + 50), 10)
            pygame.draw.line(tela, VERMELHO, (centro_x + 50, centro_y - 50), (centro_x - 50, centro_y + 50), 10)
        elif matriz[linha][coluna] == O:
            pygame.draw.circle(tela, AZUL, (centro_x, centro_y), 50, 10)

    pygame.display.update()

# Função para verificar se houve vencedor
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
    return all(matriz[i][j] != VAZIO for i in range(3) for j in range(3))

# Função para jogar a jogada da IA
def jogar_ia(matriz):
    jogada_ia = minimax.melhor_jogada_ia(matriz)
    
    #jogada_ia = IA.escolher_jogada(matriz)

    return jogada_ia;


    #jogadas_possiveis = [casa for casa, (i, j) in posicoes.items() if matriz[i][j] == VAZIO]
    #return random.choice(jogadas_possiveis) if jogadas_possiveis else None

# Função principal do jogo
def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Jogo da Velha")

    matriz = [[VAZIO for _ in range(3)] for _ in range(3)]
    turno = X  # Começa com X
    jogando = True
    jogador_ia = O  # A IA joga com O

    while jogando:
        desenhar_jogo(tela, matriz)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

            if evento.type == pygame.MOUSEBUTTONDOWN and turno == X:
                x, y = evento.pos
                coluna = x // TAMANHO_CELULA
                linha = y // TAMANHO_CELULA

                # Obtendo a casa correspondente (1 a 9)
                for casa, (i, j) in posicoes.items():
                    if (i, j) == (linha, coluna) and matriz[i][j] == VAZIO:
                        matriz[i][j] = X
                        if verificar_vencedor(matriz):
                            desenhar_jogo(tela, matriz)
                            print("Você venceu!")
                            jogando = False
                        elif jogo_empatado(matriz):
                            desenhar_jogo(tela, matriz)
                            print("Empate!")
                            jogando = False
                        turno = O
                        break

        if turno == O and jogando:  # Vez da IA
            casa_ia = jogar_ia(matriz)
            if casa_ia:
                i, j = posicoes[casa_ia]
                matriz[i][j] = O
                if verificar_vencedor(matriz):
                    desenhar_jogo(tela, matriz)
                    print("A IA venceu!")
                    jogando = False
                elif jogo_empatado(matriz):
                    desenhar_jogo(tela, matriz)
                    print("Empate!")
                    jogando = False
                turno = X

    pygame.quit()

if __name__ == "__main__":
    main()