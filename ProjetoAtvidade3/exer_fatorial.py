"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-01
Nome: Maria Paula Henriques Prandt
"""

print('Exercício 1 - função cálculo de fatorial')

def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')