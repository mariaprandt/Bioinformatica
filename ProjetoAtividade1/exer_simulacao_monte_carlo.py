'''
Algoritmos-em-bioinformatica
atividade-01-exercicio-03
Nome: Maria Paula Henriques Prandt

O exercício pede que seja feito uma simulação de Monte Carlo para calcular o valor aproximado do núemro pi.
Para isso, foram criadas duas funções: uma para calcular o valor de pi de acordo com a quantidade de pontos
escolhidos pelo usuário e outra que plota o gráfico da simulação.
'''

#importação das bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

#criação das funções para
#a
def calculapi(qnt):
    x = np.arange(0,qnt)/qnt
    y = np.random.randint(0,100,(qnt))/100
    yy = (1 - x**2)**(1/2)
    dentro = yy - y
    sel = dentro > 0
    d = dentro[sel]
    pi = (4 * d.size)/qnt
    print(f'O valor aproximado de pi é: {pi}')

#b
def pltsimulacao(qnt):
    x = np.arange(0,qnt)/qnt
    y = np.random.randint(0,100,(qnt))/100
    yy = (1 - x**2)**(1/2)
    for ponto in range(0,qnt):
        if y[ponto] <= yy[ponto]:
            plt.scatter(x[ponto],y[ponto], color='red')
        else:
            plt.scatter(x[ponto],y[ponto], color='blue')
    plt.plot(x,yy,color='black')
    plt.xlim(-0.07,1.07)
    plt.xlabel('raio')
    plt.ylim(-0.07,1.07)
    plt.ylabel('raio')
    plt.grid()
    plt.title(f'Monte Carlo - Calculo do pi com {qnt} pontos')
    plt.show()


print('Simulação de Monte Carlo' + 10*'-')
qnt = int(input('Entre com a quantidade de pontos que deseja utilizar:'))
calculapi(qnt)
pltsimulacao(qnt)

