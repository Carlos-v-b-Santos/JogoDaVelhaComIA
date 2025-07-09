import numpy as np
from q_learning import QLearningAgent
from jogo import verificar_vencedor, jogo_empatado, fazer_jogada

def main():
    agente = QLearningAgent()
    agente.carregar_modelo()
    
    matriz = np.zeros((3, 3), dtype=int)
    turno = -1  # IA começa
    
    while True:
        print(matriz)

        if turno == 1:  # Jogador
            acao = int(input("Escolha uma posição (1-9): ")) - 1
            linha, coluna = divmod(acao, 3)
            if matriz[linha, coluna] == 0:
                matriz[linha, coluna] = turno
            else:
                print("Jogada inválida! Tente novamente.")
                continue
        else:  # IA
            acao = agente.escolher_acao(matriz)
            matriz = fazer_jogada(matriz, acao, turno)

        if verificar_vencedor(matriz) == turno:
            print(matriz)
            print("Vitória do", "IA" if turno == -1 else "Jogador")
            break
        elif jogo_empatado(matriz):
            print(matriz)
            print("Empate!")
            break

        turno *= -1

if __name__ == "__main__":
    main()