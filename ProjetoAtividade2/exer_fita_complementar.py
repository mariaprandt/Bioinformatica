"""
Algoritmos-em-bioinformatica
atividade-02-exercicio-06
Nome: Maria Paula Henriques Prandt

O exercício pede para criar uma fita complementar a sequência de nucleotídeos do arquivo ex07.

"""

# Open files
dna = open('Corona_genomic.fasta', 'r')
resp = open('ex07_a.txt', 'w')

# Read files
dna.readlines(1)
d = dna.read()

# Criando fita correspondente
for char in d:
    if char in 'A':
        resp.write('T')
    elif char in 'T':
        resp.write('A')
    elif char in 'G':
        resp.write('C')
    elif char in 'C':
        resp.write('G')

# Close files
dna.close()
resp.close()