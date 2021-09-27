"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-02
Nome: Maria Paula Henriques Prandt
"""


def maxnum(*valores):
    max = 0
    print(f'Tomando o conjunto [ ', end='')
    for num in valores:
        print(f'{num}  ', end='')
        if num > max:
            max = num
    print(']')
    return max


print('Exercício 2- Programa para calcular valor máximo\n')

m = maxnum(1, 2, 3, 5, 8)
print(f'O maior numero é: {m}')
m2 = maxnum(1, 4, 33, 55, 0)
print(f'O maior numero é: {m2}')
