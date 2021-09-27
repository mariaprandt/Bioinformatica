"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-06
Nome: Maria Paula Henriques Prandt
"""

import numpy as np
import random

print('Exercício 6 - Indices Pares')

#Escolhendo uma dimensão aleatória para a matriz
dim = random.randint(1, 20)

print(f'A dimensão aleatória da matriz é de: (1x{dim})')

#Preenchendo a matriz com números aleatórios
a = np.random.randint(0, 10, dim)

#Selecionando os valores dos índices pares
b = a[::2]

#Exibindo
print(f'A matriz aleatória é: {a}\nOs valores dos índices pares são: {b}')
print('PS: os índices começam a contar a partir do 0 (zero)')
