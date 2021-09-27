"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-07
Nome: Maria Paula Henriques Prandt

O exercício pede para analisar a diferença entre duas sequências de nucleotídeos.
"""

# Open files
seqA = open('seq_a.fasta', 'r')
seqB = open('seq_b.fasta', 'r')

# Read files
seqA.readlines(1)
seqB.readlines(1)
A = seqA.read()
B = seqB.read()
c = 0
n=0

# Checar strings distintas
for s in range(0, 200):
    if A[s] != B[s]:
        print(f'A posição {s+1-n} foi trocado {A[s]} --> {B[s]}')
        c += 1
    elif A[s] == '\n':
        n += 1

print(f'O número de nucleotídeos diferentes é de {c}')

# Close files
seqA.close()
seqB.close()
