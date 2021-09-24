# -*- coding: utf-8 -*-
"""
Algoritmos-em-bioinformatica
atividade-01-exercicio-03
Nome: Maria Paula Henriques Prandt

O exercício pede para que seja plotado diferentes gráficos das funções trigonométricas.
"""

#Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt 

#Função que cria uma divisão igualmente espaçada dado os valores finais e iniciais.
angle = np.linspace(-2*np.pi, 2*np.pi, 150)

#Definindo os eixos x e y.
x = np.linspace(-6,7,150)
y= np.sin(angle)

#Separando a tela em 4 partes e plotando a função seno na primeira parte.
plt.subplot(2,2,1)
plt.plot(x,y, color='red')
plt.title('Função sen(x)')

#Plotando a função cosseno na segunda parte.
plt.subplot(2,2,2)
plt.title('Função cos(x)')
yc = np.cos(angle)
plt.bar(x,yc)

#Plotando a função tangente na terceira parte.
plt.subplot(2,2,3)
plt.title('Função tg(x)')
yt = np.tan(angle)
plt.scatter(x,yt, linewidth=0.2)
plt.xlabel('valor de x')
plt.ylabel('valor de tg(x)')