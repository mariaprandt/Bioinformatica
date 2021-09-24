"""
Algoritmos-em-bioinformatica
atividade-01-exercicio-06
Nome: Maria Paula Henriques Prandt

"""

l=float(input('Digite a largura da parede que deseja pintar (em metros): '))
h=float(input('Digite a altura da parede (em metros): '))
a=h*l
print('Serão necessários {:.2f} litros de tinta para pintar a parede'.format(a/3))