"""
Algoritmos-em-bioinformatica
atividade-03-exercicio-03
Nome: Maria Paula Henriques Prandt
"""


def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False


print('Exercício 3 - Programa para identificar a multiplicidade entre dois números:')
print(70*'-')

#Entradas
num1 = int(input('Entre com o primeiro parâmetro: '))
num2 = int(input('Entre com o segundo parâmetro: '))

#Calculo
r = multiplo(num1, num2)

#Saidas
if r:
    print(f'{num1} é multiplo de {num2}')
else:
    print(f'{num1} não é multiplo de {num2}')
