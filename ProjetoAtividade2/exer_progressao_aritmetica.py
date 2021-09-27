"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-01
Nome: Maria Paula Henriques Prandt

"""

print('Calculando uma progressão aritmética: \n')
n = int(input('Digite o primeiro número da PA: '))
r: int = int(input('Digite a razão da PA: '))
decimo= n + (10) * r

# Note que o 'decimo' representa, na vdd o 11º número da PA, mas foi proposital por conta das condições do laço FOR

for c in range(n, decimo, r):
    print(f'{c}', end=" | ")


