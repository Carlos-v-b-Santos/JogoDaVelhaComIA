from q_learning import QLearningAgent
from jogo import verificar_vencedor, jogo_empatado, fazer_jogada
import numpy as np
import minimax

EPISODIOS = 50  # Número de partidas para treinamento

agente = QLearningAgent()

for episodio in range(EPISODIOS):
    matriz = np.zeros((3, 3), dtype=int)
    turno = -1  # IA começa jogando
    
    while True:
        estado_atual = matriz.copy()
        
        if(turno == 1):#jogada do minimax
            jogada_ia = minimax.melhor_jogada_ia(matriz)
            linha, coluna = divmod(jogada_ia-1, 3)
            matriz[linha, coluna] = turno
        else:#jogada do deep learning
            acao = agente.escolher_acao(matriz)
            matriz = fazer_jogada(matriz, acao, turno)
        
        
        

        if verificar_vencedor(matriz) == -1:
            recompensa = 1  # Vitória
            agente.atualizar_q_table(estado_atual, acao, recompensa, matriz)
            break
        elif verificar_vencedor(matriz) == 1:
            recompensa = -1  # Derrota
            agente.atualizar_q_table(estado_atual, acao, recompensa, matriz)
            break
        elif jogo_empatado(matriz):
            recompensa = 0  # Empate
            agente.atualizar_q_table(estado_atual, acao, recompensa, matriz)
            break
        else:
            recompensa = +0.1  # Recompensa neutra para continuar jogando
            

        agente.atualizar_q_table(estado_atual, acao, recompensa, matriz)
        turno *= -1  # Alterna jogador

agente.salvar_modelo()
print("Treinamento concluído e modelo salvo!")