"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-02
Nome: Maria Paula Henriques Prandt

"""
# Calculando uma poupança de Juros Simples

d = float(input('Digite o valor do depósito inicial da poupança: '))
t = float(input('Digite qual a taxa de juros ao mês: '))

# No sistema de juros simples, o juros é calculado apenas em cima do valor inicial

j = d * (t / 100)

# Calculando os juros ao longo de cada mês (durante 24 meses)
for c in range(1, 25):
    d += j
    print(f'No mês {c} o valor obtido será de R${d:.2f}')

print('\nAo fim dos 24 meses, o valor total de juros obtidos será de R${:.2f}'.format(j*24))
