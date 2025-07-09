import random
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Definição do modelo de Deep Q-Learning
modelo = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(9,)),  # Tabuleiro como entrada
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(9, activation='linear')  # Saída: Q-value para cada jogada possível
])

modelo.compile(optimizer='adam', loss='mse')

# Função para escolher uma jogada com exploração (ε-greedy)
def escolher_jogada(tabuleiro, epsilon=0.1):
    if random.uniform(0, 1) < epsilon:
        # Escolha aleatória para exploração
        return random.choice([i for i in range(9) if tabuleiro[i] == 0])
    else:
        # Escolha baseada no modelo treinado
        tabuleiro = np.array(tabuleiro).reshape(1, 9)
        q_values = modelo.predict(tabuleiro)
        melhor_jogada = np.argmax(q_values)
        return melhor_jogada
