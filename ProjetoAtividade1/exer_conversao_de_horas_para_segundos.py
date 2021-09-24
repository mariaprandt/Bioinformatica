"""
Algoritmos-em-bioinformatica
atividade-01-exercicio-05
Nome: Maria Paula Henriques Prandt

"""

d=int(input('Entre com a quantidade de dias: '))
h=int(input('Entre com a quantidade de horas: '))
m=int(input('Entre com a quantidade de minutos: '))
s=int(input('Entre com a quantidade de segundos: '))

tots=((d*24)*3600)+h*3600+m*60+s

print('{} dias, {} horas, {} minutos e {} segundo, equivalem a {} segundos no total'.format(d,h,m,s,tots))