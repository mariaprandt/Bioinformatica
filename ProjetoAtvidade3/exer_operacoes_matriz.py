"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-07
Nome: Maria Paula Henriques Prandt
"""
import numpy as np

print('Exercício 7 - Operações com arrays')
matrix = np.random.randint(-10, 65, (4, 5))
print(f'Matriz:\n{matrix}\n')
#a)
print(f'A) Valores absolutos:\n {np.absolute(matrix)}\n')
#b)
print(f'B) Seno dos vlores da primeira linha: \n {np.sin(matrix[0,:])}\n')
#c)
print(f'C) Valores máximos das colunas: \n{matrix.max(0)}\n')
#d)
print(f'D) Soma dos elementos de cada coluna:\n {matrix.sum(0)}\n')
#e)
print(f'E) Soma dos elementos de cada linha: \n {matrix.sum(1)}\n')
#f)
print(f'F) Produto dos elementos de cada coluna: \n{matrix.prod(0)}')
