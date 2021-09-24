"""
Algoritmos-em-bioinformatica
atividade-01-exercicio-04
Nome: Maria Paula Henriques Prandt

O exercício pede que seja calculado os dias de vida que o fumo pode tirar de uma pessoa de acordo
com as condições apresentadas em sala.
"""

c=int(input('Quantos cigarros são fumados por dia?'))
d=float(input('A quantos anos você fuma?'))
total= (d*365)*c
dias= ((total*10)/60)//24
print('O fumante perderá aproximadamente {:.1f} dias de vida'.format(dias))
