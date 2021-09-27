"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-03
Nome: Maria Paula Henriques Prandt

O exercício pede para que seja feito uma sequência numérica organizada de maneira crescente
"""

# Exercício feito usando lista
linha = list()

for c in range(1,6):
    for i in range (1,c+1):
        linha.append(c*i)
    print(f'{linha}')
    linha.clear()

print('\n')

# Exercício feito usando apenas o FOR
for j in range(1,6):
    for b in range (1,j+1):
        print(f'{j*b}', end=' ')
    print('')