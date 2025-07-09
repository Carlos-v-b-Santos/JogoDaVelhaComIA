import numpy as np
import random
import pickle

# Parâmetros do Q-Learning
ALPHA = 0.1   # Taxa de aprendizado
GAMMA = 0.9   # Fator de desconto
EPSILON = 0.2  # Probabilidade de exploração (jogada aleatória)

class QLearningAgent:
    def __init__(self):
        self.q_table = {}  # Armazena os valores Q

    def get_state(self, matriz):
        """Converte o tabuleiro em uma tupla imutável para ser usada como chave no dicionário."""
        return tuple(map(tuple, matriz))

    def escolher_acao(self, matriz):
        """Escolhe a melhor ação ou faz uma jogada aleatória com base na política epsilon-greedy."""
        estado = self.get_state(matriz)
        acoes_disponiveis = self.acoes_possiveis(matriz)

        # Garante que o estado esteja na Q-table
        if estado not in self.q_table:
            self.q_table[estado] = {acao: 0 for acao in acoes_disponiveis}

        if random.uniform(0, 1) < EPSILON:
            return random.choice(acoes_disponiveis)  # Escolha aleatória (exploração)
        else:
            return max(self.q_table[estado], key=self.q_table[estado].get, default=random.choice(acoes_disponiveis))

    def acoes_possiveis(self, matriz):
        """Retorna todas as posições vazias como possíveis ações."""
        return [(i, j) for i in range(3) for j in range(3) if matriz[i][j] == 0]

    def atualizar_q_table(self, estado_atual, acao, recompensa, estado_futuro):
        """Atualiza a tabela Q com base na recompensa recebida e na equação de Bellman."""
        estado_atual = self.get_state(estado_atual)
        estado_futuro = self.get_state(estado_futuro)

        # Garante que os estados existam na Q-table
        if estado_atual not in self.q_table:
            self.q_table[estado_atual] = {acao: 0 for acao in self.acoes_possiveis(np.array(estado_atual))}

        if estado_futuro not in self.q_table:
            self.q_table[estado_futuro] = {acao: 0 for acao in self.acoes_possiveis(np.array(estado_futuro))}

        # Verifica se a ação existe no estado_atual, se não, a inicializa
        if acao not in self.q_table[estado_atual]:
            self.q_table[estado_atual][acao] = 0

        # Calcula o valor máximo futuro
        max_q_futuro = max(self.q_table[estado_futuro].values(), default=0)

        # Atualiza a Q-table com a equação de Bellman
        self.q_table[estado_atual][acao] = (1 - ALPHA) * self.q_table[estado_atual][acao] + ALPHA * (recompensa + GAMMA * max_q_futuro)

    def salvar_modelo(self, arquivo="q_table.pkl"):
        """Salva a tabela Q em um arquivo."""
        with open(arquivo, "wb") as f:
            pickle.dump(self.q_table, f)

    def carregar_modelo(self, arquivo="q_table.pkl"):
        """Carrega a tabela Q de um arquivo."""
        try:
            with open(arquivo, "rb") as f:
                self.q_table = pickle.load(f)
        except FileNotFoundError:
            self.q_table = {}
