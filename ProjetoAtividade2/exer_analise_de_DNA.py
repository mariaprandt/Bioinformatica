"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-04
Nome: Maria Paula Henriques Prandt

O exercício pede para que seja extraido algumas informações a partir da sequencia de nucleotídeos
de um DNA
"""


seq = str(input('Entre com a sequência de nucleotídeos do DNA: ')).strip().upper().replace(' ', '')
l = 'ATCG'

#Identificando se a sequência é valida.
for char in seq:
    if char not in l:
        print('sequência de DNA invalida')
        exit()

print('A sequência digitada é válida')

#Calculando a quantidade de nucleotídeos da sequência
qnt = len(seq)
a = seq.count('A')
t = seq.count('T')
c = seq.count('C')
g = seq.count('G')

#Calculando a porcentagem de cada nucleotídeo da sequência.
fa = (a*100)/qnt
ft = (t*100)/qnt
fc = (c*100)/qnt
fg = (g*100)/qnt

#Exibindo resultados
print(f'O número totoal de nucleotídeos da sequência digitada é de: {qnt}')
print(f'A sequência difitada possui: \n {a} Adenina (A)\n {g} Guanina (G)\n {c} Citosina (C)\n {t} Timina (T)')
print(f"A frequência de nucleotídeos na sequência é de:\n {fa:.2f}% Adenina (A)\n {fg:.2f}% Guanina (G)\n {fc:.2f}% Citosina (C)\n "
      "{ft:.2f}% Timina (T)")
